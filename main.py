# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
import zipfile
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
from os.path  import basename
def get_chapters(url):
    test_site = url
    hdr = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'}
    site = requests.get(test_site)
    soup = BeautifulSoup(site.text)
    ahref = soup.find("div", {"class": "group-box list",}).find_all('a', href=True)
    links= []
    for a in ahref:
        links.append(a['href'])

    scrape_chapters(links)

def scrape_chapters(chapters):
    #print(chapters)
    #chaptername = chapters[0]
    #print(chaptername.split('/')[3])
    hdr = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'}
    for count, value in enumerate(chapters):
        print(count)

        site = requests.get(chapters[count])
        soup = BeautifulSoup(site.text)

        chaptername = chapters[count]
        splitschaptername=chaptername.split('/')[3]
        pictures= soup.find_all('img', src=True)
        picturelinks=[]
        for a in pictures:
            picturelinks.append(a['src'])

        print(picturelinks)
        counter=1
        with zipfile.ZipFile(splitschaptername+'.cbr', 'w') as img_zip:
            for image_url in picturelinks:

                img_name = os.path.basename(str(counter).zfill(3)+'.jpg')
                img_data = requests.get(image_url).content
                img_zip.writestr(img_name, img_data)
                counter+=1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_chapters(sys.argv[1])

