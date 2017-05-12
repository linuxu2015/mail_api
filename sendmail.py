#coding:utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def send_mail(tos,subject,content):
    user = ''
    password = ''
    smtp_server = ''
    #from_addr邮件列表显示标题
    #subject 邮件标题
    #to_addr 接受者

    msg = MIMEText('%s' %content, 'html', 'utf-8')
    msg['From'] = (u'falcon报警')
    msg['To'] = (u'%s' % tos)
    msg['Subject'] = subject

    server = smtplib.SMTP(smtp_server, 25)
    #server.set_debuglevel(1)
    server.login(user, password)
    server.sendmail(user, [tos], msg.as_string())
    server.quit()
