from urllib.request import urlopen
import html.parser
html = urlopen("http://www.wikipedia.com/")
for el in html:
    print(el)
