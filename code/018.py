#复读机相加求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a=input('被加数字：')
n=int(input('几个相加：'))
res=0
for i in range(n):
    res+=int(a)
    a+=a[0]
    print(res)
    print(a)

print('结果是：',res)
