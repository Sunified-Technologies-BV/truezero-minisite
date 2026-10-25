import base64,re
t=open('index.src.html',encoding='utf-8').read()
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
rep={'{{FONT_R}}':b('build/Inter-Regular.woff2'),'{{FONT_M}}':b('build/Inter-Medium.woff2'),'{{FONT_S}}':b('build/Inter-SemiBold.woff2'),'{{WORDMARK}}':b('build/wordmark.png'),'{{CHIP}}':b('build/chip.jpg'),'{{BADGE}}':b('build/badge.png')}
for k,v in rep.items(): t=t.replace(k,v)
open('public/index.html','w',encoding='utf-8').write(t)
print('bytes',len(t.encode()),'em',t.count('—'),'en',t.count('–'))
