#coding:utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))
def send_mail(tos,subject,content):
    user = 'xulibao@aioute.com'
    password = '1qaz2wsx'
    #from_addr = '11111@qq.com'
    smtp_server = 'smtp.aioute.com'
    #to_addr = '371044414@qq.com'
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
#send_mail('371044414@qq.com','hahahahahah','dd')
#
