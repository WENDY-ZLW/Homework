from collections import deque

total_num = int(input("> The total number is: "))
offset = int(input("> The target number is: "))
lucky_one = deque(range(1,total_num+1))   #总共有n个人参与

def survivor(total_num,offset):
  
    while len(lucky_one) > 1:
    
        lucky_one.rotate(-(offset-1))  #将左边元素放入右边，即左移k-1次，到第k个人 ； .rotate(1)默认将末尾放入左边
        lucky_one.popleft()       #删除最左端的第k个元素
    
    return lucky_one[0] 

print ('So the last one is:' , survivor(total_num,offset))