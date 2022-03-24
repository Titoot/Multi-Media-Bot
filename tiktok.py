import requests
import re

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
regex = r'.*tiktok\.com\/(@.*)\/video\/(\d*)'
def VerifyLink(url):

    if re.match(regex, url):
        return True
        
def get_url(url):

    m = re.match(regex,url)
    print(m[1])
    print(m[2])
    url = 'https://www.tiktok.com/node/share/video/{0}/{1}'.format(m[1],m[2])
    s = requests.Session()
    r = s.get(url, headers= {
        "User-Agent": userAgent
    })
    data = r.json()

    videoUrl = data["itemInfo"]["itemStruct"]["video"]["downloadAddr"]


    print(videoUrl)
    return videoUrl