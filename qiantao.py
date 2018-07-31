# if 嵌套
num = int(input("输入一个数字: "))

if num%2==0:
    if num%3==0:
        print("输入的数字可以同时被2和3整除")
    else:
        print("可以被2整除,但是不能被3整除")
else:
    if num%3 == 0:
        print('可以被3整除,但是不能被2整除')
    else:
        print("不能被2和3整除")