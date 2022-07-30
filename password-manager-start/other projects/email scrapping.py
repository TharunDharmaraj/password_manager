#=============email scrapping=============
from requests_html import html
import re
from bs4 import BeautifulSoup

#page url
url =r"https://www.randomlists.com/email-addresses"

#regex pattern
pattern =r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"

#initialize the session
session = HTMLSession()

#send the get request
response = session.get(url)

#simulate JS running code
response.html.render()

#get body element
body = response.html.find("body")[0]

#extract emails
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", body.text)

for index,email in enumerate(emails):
    print(index+1, "---->", email)