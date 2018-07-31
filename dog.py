age = int(input("输入狗狗的年龄:"))
print("")
if age<0:
    print("你在逗我吧~")
elif age == 1:
    print("相当于人类14岁")
elif age >2:
    human = 22 + (age-2)*5
    print("对应人类年龄:",human)

input("\n\n回车退出")