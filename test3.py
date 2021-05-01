import serial
from icecream import ic
return_dict = {'return_code': '500', 'return_info': '处理失败', 'result': False}
# 功能函数
def getdata(com, bsp):  # 发送函数
    
    try:


        '''    connect serial'''
        try:
            '''    connect serial'''
            x = serial.Serial(com, bsp,timeout=0.3)  # 这是我的串口，测试连接成功，没毛病
        except Exception as e:
            print(e)
            return_dict['return_info'] = '串口链接超时'
            #return 

        myinput = bytes([0x02,0x41,0x42,0x30,0x33,0x03])
        #print(myinput[2:5])
        print(myinput)
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


        #ic(new_datas[12])
        nums = nums +'.' + str(bytes.fromhex(new_datas[11]), encoding='utf-8')
        #ic(nums)
        nums = float(nums)
        #ic(nums)
        return nums
    except Exception as e:
        print(e)

getdata('com4',2400)