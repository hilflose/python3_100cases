#暂停一秒输出，并格式化当前时间。
import time

for i in range(4):
    # 把struct_time转换为format_time
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))#直接生成时间元组
    # 直接生成format_time
    print(time.strftime('%Y-%m-%d %X'))
    time.sleep(1)
