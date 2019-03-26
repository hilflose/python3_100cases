#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
#将每一对因子加进集合，在这个过程中已经自动去重。最后的结果要求不计算其本身。
def factor(num):
    target=int(num)
    res=set()#集合去重
    for i in range(1,num):
        if num%i==0:
            res.add(i)#加进集合
            res.add(num/i)#加入另一个因子
    return res

for i in range(2,1001):
    if i==sum(factor(i))-i:#减去了一个本身
        print(i)
