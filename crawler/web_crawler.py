# 抓取PTT電影版的網頁原始碼（HTML）
import urllib.request as req

def getData(url):

	# 建立一個Request物件，附加Request Headers的資訊
	request=req.Request(url, headers={
		"cookie":"over18=1",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
	})
	with req.urlopen(request) as response:
		data=response.read().decode("utf-8")

	# 解析原始碼，取得每篇文章的標題
	import bs4
	root=bs4.BeautifulSoup(data, "html.parser")
	titles=root.find_all("div", class_="title")# 尋找所有class="title"的div標籤
	for title in titles:
		if title.a != None:  # 如果標題包含a標籤 （沒有被刪除）.印出來
			print (title.a.string)
	# 抓取上一頁的連結
	nextLink=root.find("a", string="‹ 上頁")# 找到內文是‹ 上頁 的a 標籤
	return nextLink["href"]


pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
	pageURL="https://www.ptt.cc"+getData(pageURL)
	count+=1


