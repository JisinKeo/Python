import urllib.request
from bs4 import BeautifulSoup
import re
import csv
from selenium import webdriver
import time
hdr = { 'User-Agent' : 'Mozilla/5.0' }
url = 'https://www.melon.com/artistplus/artistchart/index.htm'

req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

# driver = webdriver.Chrome()
# driver.get(url)

# artistplus_li = soup.select('.artistplus_li')

# for i in artistplus_li:
#     print(i.select_one('.rank.top').text, end = '위 ')
#     print(i.select_one('.ellipsis').text, end = ' ')
#     print(i.select_one('.gubun').text, end = ' ')



# driver.find_element_by_css_selector("span.even_span").click()
# index = soup.find_all("li", attrs={'data-page-index':re.compile('^1')})
# idx = index.find("span", attrs={'class':'rank'}).get_text()
# print(idx)

artistplus_li = soup.find_all("li", attrs={'class':re.compile('^artistplus_li')})
#print(artistplus_li[0].find("a", attrs={'class':'ellipsis'}).get_text())
list=[]
for i in artistplus_li:
    temp=[]
    rank = i.find("span", attrs={'class':'rank'}).get_text()
    temp.append(rank)
    name = i.find("a", attrs={'class':'ellipsis'}).get_text()
    temp.append(name)
    # rank_top = i.find("span", attrs={'class':'rank top'}).get_text()
    # if rank_top:
    #     rank_top = rank_top.get_text()
    fan = i.find("dd", attrs={'class':'gubun'}).get_text()
    temp.append(fan)
    list.append(temp)

for i in range(len(list)):
    print(list[i])
    
with open('melon_artist.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['순위','아티스트','팬 수'])
    writer.writerows(list)
