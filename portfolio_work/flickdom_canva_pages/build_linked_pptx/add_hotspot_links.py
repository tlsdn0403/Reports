from __future__ import annotations

import argparse
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
HYPERLINK_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink"

ET.register_namespace("p", P_NS)
ET.register_namespace("a", A_NS)
ET.register_namespace("r", R_NS)


def add_relationship(root: ET.Element, rel_id: str, target: str) -> None:
    for rel in root.findall(f"{{{PKG_REL_NS}}}Relationship"):
        if rel.get("Id") == rel_id:
            rel.set("Target", target)
            rel.set("Type", HYPERLINK_REL_TYPE)
            rel.set("TargetMode", "External")
            return

    ET.SubElement(
        root,
        f"{{{PKG_REL_NS}}}Relationship",
        {
            "Id": rel_id,
            "Type": HYPERLINK_REL_TYPE,
            "Target": target,
            "TargetMode": "External",
        },
    )


def add_shape_link(slide_root: ET.Element, shape_name: str, rel_id: str) -> None:
    for c_nv_pr in slide_root.findall(f".//{{{P_NS}}}cNvPr"):
        if c_nv_pr.get("name") != shape_name:
            continue

        for existing in c_nv_pr.findall(f"{{{A_NS}}}hlinkClick"):
            c_nv_pr.remove(existing)

        hlink = ET.Element(f"{{{A_NS}}}hlinkClick", {f"{{{R_NS}}}id": rel_id})
        ext_lst = c_nv_pr.find(f"{{{A_NS}}}extLst")
        if ext_lst is None:
            c_nv_pr.append(hlink)
        else:
            insert_at = list(c_nv_pr).index(ext_lst)
            c_nv_pr.insert(insert_at, hlink)
        return

    raise RuntimeError(f"Could not find shape named {shape_name!r}")


def patch_pptx(input_path: Path, output_path: Path) -> None:
    replacements = {
        "ppt/slides/slide1.xml": None,
        "ppt/slides/_rels/slide1.xml.rels": None,
    }

    with zipfile.ZipFile(input_path, "r") as zin:
        slide_xml = zin.read("ppt/slides/slide1.xml")
        rels_xml = zin.read("ppt/slides/_rels/slide1.xml.rels")

    slide_root = ET.fromstring(slide_xml)
    rels_root = ET.fromstring(rels_xml.decode("utf-8-sig").encode("utf-8"))

    add_relationship(rels_root, "rIdFlickDomGithub", "https://github.com/AACHANJINAA/FlickDom")
    add_relationship(rels_root, "rIdFlickDomVideo", "https://www.youtube.com/watch?v=ddM9ggItGwQ&feature=youtu.be")
    add_shape_link(slide_root, "github-link-hotspot", "rIdFlickDomGithub")
    add_shape_link(slide_root, "video-link-hotspot", "rIdFlickDomVideo")

    replacements["ppt/slides/slide1.xml"] = ET.tostring(slide_root, encoding="utf-8", xml_declaration=True)
    replacements["ppt/slides/_rels/slide1.xml.rels"] = ET.tostring(rels_root, encoding="utf-8", xml_declaration=True)

    if output_path.exists():
        output_path.unlink()

    with zipfile.ZipFile(input_path, "r") as zin, zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = replacements.get(item.filename)
            if data is None:
                data = zin.read(item.filename)
            zout.writestr(item, data)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    patch_pptx(args.input, args.output)


if __name__ == "__main__":
    main()
