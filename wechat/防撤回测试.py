#coding=utf-8
import os
import re
from wxpy import *
bot=Bot()
my_friend=bot.friends().search(somebody)[0]
my_friend.send("撤回测试")
#字典
his={}
#列表
her=[]
@bot.register(my_friend)
def reply(msg):
    mt=msg.raw["MsgType"]
    # 获取消息类型，10002为被撤回类型
    if mt==10002:
        msgid=re.search(r'(?<=\<msgid\>)(.+?)(?=\</msgid\>)',msg.raw["Content"])
        #test=his.pop(msgid.group())
        bot.messages.reverse()
        for i in bot.messages:
            if msgid.group()==str(i.id):
                try:
                    # 发送被撤回的消息给文件传输助手
                    i.forward(bot.file_helper,prefix=i.sender)
                except:
                    return "他们也许撤回太快了"
        #msg.chat.send_raw_msg(test[0],test[1])
    else:
        md=msg.raw["MsgId"]
        #his[md]=[mt,msg.raw["Content"]]
        her.append(md)
        return "你发了"+str(mt)

embed()
