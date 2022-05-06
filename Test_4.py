import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input('请猜数字：')
    num = int(num)
    if num == r:
        print('猜中了！')
        print('这是你猜的第', count, '次')
        break
    elif num > r:
        print('大了！')
    elif num < r:
        print('小了！')
    print('这是你猜的第', count, '次')
