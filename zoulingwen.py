#This python file uses the following encoding:utf-8
#约瑟夫环问题：已知n个人（以编号1，2，3…n分别表示）围坐在一张圆桌周围。
#从编号为k的人开始报数，数到k的那个人被杀掉；他的下一个人又从1开始报数，数到k的那个人又被杀掉；依此规律重复下去，直到圆桌周围的人只剩最后一个。

from collections import deque

total_num = int(raw_input("> The total number is: "))
k = int(raw_input("> The target number is: "))

def surviver(total_num,k):
    
    lucky_one = deque(range(1,total_num+1))   #总共有n个人参与
    
    while len(lucky_one) > 1:
    
        lucky_one.rotate(-(k-1))  #循环左移k-1次，即到第k个人
        lucky_one.popleft()       #删除最左端的第k个元素
    
    return lucky_one[0]  
    

print "So the last one is: " , surviver (total_num,k)