num = 7
guess = 0

print("猜数字游戏:")

while guess != num:
    guess = int(input('输入你猜测的数字'))
    if guess == num:
        print("恭喜,猜对了")
    elif guess < num:
        print("猜测的数字小了..")
    elif guess > num:
        print("大了..了..")
