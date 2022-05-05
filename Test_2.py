country = input('请问你是那个国家？')
age = input('请输入您的年龄：')
age = int(age)
if country == '台湾':
    if age >= 18:
        print('您可以考驾照')
    else:
        print('你还不能考驾照！')
