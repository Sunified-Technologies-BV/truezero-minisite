import base64
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sunified · True Zero You Can Verify.</title>
<meta name="description" content="Creating a global green energy data standard. Sunified’s Unity Chip signs the energy measurement on the panel. Finalist, True Zero Global Prize 2026.">
<meta property="og:title" content="Sunified · True Zero You Can Verify.">
<meta property="og:description" content="Creating a global green energy data standard. Finalist, True Zero Global Prize 2026.">
<meta property="og:image" content="media/poster.jpg">
<meta name="theme-color" content="#003E52">
<style>
'''
css=open('base.css',encoding='utf-8').read()+open('extra.css',encoding='utf-8').read()
body=open('body.html',encoding='utf-8').read()
t=head+css+'</style>\n</head>\n'+body
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
for k,v in {'{{FONT_R}}':b('build/Inter-Regular.woff2'),'{{FONT_M}}':b('build/Inter-Medium.woff2'),'{{FONT_S}}':b('build/Inter-SemiBold.woff2'),'{{WORDMARK}}':b('build/wordmark.png'),'{{CHIP}}':b('build/chip.jpg'),'{{BADGE}}':b('build/badge.png')}.items(): t=t.replace(k,v)
open('index.src.html','w',encoding='utf-8').write(head+css+'</style>\n</head>\n'+body)
open('public/index.html','w',encoding='utf-8').write(t)
print('bytes',len(t.encode()),'em',t.count('—'),'en',t.count('–'),'placeholders left',t.count('{{'))
