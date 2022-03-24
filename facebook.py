import re
import requests as r
from urllib.parse import unquote
import json
#import urllib.request
#opener = urllib.request.build_opener()
#urllib.request.install_opener(opener)
#import os
#import yt_dlp

text = 'ستوريز؟ بجد!  انت جاي تهزر ولا ايه, خلي حوارات الكراش ديه بعيد'

headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With':'XMLHttpRequest'}

#--merge-output-format FORMAT 
regex = r'.*\.facebook\.com\/\d*\/videos\/\d*.*'
regexStories = r'.*\.facebook\.com\/stories\/videos\/\d*'
#https://www.facebook.com/stories/113510457238643

def download(url):
  if re.match(regex,url):
    data = {'query': url}
    html = r.post('https://fbdownloader.net/ajax', headers=headers, data=data)
   
    m = json.loads(html.text)["downloadUrl"]
    print(m)
    #print(m[0])
    #print()
    #a = m[0]+'='*18+m[len(m)]
    #urllib.request.urlretrieve(key, '1.mp4')
    
    return unquote(m.replace('amp;',''))
    #return 'كسم الفيس'
      
  elif re.match(regexStories,url):

    return text
  else:
    return 'Error: Unsupported Facebook Url'