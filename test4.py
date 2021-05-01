from icecream import ic
datas = '/x02/x41/x42/x2b/x30/x30/x30/x30/x30/x30/x30/x31/x38/x03'
new_datas = datas.split("/x")#将字符串分割，拼接下标4和5部分的数据
# num2 = new_datas[6]
# num3 = new_datas[7]
# bytenum2 = bytes.fromhex(num2)
# print(bytenum2)
# intnum2 = str(bytenum2, encoding='utf-8')
# ic(intnum2)


#拼接整数位
nums = ''
for num in new_datas[5:10]:
	nums += str(bytes.fromhex(num), encoding='utf-8')

ic(nums)
#拼接小数位
nums = nums +'.' + str(bytes.fromhex(new_datas[11]), encoding='utf-8')
ic(nums)
nums = float(nums)
ic(nums)
# num1 = '0x'+new_datas[5]
# print(num1)
# print(type(int(num1)))
# #print(chr(int(num1)))
# print(chr(num1))
# #print(chr(new_datas[5]))

        """myout=x.read(7)#读取串口传过来的字节流，这里我根据文档只接收7个字节的数据
        datas =''.join(map(lambda x:('/x' if len(hex(x))>=4 else '/x0')+hex(x)[2:],myout))#将数据转成十六进制的形式
        new_datas = datas.split("/x")#将字符串分割，拼接下标4和5部分的数据
        need = new_datas[4]+new_datas[5];#need是拼接出来的数据，比如：001a
        my_need = int(hex(int(need,16)),16)#将十六进制转化为十进制
        my_need = my_need/10
        print('weight',my_need)"""
