from pytube import YouTube

# 全局取消驗證
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

yt = YouTube('https://www.youtube.com/watch?v=3avsMx4MTkU')

print ('開始下載影片 請稍候')

yt.streams.first().download()

print('影片下載完成')