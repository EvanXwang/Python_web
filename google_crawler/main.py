import requests
url = "https://www.google.com/search?ei=Z3KJXYefGIK0mAX-vp64CQ&yv=3&q=%E6%B5%A3%E7%86%8A&tbm=isch&vet=10ahUKEwjH7qivqOjkAhUCGqYKHX6fB5cQuT0ISigB.Z3KJXYefGIK0mAX-vp64CQ.i&ved=0ahUKEwjH7qivqOjkAhUCGqYKHX6fB5cQuT0ISigB&ijn=1&start=100&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc"
h = {
    "accept-language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
response = requests.get(url, headers=h)
response.text
from bs4 import BeautifulSoup
import json
html = BeautifulSoup(response.text)
div = html.find("div", class_="rg_meta")
print("盒子:", div)
print("網址:", json.loads(div.text)["ou"])

# 拿到每一頁每一張圖片網址
import requests
from bs4 import BeautifulSoup
import json

imgs_url = []
page = 0
while True:
    # TODO: 看你要搜尋啥
    url = (
                "https://www.google.com/search?ei=Z3KJXYefGIK0mAX-vp64CQ&yv=3&q=請輸入關鍵字&tbm=isch&vet=10ahUKEwjH7qivqOjkAhUCGqYKHX6fB5cQuT0ISigB.Z3KJXYefGIK0mAX-vp64CQ.i&ved=0ahUKEwjH7qivqOjkAhUCGqYKHX6fB5cQuT0ISigB&ijn="
                + str(page) + "&start="
                + str(page * 100) + "&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc")
    print("第幾頁:", page + 1)
    print("網址:", url)
    h = {
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
    response = requests.get(url, headers=h)

    html = BeautifulSoup(response.text)
    divs = html.find_all("div", class_="rg_meta")

    if len(divs) == 0:
        print("應該是最後一頁了")
        break

    print("這頁有幾張?", len(divs))
    for d in divs:
        img = json.loads(d.text)["ou"]
        imgs_url.append(img)
    page = page + 1

# 下載圖片
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# TODO: save to
base = "Download"
if not os.path.exists(base):
    os.makedirs(base)
saved = ["jpg", "jpeg", "png"]
for i, iurl in enumerate(imgs_url):
    for f in saved:
        if f.upper() in iurl or f in iurl:
            try:
                h = {
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
                }
                iresponse = requests.get(iurl, headers=h, stream=True, verify=False)
                fn = os.path.join(base, str(i) + "." + f)
                with open(fn, "wb") as f:
                    # .read: .raw是一個檔案, 使用read去讀取
                    f.write(iresponse.raw.read())
            except:
                print("放棄:", iurl)