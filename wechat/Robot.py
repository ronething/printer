# -*- coding: utf-8 -*-
import sys
from wxpy import *
from tema import TeMa
import os
import random
from imgtest import MMp
import threading
import time
import re
from fmovice import *
from filedir import filesdir
#robot
bot=Bot(cache_path=True)
#列表
her=[]
#meizitu
mm=MMp()
ssList=mm.walkfunc()
#头像
headpath="f:/onethingrobot/Himg"
headimg=mm.walkfunc(headpath)
#美食
food=mm.walkfunc("f:/onethingrobot/Food")
#图灵机器人
tuling = Tuling(api_key="your tuling api_key")
#个人
my_friend=bot.friends().search(somebody)[0]
my_friend.send("Hello")
#emoji替换
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#使用时用print(a.translate(non_bmp_map))
#群列表
'''
groupList=[]
for i in bot.groups():
	if
'''
#计时器
def fun_timer():
	my_friend.send("可以起床了")
	global timer
	timer=threading.Timer(3,fun_timer)
	timer.start()
famgroup=bot.groups().search("We are family")[0]
#xiaxianggroup=bot.groups().search("下乡")[0]
#testgroup=bot.groups().search("20+1的天空")[0]
for i in bot.groups():
	#global twngroup
	if i.raw["Uin"]==dorkey:
		dorgroup=i
	#if i.raw["Uin"]==friendkey:
	#	friendgroup=i
	if i.raw["Uin"]==twnkey:
		twngroup=i
	if i.raw["Uin"]==ershoukey:
		ershougroup=i
	if i.raw["Uin"]==xiaxiangkey:
		xiaxianggroup=i
try:
	@bot.register(bot.groups())
	def reply_evey(msg):
		if msg.is_at and msg.type=="Text":
			if "@onething\u2005资源" in msg.text or "@onething 资源" in msg.text:
				if "@onething\u2005资源" in msg.text:
					info=re.compile("@onething\u2005资源")
				else:
					info=re.compile("@onething 资源")
				ques=info.sub("",msg.text)
				try:
					return movice.Search_main(ques)
				except:
					return "暂时搜索不到您想要的资源"
			try:
				tuling.do_reply(msg)
			except:
				return "我可能坏了"
		elif msg.type=="Recording":
			msg.forward(my_friend,prefix="有人发了语音消息")
	@bot.register(ershougroup)
	def reply_pic(msg):
		mt=msg.raw["MsgType"]
		if mt==3:
			try:
				msg.forward(my_friend)
			except:
				return "something error"
	@bot.register([jinpugroup,xiaxianggroup,dorgroup])
	def reply_jinpu(msg):
		global her
		mt=msg.raw["MsgType"]
		if msg.is_at:
			md=msg.raw["MsgId"]
			if len(her)==50:
				her=[her[-1]]
			her.append(md)
			if msg.type=="Text":
				if "@onething\u2005资源" in msg.text or "@onething 资源" in msg.text:
					if "@onething\u2005资源" in msg.text:
						info=re.compile("@onething\u2005资源")
					else:
						info=re.compile("@onething 资源")
					ques=info.sub("",msg.text)
					try:
						return movice.Search_main(ques)
					except:
						return "暂时搜索不到您想要的资源"
				try:
					tuling.do_reply(msg)
				except:
					return "可能哪里有问题"
		elif msg.text=="大家晚安":
			retfood=random.choice(food)
			msg.reply_image(retfood)
			return
		elif mt==10002:
			msgid=re.search(r'(?<=\<msgid\>)(.+?)(?=\</msgid\>)',msg.raw["Content"])
			#test=his.pop(msgid.group())
			bot.messages.reverse()
			for i in bot.messages:
				if msgid.group()==str(i.id):
					try:
						if i.member:
							i.forward(my_friend,prefix=i.member)
						else:
							i.forward(my_friend,prefix=i.sender)
					except:
						return "他们也许撤回太快了"
			#msg.chat.send_raw_msg(test[0],test[1])
		else:
			md=msg.raw["MsgId"]
			#his[md]=[mt,msg.raw["Content"]]
			if len(her)==50:
				her=[her[-1]]
			her.append(md)
			#return "你发了"+str(mt)
	@bot.register(twngroup)
	def get_mm(msg):
		global her
		mt=msg.raw["MsgType"]
		if msg.is_at:
			md=msg.raw["MsgId"]
			if len(her)==50:
				her=[her[-1]]
			her.append(md)
			if msg.type=="Text":
				if "@onething\u2005资源" in msg.text or "@onething 资源" in msg.text:
					if "@onething\u2005资源" in msg.text:
						info=re.compile("@onething\u2005资源")
					else:
						info=re.compile("@onething 资源")
					ques=info.sub("",msg.text)
					try:
						return movice.Search_main(ques)
					except:
						return "暂时搜索不到您想要的资源"
				if msg.text=="@onething\u2005妹子" or msg.text=="@onething 妹子":
					mmp=random.choice(ssList)
					msg.reply_image(mmp)
					return
				else:
					try:
						tuling.do_reply(msg)
					except:
						return "可能哪里有问题"
		elif mt==10002:
			msgid=re.search(r'(?<=\<msgid\>)(.+?)(?=\</msgid\>)',msg.raw["Content"])
			#test=his.pop(msgid.group())
			bot.messages.reverse()
			for i in bot.messages:
				if msgid.group()==str(i.id):
					try:
						i.forward(my_friend,prefix=i.sender)
					except:
						return "他们也许撤回太快了"
			#msg.chat.send_raw_msg(test[0],test[1])
		else:
			md=msg.raw["MsgId"]
			if len(her)==50:
				her=[her[-1]]
			#his[md]=[mt,msg.raw["Content"]]
			her.append(md)
			#return "你发了"+str(mt)
	@bot.register(famgroup)
	def reply_fam(msg):
		if msg.is_at:
			if ("码" in msg.text or "6" in msg.text) and msg.type=="Text":
				ma=TeMa()
				return ma.liuhe()
			else:
				try:
					tuling.do_reply(msg)
				except:
					return "万一我坏了呢"
	@bot.register(my_friend)
	def reply_my_friend(msg):
		if msg.type=="Note":
			return "据说你撤回了消息"
		else:
			if msg.text=="测试":
				mmp=random.choice(ssList)
				msg.reply_image(mmp)
			elif msg.text=="启动":
				global timer
				timer=threading.Timer(1,fun_timer)
				timer.start()
			elif msg.text=="停止":
				global timer
				timer.cancel()
			elif msg.text[:3]=="cmd" or msg.text[:3]== "Cmd" :
				if msg.text[3:] == "当前":
					return os.getcwd()
				flag = filesdir(msg)
				if not flag:
					return msg.text[3:]+"指令已完成"
				if flag==1:
					my_friend.send_file("filesdir.txt")
				if flag==2:
					return "请输入正确cmd指令."
			elif msg.text[:3]=="get"or msg.text[:3]=="Get":
				try:
					my_friend.send_file(msg.text[3:])
				except:
					return "错误指令"
			elif msg.text=="特码":
				ma=TeMa()
				return ma.liuhe()
			elif "资源" in msg.text:
				info=re.compile("资源")
				ques=info.sub("",msg.text)
				try:
					return movice.Search_main(ques)
				except:
					return "暂时搜索不到您想要的资源"
			elif "头像" in msg.text:
				head=random.choice(headimg)
				msg.reply_image(head)
				return
			else:
				try:
					tuling.do_reply(msg)
				except:
					return "也许我坏了呢"
except:
	pass
embed()
