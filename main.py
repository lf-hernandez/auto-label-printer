from requests import get
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import re
from win32printing import Printer

def getLinks(url):
    links = []
    document = BeautifulSoup(response, "html.parser")

    for element in document.findAll('a', href=re.compile(".pdf$")):
        links.append(element.get('href'))

    return links

site = 'https://greenteapress.com/wp/think-python/'

http = httplib2.Http()
status, response = http.request(site)
pdf_links = getLinks(response) 

files = []

for link in pdf_links:
    pdf_file = requests.get(url)
    files.append(pdf_file)

with Printer(linegap=1) as printer:
    for pdf_file in files:
        printer.text(pdf_file)