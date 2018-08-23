# -*- coding=utf-8 -*-
#qq群:542110741

import requests
import re
import time
import json

def get_comment(itemid):
    i = 1#开始页码
    d = []#构建一个列表用于判断是否继续循环
    lis = []#放置抓取到的内容
    while i:
        #构建循环用的url        
        url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId={}&currentPageNum={}'.format(itemid,str(i))

        url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId={}&currentPageNum={}'.format('572621017964',1)
        html = requests.get(url).text#获取相关内容的源代码
        pl = re.findall(r'"content":"(.*?)","rateId"',html)#评论抓取
        dat = re.findall(r'"rateDate":"(.*?)","reply"',html)#评论时间抓取
        if dat == d or pl ==[]:#判断是否重复或者是否存在评论
            print('==============================')
            return lis #跳出循环并返回值
        else:
            try:
                d = dat#没有重复则将评论时间赋值给d，用于下次循环判断
            except IndexError as e:
                continue#出现该错误则跳出循环，进行下一次
        print("第%d页评论"%i,pl)#打印评论内容
        lis.append(pl)
        i += 1
        time.sleep(2)#访问间隔
        
        
        
def get_id(kw):

    url = 'https://s.taobao.com/api?_ksTS=1534994210547_238&m=customized&q={}'.format(kw)
    html = requests.get(url).json()
    
    list = html.get("API.CustomizedApi").get("itemlist").get("auctions")
    list[0].get('nid')
    type(list[0].get('nid'))
    nidList = []
    for item in list:
        nid = list[0].get('nid')
        nid.replace("'","")
        nidList.append(nid)
    return nidList

ids = get_id()
for idl in ids:
    liss = get_comment(idl)
    for lis in liss:
        with open('C:\pyTest\123.txt','a=') as f:
            f.write('\n'+li+'\n')