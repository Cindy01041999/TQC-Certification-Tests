# -*- coding: utf-8 -*-
'''
請撰寫一程式，爬取 https://www.codejudger.com/target/5203.html
程式須回傳下列資訊：
1.大樂透的開出順序
2.大樂透的大小順序
3.大樂透的特別號
'''
import bs4
import requests

url = 'https://www.codejudger.com/target/5203.html'
# GET 請求
html = requests.get(url)

# 使用 lxml 解析器
objSoup = bs4.BeautifulSoup(html.text,'lxml')

dataTag = objSoup.select('.contents_box02')

balls = dataTag[2].find_all('div', {'class':'ball_tx ball_yellow'})
print("大樂透開獎 : ")
print('-------------')

# 開出順序
print("開出順序 : ", end='')
for i in range(6):
    print(balls[i].text, end='   ')

# 大小順序
print("\n大小順序 : ", end='')
for i in range(6, len(balls)):
    print(balls[i].text, end='   ')

# 特別號：資料位於 <div class="ball_red"></div>
redball = dataTag[2].find_all('div', {'class': 'ball_red'})
print("\n特別號   :", redball[0].text)
