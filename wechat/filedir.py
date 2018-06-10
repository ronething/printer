# -*- coding: utf-8 -*-

import os
def filesdir(msg):
    if msg.text[:3] == "cmd" or msg.text[:3]=="Cmd" :
        if msg.text[3:] == "清空":
            with open("filesdir.txt", "w") as f:
                f.truncate()
                return 0
        elif msg.text[3:] == "返回":
            os.chdir("f:/onethingrobot")
            return 0
        elif msg.text[3:] == "f:":
            os.chdir("..")
        elif msg.text[3:5] == "路径":
            try:
                os.chdir(msg.text[5:])
                return 0
            except:
                return 2
        else:
            try:
                filedir = os.popen(msg.text[3:])
                read=filedir.read()
                if not read:
                    return 2
            except:
                return 2
            with open("filesdir.txt", "a") as f:
                f.write(read)
                return 1
