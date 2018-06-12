# -*- coding: UTF-8 -*-
import re
from urllib import request
import time
class TeMa:
    def __init__(self):
        pass
    def liuhe(self):
        try:
            ss=""
            url=r"http://www.6hck.co/diaoyong/"
            response=request.urlopen(url,timeout=10)
            html=(response.read()[5000:]).decode("utf-8")
            opentime=html.find(u"最新开奖")
            #return str(opentime)
            thetime=re.search(r"\d{4}(\-|\/|\.)\d{1,2}\1\d{1,2}",html[opentime:opentime+35])
            ss+=thetime.group()+"\n"
            cont=0
            balls=[]
            a=html.find("ball",opentime)
            while a!=-1:
                b = html.find("</span>",a,a+30)
                if b!=-1:
                    balls.append(html[b-2:b])
                    cont+=1
                    if cont==7:
                        break;
                a = html.find("ball",b)
            for i in range(len(balls)-1): 
                ss+="码仔:"+balls[i]+"\n"
            ss+="特码:"+balls[6]
            return ss
        except:
            mpurl="http://m.6hck.vip"
            return "抱歉暂时无法查询≧ ﹏ ≦\n点击自行查看"+mpurl
'''
a=TeMa()
print (a.liuhe())
'''


