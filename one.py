#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:00:47 2019

@author: hang-star
"""
import re,requests
from requests.exceptions import RequestException
import json,time

def get_one_page(url):
    try :
        headers ={
            'Users-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'
            }
        response =requests.get(url,headers=headers)
        if response.status_code ==200:
            return response.text
        return None
    except RequestException :
        return None

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html =get_one_page(url)
    #print (html)
    parse_one_page(html)
    for item in parse_one_page(html):
        write_file(item)
        print (item)

def parse_one_page(html):
    pattern =re.compile(
            '<dd>.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?title="(.*?)".*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
            
    items=re.findall(pattern,html)
    for item in items :
        yield{
          'index':item[0],
          'image':item[1],
          'title':item[2].strip(),
          'actor':item[3].strip()[3:],
          'time':item[4].strip()[5:],
          'score':item[5]+item[6]
              }
        
def write_file(content):
    with open ('result1.txt','a',encoding ='utf-8') as f:
        #print (type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

if __name__ == "__main__":    
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)










