# -*- coding: utf-8 -*-
# 获取wechat通讯录中所有好友的个性签名
import sys
from wxpy import *
import os
import random
import re

tList=[]
bot=Bot()
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#使用时用print(a.translate(non_bmp_map))
for i in bot.friends():
	signature = ((i.raw["Signature"]).translate(non_bmp_map)).replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
	rep = re.compile("1f\d.+")
	signature = rep.sub("", signature)
	rep = re.compile("<?>")
	signature = rep.sub("", signature)
	tList.append(signature)

text="".join(tList)
print (text)

