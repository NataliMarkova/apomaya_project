import requests
from bs4 import BeautifulSoup

url = 'https://apomaya.com'

page = requests.get(url)
page_status = page.status_code
if page_status == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    scripts = soup.find_all('script')
    page2 = requests.get(scripts[3]['src'])
    count = page2.text.count('return')
    print("Number of returns: " + str(count) + '\n')
    print("Response headers: \n")
    print(page2.headers)





