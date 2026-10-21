from pathlib import Path
import pymupdf as f
import shutil
root=Path.cwd(); tmp=root/'tmp/pdfs/pccp'; backup=tmp/'originals'; backup.mkdir(exist_ok=True)
font='C:/Windows/Fonts/malgun.ttf'; bold='C:/Windows/Fonts/malgunbd.ttf'
def text(page,x,y,s,size=9,b=False,color=(0,0,0)):
    page.insert_font(fontname='krb' if b else 'kr',fontfile=bold if b else font)
    page.insert_text((x,y),s,fontsize=size,fontname='krb' if b else 'kr',color=color)
paths=[root/'회사지원/넥토리얼/박신우 클라이언트 포트폴리오.pdf',root/'이력서/박신우_이력서.pdf']
for idx,path in enumerate(paths):
    shutil.copy2(path,backup/path.name)
    d=f.open(path); p=d[0]
    if idx==0:
        text(p,930,310,'자격  PCCP Level 3 취득',21,color=(.15,.15,.17))
    else:
        text(p,35.433,461,'자격사항',9.5,True)
        xs=[35.433,225,390,565.7]; ys=[478,506.35,534.7]
        p.draw_rect(f.Rect(xs[0],ys[0],xs[-1],ys[1]),fill=(.949,.949,.949),color=None)
        for y in ys: p.draw_line((xs[0],y),(xs[-1],y),color=(.75,.75,.75),width=.45)
        for x in xs: p.draw_line((x,ys[0]),(x,ys[-1]),color=(.75,.75,.75),width=.45)
        for vals,y,b in [(['자격명','취득 등급','취득 여부'],496,True),(['PCCP','Level 3','취득'],524.35,False)]:
            ft=f.Font(fontfile=bold if b else font)
            for i,s in enumerate(vals): text(p,(xs[i]+xs[i+1]-ft.text_length(s,fontsize=8.7))/2,y,s,8.7,b)
    target=tmp/path.name; d.save(target,garbage=3,deflate=True);d.close()
    final=f.open(target); assert 'PCCP' in final[0].get_text(); assert len(final)==(18 if idx==0 else 1)
    final[0].get_pixmap(matrix=f.Matrix(1.4,1.4)).save(tmp/('after'+str(idx)+'.png'));final.close()
    shutil.copy2(target,path)
print('Updated both PDFs; original backups saved.')
