import os, logging, argparse, glob, cloudscraper
from bs4 import BeautifulSoup
from googlesearch import search
from datetime import date
from urllib.request import Request, urlopen

url='https://yogaspring.blogspot.com/'
year = date.today().year
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleW...'
#url_year = url+str(year)+'/'

def get_articles(url_blog):
    req = Request(url_blog)
    req.add_header('User-Agent',user_agent)
    page = urlopen(req)
    soup = BeautifulSoup(page,features="html.parser")
    images = soup.findAll('h3', {'class': 'post-title entry-title'})
    for image in images:
            url_chapter = image.a.get('href')
            print(url_chapter)

def get_text_articles(url_article):
    req = Request(url_blog)
    req.add_header('User-Agent',user_agent)
    page = urlopen(req)
    soup = BeautifulSoup(page,features="html.parser")
    images = soup.findAll('h3', {'class': 'post-title entry-title'})
    for image in images:
            url_chapter = image.a.get('href')
            print(url_chapter)

list_blogs=['https://feedreader.com/observe/my-yoga-blog.blogspot.com', 'https://gyanviyoga.blogspot.com/', 'http://mysuryayoga.blogspot.com/', 'https://66yoga.blogspot.com/', 'https://yogagypsy.blogspot.com/', 'http://yogaforhealthyaging.blogspot.com/', 'http://yogaspring.blogspot.com/', 'http://eyogateacher.blogspot.com/', 'http://thejoyofyoga.blogspot.com/', 'http://swadhyayayoga.blogspot.com/']

for blog in list_blogs:
    print(str(' '+blog+' ').center(len(blog)+10,'#'))
    get_articles(blog)

