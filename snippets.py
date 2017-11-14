#get web resource
from urllib.request import urlopen
import html.parser
html = urlopen("http://www.wikipedia.com/")
for el in html:
    print(el)
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
