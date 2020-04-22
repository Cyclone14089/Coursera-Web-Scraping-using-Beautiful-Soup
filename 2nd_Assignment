import urllib.request
from bs4 import *

currentRepeatCount = 0
url = input('Enter url : ')
repeatCount = int(input('Enter count : '))
position = int(input('Enter position : '))

def parse_html(url) :
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while currentRepeatCount < repeatCount :
    print('Retrieving url : ', url)
    tags = parse_html(url)
    for index,item in enumerate(tags) :
        if index == position - 1 :
            url = item.get('href', None)
            name = item.contents[0]
            break
    currentRepeatCount = currentRepeatCount + 1

print("\nLast url :", url)
