#coding=utf-8

from ftplib import FTP
import time
import os

HOST = "127.0.0.1"
PORT = 2121
USER = "user"
PASSWORD = "12345"
LEVEL = 0           # debug等级

# 连接ftp并且登录user用户
def ftpconnect(host=HOST,port=PORT,username=USER,password=PASSWORD):
    ftp = FTP()
    ftp.set_debuglevel(LEVEL)
    ftp.connect(host,port)
    ftp.login(username,password)
    return ftp

# 下载文件
def downloadfile(ftp,remotepath,localpath):
    bufsize = 1024
    ftp.set_debuglevel(LEVEL)
    try:
        fp = open(localpath,"wb")
        ftp.retrbinary("RETR " + remotepath, fp.write, bufsize)
        filename = os.path.split(remotepath)[-1]
        print('成功下载文件：{0}'.format(filename))
        fp.close()
        return True
    except Exception as e:
        print("发生错误，错误原因：")
        print(e)
        return False

# 上传文件
def uploadfile(ftp,remotepath,localpath):
    bufsize = 1024
    ftp.set_debuglevel(LEVEL)
    try:
        fp = open(localpath,"rb")
        ftp.storbinary("STOR " + remotepath, fp, bufsize)
        filename = os.path.split(remotepath)[-1]
        print("成功上传文件：{0}".format(filename))
        fp.close()
        return True
    except Exception as e:
        print("发生错误，错误原因：")
        print(e)
        return False

# 退出ftp连接
def ftpquit(ftp):
    ftp.quit()

# 将服务器上的文件 fromname 重命名为 toname
def ftprename(ftp,fromname,toname):
    try:
        ftp.rename(fromname,toname)
        return True
    except Exception as e:
        print(e)
        return False

# 在服务器上创建一个新目录
def ftpmkdir(ftp,pathname):
    try:
        ftp.mkd(pathname)
        return True
    except Exception as e:
        print(e)
        return False

# 删除目录
def ftprmdir(ftp,pathname):
    try:
        ftp.cwd(pathname)
        for i in ftp.nlst():
            print(i)
            try:
                ftp.delete(i)
            except:
                ftprmdir(ftp,i)
        ftp.cwd("..")
        ftp.rmd(pathname)
        return True
    except Exception as e:
        print(e)
        return False

# 删除文件
def ftpdelfile(ftp,filename):
    try:
        ftp.delete(filename)
        return True
    except Exception as e:
        print(e)
        return False

# 设置服务器上的当前目录
def ftpcwd(ftp,pathname):
    try:
        ftp.cwd(pathname)
        return True
    except Exception as e:
        print(e)
        return False

# 主函数
def main():
    print("简单FTP客户端软件")
    welcome = """
    1：连接ftp服务器
    2：关闭连接
    3：欢迎信息
    4：列出当前目录下的文件
    5：目录/文件重命名
    6：文件下载
    7：文件上传
    8：目录创建
    9：目录删除
    10：文件删除
    11：设置服务器上的当前目录
    12：服务器上当前目录的路径名
    q：退出程序
    """
    while True:
        print(welcome)
        choose = str(input("请输入你的选择："))
        if choose=='1':
            ftp = ftpconnect()
            print("已连接ftp服务器并登录")
        elif choose=='2':
            ftpquit(ftp)
            print("已关闭连接")
        elif choose=='3':
            print(ftp.getwelcome())
        elif choose=='q':
            print("退出ftp客户端软件程序")
            break
        elif choose=='4':
            ftp.dir()
        elif choose=='5':
            fromname = str(input("要重命名的文件或目录："))
            toname   = str(input("重命名为："))
            res = ftprename(ftp,fromname,toname)
            if(res):
                print("修改成功")
            else:
                print("修改失败")
        elif choose=='6':
            downremotepath = str(input("要下载文件在服务器上的路径："))
            downlocalpath  = str(input("下载到本地的路径："))
            res = downloadfile(ftp,downremotepath,downlocalpath)
            if(res):
                print("下载成功")
            else:
                print("下载失败")
        elif choose=='7':
            uploadlocalpath  = str(input("上传的文件在本地的路径："))
            uploadremotepath = str(input("文件要上传到服务器上的路径："))
            res = uploadfile(ftp,uploadremotepath,uploadlocalpath)
            if(res):
                print("上传成功")
            else:
                print("上传失败")
        elif choose=='8':
            dirname = str(input("要创建的目录名："))
            res = ftpmkdir(ftp,dirname)
            if(res):
                print("创建成功")
            else:
                print("创建失败")
        elif choose=='9':
            dirname = str(input("要删除的目录名："))
            res = ftprmdir(ftp,dirname)
            if(res):
                print("删除成功")
            else:
                print("删除失败")
        elif choose=='10':
            filename = str(input("要删除的文件名："))
            res = ftpdelfile(ftp,filename)
            if(res):
                print("删除成功")
            else:
                print("删除失败")
        elif choose=='11':
            pathname = str(input("要进入哪个目录："))
            res = ftpcwd(ftp,pathname)
            if(res):
                print("进入成功")
            else:
                print("进入失败")
        elif choose=='12':
            print(ftp.pwd())
        else:
            print("请仔细阅读说明并重新输入")

if __name__=="__main__":
    main()
