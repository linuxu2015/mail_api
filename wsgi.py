#coding:utf-8
from flask import Flask
from flask import jsonify
from flask import request
from sendmail import send_mail
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

app = Flask(__name__)

'''@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'
    '''
status = [
    {
        'status': 200,
        'info': '发送成功'
    }
]
@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        tos = request.form.get('tos')
        content = request.form.get('content')
        subject = request.form.get('subject')
        print('content: %s' %content)
        data = content.split('\n')
       # print('################')
       # print(data)
        if data[0] == 'OK':
            alarm_status = '<b style="color:green;">%s</b>' % data[0]
        else:
            alarm_status = '<b style="color:red;">%s</b>' % data[0]
        new_content = '''
<a href=http://192.168.100.145:8081/portal/alarm-dash/case>报警面板</a>------<a href=%s>策略</a><br>
报警状态：%s<br>
报警级别：%s<br>
故障主机：%s<br>
监控项：%s<br>
标记:%s<br>
出发条件：%s<br>
备注：%s<br>
最大次数：%s<br>
当前次数：%s<br>
报警时间：%s<br>
''' % (data[9].replace('127.0.0.1','192.168.100.145'),alarm_status,data[1],data[2].split(':')[1],data[3].split(':')[1],data[4].split(':')[1],data[5],data[6].split(':')[1],data[7].split(':')[1].split(',')[0],data[7].split(':')[2],data[8].split(':')[1]+data[8].split(':')[2]+data[8].split(':')[3])
        send_mail(tos,subject,new_content)
        return jsonify({'resp':status})
    elif request.method == 'GET':
        return jsonify({'resp':status})
    else:
        return 'no data'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555,debug=True)
