import os
import cv2
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart  # 构建邮箱的格式
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage
from email.mime.image import MIMEImage

# 开启摄像头拍照
# 摄像头从0开始数，数字代表第几个摄像头
sxt = cv2.VideoCapture(0)

# 读取照片
_, zp = sxt.read()
# 保存图片
cv2.imwrite('image.jpg', zp)
# 关闭摄像头
sxt.release()

# 选择邮箱
email_protocol = 'smtp.126.com'  # QQ邮箱的传输协议
email_user = 'yzsxsunhj@126.com'  # 账号
email_shouquanma = 'HZBVGHDKYWLQQMTD'  # 使用授权码，而不是密码

# 创建发送内容
my_email = MIMEMultipart()
my_email['Subject'] = '照片'
my_email['To'] = email_user
my_email['Form'] = email_user

html = """
<html><body><img src="cid:imagel" alt="imagel" align="center" width="100%"></body>
</html>
"""
# 原理：https://blog.csdn.net/shenshibaoma/article/details/76148118
my_email.attach(MIMEText(html, _subtype='html', _charset='utf8'))
image = MIMEImage(open('image.jpg', 'rb').read(), _subtype='octet-stream')
image.add_header('Content-ID', 'imagel')
my_email.attach(image)

# 发送邮件
# 连接服务器
server = SMTP_SSL(email_protocol)
# 登录
server.login(email_user, email_shouquanma)
# 发送邮件
server.sendmail(email_user,email_user,my_email.as_string())
# 退出
server.quit()

# 删除照片
os.remove('image.jpg')
