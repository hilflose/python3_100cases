def draw(num):
    a="*"*(2*(4-num)+1)
    print(a.center(9,' '))
    #center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
    if num!=1:
        draw(num-1)#此处递归
        print(a.center(9,' '))
draw(4)
