import random

r = random.randint(1, 100)
while True:
    num = input('请猜数字：')
    num = int(num)
    if num==r:
        print('猜中了！')
        break
    elif num>r:
        print('大了！')
    elif num<r:
        print('小了！')
