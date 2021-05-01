from flask import Flask, request
import flask
import json
import random
import serial
from icecream import ic
com = 'com4'
bsp = 2400
print('com,bsp', com, bsp)
'''    connect serial'''
try:
    x = serial.Serial(com, bsp) 
except Exception as e:
	print(e) 

myinput = bytes([0x02,0x41,0x42,0x30,0x33,0x03])
#print(myinput[2:5])
x.write(myinput)

data = x.read(14)
datas =''.join(map(lambda x:('/x' if len(hex(x))>=4 else '/x0')+hex(x)[2:],data))#将数据转成十六进制的形式
#datas =''.join(map(lambda x:('0x' if len(hex(x))>=4 else '0x0')+hex(x)[2:],data))#将数据转成十六进制的形式

print(datas)
#datas = '/x02/x41/x42/x2b/x30/x30/x30/x30/x30/x30/x30/x31/x38/x03'
new_datas = datas.split("/x")#将字符串分割，拼接下标4和5部分的数据

#拼接整数位
nums = ''
for num in new_datas[5:11]:
        ic(num)
        nums += str(bytes.fromhex(num), encoding='utf-8')

ic(nums)
#拼接小数位a
ic(new_datas[12])
nums = nums +'.' + str(bytes.fromhex(new_datas[11]), encoding='utf-8')
ic(nums)
nums = float(nums)
ic(nums)