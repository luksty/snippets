from urllib.request import urlopen
import html.parser
html = urlopen("http://www.wikipedia.com/")
for el in html:
    print(el)
# xxx


import os
os.chdir(r'C:\Users\luksty\OneDrive - Syncron\TEMP\.vim\plugged\vim-colorschemes\colors')
dir=[el[:-4].upper() for el in os.listdir() if el[-3:]=='vim']
scheme=vim.eval("g:colors_name")
try:
    index=dir.index(scheme.upper())
except:
    index=dir.index(c[-1])
    index=index+1
index=index+1
vim.command('colorscheme '+dir[index])
[print(line) for line in c]
print(dir[index])
# xxx


# group by groupby modulo number of line with dict
d = {}
for idx, line in enumerate(c):
    key, value = idx % 6, line
    l = d.get(key, [])
    l.append(value)
    d[key] = l

print(d)
# xxx
