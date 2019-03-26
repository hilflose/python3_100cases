#输出指定格式的日期。
import datetime
print(datetime.date.today())
print(datetime.date(2333,2,3))
print(datetime.date.today().strftime('%d/%m/%Y'))
day=datetime.date(1111,2,3)
day=day.replace(year=day.year+22)
print(day)





from datetime import datetime
now=datetime.now()
print('当前时间：',now)
utcnow=datetime.utcnow()
print('世界标准时间：',utcnow)
dt=datetime(2019, 5, 23, 12, 20)
print('指定日期：',dt)