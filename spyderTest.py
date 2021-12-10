import urllib.request
from bs4 import BeautifulSoup
import smtplib
#伪装库
from email.mime.text import MIMEText
# modify
def askURL(url):
    head={}
    request=urllib.request.Request(url,headers=head)
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        return html
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

# html=open('xxgg.html',encoding='utf-8')
# bs=BeautifulSoup(html,'html.parser')
# ArrA=bs.select('.list-w1 a')

# 1. 先读取old.txt中的内容
# 2. 将新网页中的内容写入new.txt
# 3. 将old.txt中的内容和new.txt中的内容朱相比较
# 4. 加入idx=3,则0，1，2下表对应的节点就是新的新闻
# 5. 最后，将new.txt中的内容覆盖old.txt
oldContent = []
oldHref = []
def readOldTxt():
    # 读取旧信息
    f1 = open(r'D:\Pycharm\oneHundredThousandCodePlanning\MessageNotice\old.txt', 'r', encoding='utf-8')

    while True:
        line = f1.readline()
        if not line:
            break
        strs = line.split(' ')
        oldContent.append(strs[0])
    f1.close()

#2
newContent = []
newHref = []
def getNewInfo(url):

    html = askURL(url)
    bs = BeautifulSoup(html, 'html.parser')
    ArrA = bs.select('.list-w1 a')
    # 将新信息放入列表
    for i in range(0, len(ArrA)):
        content = ArrA[i].string
        contentHref = ArrA[i].get('href')
        contentHref="https://www.cuit.edu.cn"+contentHref[2:len(contentHref)]
        newContent.append(content)
        newHref.append(contentHref)
# 覆盖
def cover(email):
    # print("oldContent长度:"+len(oldContent))
    if len(oldContent) != 0:
        firstCon = oldContent[0]

        idx = int()
        for i in range(0, len(newContent)):
            content = newContent[i]
            if content == firstCon:
                idx = i
                break

        print("第一个下标不同的时:"+str(idx))
        #email发送
        for i in range(0, idx):
            email += "<a href="+newHref[i]+">"+newContent[i]+"</a><br>"
            # print(email+"\n")
        with open(r'D:\Pycharm\oneHundredThousandCodePlanning\MessageNotice\old.txt', 'a+', encoding='utf-8') as test:
            test.truncate(0)

    f = open(r'D:\Pycharm\oneHundredThousandCodePlanning\MessageNotice\old.txt', 'w', encoding='utf-8')
    for i in range(0, len(newContent)):
        f.write(str(newContent[i]) + " " + str(newHref[i])+"\n")
    f.close()
    return email
def send(msg):
    # 服务的设置[qq]
    # host , port
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # 登录
    server.login("1211010043@qq.com", "tajhcfimrrqfhchf")
    # 发送信息的填写
    # msg = "<a href=" + href + ">hello</a>"
    print("sendByMail函数中msg内容:" + str(msg))
    # 信息的转化
    message = MIMEText(msg, 'html', 'utf8')
    # 邮件主题
    title = "成都信息工程大学的消息更新了"
    # sender and receiver
    message["From"] = "{}".format("1211010043@qq.com")
    message["To"] = ",".join(['1211010043@qq.com'])
    # 设置主题
    message['Subject'] = title
    # 邮件的发送  sender recevier
    server.sendmail("1211010043@qq.com", "1211010043@qq.com", message.as_string())

    # quit
    server.quit()
    print("done")
url = "https://www.cuit.edu.cn/xw/xxgg.htm"
readOldTxt()
getNewInfo(url)
email=""
email=cover(email)
print("调用之前的list"+str(list))
send(email)
print("done")