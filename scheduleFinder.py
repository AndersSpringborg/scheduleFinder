import urllib
import re

from bs4 import BeautifulSoup

def main():
    
    for n in range(7000,10000):
        print('id: %d' % n, end='\r')

        data = urllib.request.urlopen('https://www.moodle.aau.dk/calmoodle/public/?sid=%d' % n).read()
        soup = BeautifulSoup(data, 'html5lib')
        title = soup.find('h1', attrs={'class': 'aalborg_title'})
        match = re.match('.*Software 5.*', title.text)
        if match:
            print("match at id %d" %n)
            return

main()
print()

