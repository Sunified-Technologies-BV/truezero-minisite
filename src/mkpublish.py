import re
s=open('site/public/index.html',encoding='utf-8').read()
s=s.replace('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>Sunified · True Zero You Can Verify.</title>\n',
            '<title>Sunified True Zero Pitch</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n')
s=s.replace('</head>\n<body>\n','\n').replace('</body>\n</html>\n','\n')
s=s.replace('.wrap{max-width:1280px;margin:0 auto;padding:0 var(--gutter);position:relative}','.wrap{max-width:1280px;margin:0 auto;padding-left:max(var(--gutter),env(safe-area-inset-left,0px));padding-right:max(var(--gutter),env(safe-area-inset-right,0px));position:relative}')
s=s.replace('nav{position:sticky;top:0;z-index:30;','nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:30;')
s=s.replace('<a href="media/Sunified-TRUE-ZERO-Global-Prize-V1.pdf" download>Download PDF (4.7 MB)</a>','<a href="media/Sunified-TRUE-ZERO-Global-Prize-V1.pdf" target="_blank" rel="noopener">Open the PDF (4.7 MB)</a>')
assert '<!doctype' not in s and '<body>' not in s and 'safe-area-inset-top' in s and ' download>' not in s
open('publish/index.html','w',encoding='utf-8').write(s); print('publish bytes',len(s.encode()))
