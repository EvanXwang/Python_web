import requests, bs4

# 八卦版
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ppt_gossiping = requests.get(url, cookies={'over18':'1'})
ppt_goss_soup = bs4.BeautifulSoup(ppt_gossiping.text,'lxml')
print (type (ppt_goss_soup))

articles = []
pttdivs = ppt_goss_soup.find_all('div','r-ent')
for p in pttdivs:
    if p.find('a'):
        title = p.find('a').text
        author = p.find('div','author').text
        href = p.find('a')['href']
        articles.append({'title':title,'author':author,'href':href,})

count = 0
for article in articles:
    count += 1
    print('編號：', count)
    print('標題：', article['title'] )
    print('作者：', article['author'])
    print('連結：', article['href'],'\n')

