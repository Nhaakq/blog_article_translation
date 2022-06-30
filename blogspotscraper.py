import requests
from bs4 import BeautifulSoup

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
query = "inurl:blogspot.com yoga"
 
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)