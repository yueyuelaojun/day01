# Rang是清单产生器
import random

for i in range(100):
    r = random.randint(1, 1000)
    print('这是第', i + 1, '个', r)
    
range(5)  # [0,1,2,3,4]
range(3)  # [0,1,2]
range(2, 5)  # [2,3,4]
range(8, 10)  # [8,9]
range(2, 10, 3)  # [2,5,8]
range(3, 8, 2)  # [3,5,7]
range(10, 3, -2)  # [10,8,6,4]
