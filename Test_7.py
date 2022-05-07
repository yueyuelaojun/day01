data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
print('档案读取完成，共有', len(data), '笔资料！')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('平均留言长度为：', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '笔留言长度小于100')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '笔记录提到GOOD!')

good_1 = [d for d in data if 'good' in d]
print('一共有', len(good_1), '笔记录提到GOOD!')

bad = ['bad' in d for d in data]
print(bad)
#正规的写法
#bad = []
#for d in data:
#    bad.append('bad' in d)
