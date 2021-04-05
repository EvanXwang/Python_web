## Youtube 下載影片

一開始會出現錯誤訊息如下：(提示SSL验证失败)    
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>  

需加入：  
import ssl  
ssl._create_default_https_context = ssl._create_unverified_context

