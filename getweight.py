from flask import Flask, request
import flask
import json
import random
import serial

app = Flask(__name__)

from wsgiref.simple_server import make_server


# 只接受get方法访问
@app.route("/dibang", methods=["GET"])
def check():
    # 默认返回内容
    return_dict = {'return_code': '500', 'return_info': '处理失败', 'result': False}
    # 判断入参是否为空
    com = flask.request.values.get('com')
    bsp = flask.request.values.get('bsp')

    if com and bsp:
        return_dict['result'] = True
        # 对参数进行操作,并将结果返回
        return_dict['result'] = getdata(com, bsp)
        return_dict['return_info'] = '处理成功'
        return_dict['return_code'] = '200'
        return json.dumps(return_dict, ensure_ascii=False)
    else:
        return json.dumps(return_dict, ensure_ascii=False)


# 功能函数
def getdata(com, bsp):  # 发送函数
    try:
        # return_dict = {'return_code':'200','return_info':'获取重量','result':False}

        # if requests.args is None:
        #     return_dict['return_code'] = '5004'
        #     return_dict['return_info'] = '请求参数为空'
        #     return json.dumps(return_dict,ensure_ascii = False)
        #
        # get_data = requests.args.to_dict()
        # com = get_data.get('com')
        # bsp =
        print(com, bsp)
        print('com,bsp', com, bsp)
        '''    connect serial'''
        # x = serial.Serial(com, bsp)  # 这是我的串口，测试连接成功，没毛病

        '''    connect dibang   握手'''
        # myinput = bytes('02','41','41','30','30','03')
        # x.write(myinput)

        '''    read from dibang '''
        # myout = x.read(6)  # 读取串口传过来的字节流，这里我根据文档只接收7个字节的数据
        # print('myout',myout)

        """read data maozhong"""
        # myinput = ('02','41','42','30','33','03')
        # x.write(myinput)

        """myout=x.read(7)#读取串口传过来的字节流，这里我根据文档只接收7个字节的数据
        datas =''.join(map(lambda x:('/x' if len(hex(x))>=4 else '/x0')+hex(x)[2:],myout))#将数据转成十六进制的形式
        new_datas = datas.split("/x")#将字符串分割，拼接下标4和5部分的数据
        need = new_datas[4]+new_datas[5];#need是拼接出来的数据，比如：001a
        my_need = int(hex(int(need,16)),16)#将十六进制转化为十进制
        my_need = my_need/10
        print('weight',my_need)"""

        # 生成随机数，浮点类型
        x1 = random.uniform(401, 699)
        # 控制随机数的精度round(数值，精度)

        print(x1)
    except Exception as e:
        print(e)

    return x1


# 默认返回内容
return_dict = {'return_code': '500', 'return_info': '处理失败', 'r1': False, 'r2': False}


# 只接受get方法访问
@app.route("/dianziweilan", methods=["GET"])
def checkin():
    # 判断入参是否为空
    com = flask.request.values.get('com')
    bsp = flask.request.values.get('bsp')
    if com and bsp:
        # 对参数进行操作
        print(com, bsp)
        return_dict['return_code'] = '200'
        return_dict['return_info'] = '处理成功'
        return_dict['r1'], return_dict['r2'] = dianziweilan(com, bsp)
        return json.dumps(return_dict, ensure_ascii=False)

    else:
        return_dict['return_info'] = '参数为空'
        return json.dumps(return_dict, ensure_ascii=False)


# 获取电子围栏寄存器状态
def dianziweilan(com, bsp):
    r1 = False
    r2 = False

    try:
        try:
            '''    connect serial'''
            x = serial.Serial(com, bsp,timeout=0.3)  # 这是我的串口，测试连接成功，没毛病
        except Exception as e:
            print(e)
            return_dict['return_info'] = '串口链接超时'
        '''    connect dibang   握手'''
        myinput = bytes([0xFE, 0x02, 0x00, 0x00, 0x00, 0x04, 0x6D, 0xC6])
        x.write(myinput)

        '''    read from dianziweilan '''
        myout = x.read(6)  # 读取串口传过来的字节流，这里我根据文档只接收7个字节的数据

        if len(myout) < 6:
            return_dict['return_info'] = '串口未拿到返回值'

        datas = ''.join(map(lambda x: ('/x' if len(hex(x)) >= 4 else '/x0') + hex(x)[2:], myout))  # 将数据转成十六进制的形式

        new_datas = datas.split("/x")  # 将字符串分割，拼接下标4和5部分的数据

        '''     chuli '''
        status = new_datas[4]
        print(status)
        if status == '01':
            r1 = True
        if status == '03':
            r2 = True
            r1 = True
        if status == '02':
            r2 = True
    except Exception as e:
        print(e)

    # my_need = int(hex(int(need,16)),16)#将十六进制转化为十进制
    # my_need = my_need/10
    # print('weight',my_need)

    print(r1, r2)
    return r1, r2


if __name__ == "__main__":
    server = make_server('', 5000, app)
    server.serve_forever()
    # app.run(host='0.0.0.0', port=5000, debug=True)
