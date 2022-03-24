import requests as r
import re
from textwrap import wrap

#list = ["batch": "at" ]
def get_paste(url):
  h = r.get(url)
  type = re.search('class="btn -small h_800">(.+?)</a>',h.text).group(1)
  url = re.match(r'.*pastebin.com\/(.*)',url)[1]
  url = f'https://pastebin.com/raw/{url}'
  print(url)
  type = type.lower()
  print(type)
  h = r.get(url)
  #h = h.text
  h = wrap(h.text,1500)
  return h, type