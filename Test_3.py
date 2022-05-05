pwd = 'a123456'
i = 3
while i > 0:
    password = input('请输入密码：')
    if password == pwd:
        print('登录成功！')
        break
    else:
        i = i - 1
        if i>0:
            print('密码错误，还有', i, '次机会')
        else:
            print('密码错误!')

