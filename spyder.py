import smtplib
#伪装库
from email.mime.text import MIMEText
def sendMailBySMTP(msg):
    # 服务的设置[qq]
    # host , port
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # 登录
    server.login("1211010043@qq.com", "tajhcfimrrqfhchf")
    # 发送信息的填写
    # msg = "<a href=" + href + ">hello</a>"
    print("sendByMail函数中msg内容:"+str(msg))
    # 信息的转化
    message = MIMEText(msg, 'html', 'utf8')
    # 邮件主题
    title = "成都信息工程大学的消息更新了"
    # sender and receiver
    message["From"] = "{}".format("1211010043@qq.com")
    message["To"] = ",".join(['629006787@qq.com'])
    # 设置主题
    message['Subject'] = title
    # 邮件的发送  sender recevier
    server.sendmail("1211010043@qq.com", "629006787@qq.com", message.as_string())

    # quit
    server.quit()
    print("done")
