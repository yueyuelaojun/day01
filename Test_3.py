i = 3
while True:
    password = input('请输入密码：')
    if password == 'a123456':
        print('登录成功！')
        break
    else:
        i = i - 1
        print('密码错误，还有', i, '次机会')
