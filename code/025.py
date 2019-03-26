#求1+2!+3!+...+20!的和。
#1+2!+3!+...+20!=1+2(1+3(1+4(...20(1))))
res=1
for i in range(20,1,-1):
    print(i)
    res=i*res+1
    print(res)
print(res)
