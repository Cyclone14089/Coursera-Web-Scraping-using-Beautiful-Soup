import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL : ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
s = 0
c = 0
for tag in tags :
    s = s + int((tag.contents[0]))
    c = c + 1

print('Count',c)
print('Sum',s)
