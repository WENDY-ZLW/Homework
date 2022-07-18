#This python file uses the following encoding:utf-8

from collections import deque

total_num = int(input("> The total number is: "))
k = int(input("> The target number is: "))

def surviver(total_num,k):
    
    lucky_one = deque(range(1,total_num+1))   #总共有n个人参与
    
    while len(lucky_one) > 1:
    
        lucky_one.rotate(-(k-1))  #将左边元素放入右边，即左移k-1次，到第k个人 ； .rotate(1)默认将末尾放入左边
        lucky_one.popleft()       #删除最左端的第k个元素
    
    return lucky_one[0]  
    

print( "So the last one is: " , surviver (total_num,k))

class Person:
    def __init__(self, name, id, gender, age) -> None:
        self.name = name
        self.id = id
        self.gender = gender
        self._age = age

    def guess_age(self, age):
        if age > self._age:
            return 1
        elif age < self._age:
            return -1
        else:
            return 0

class JosephusRing:
    def __init__(self, members = []) -> None:
        self._members = members

    def add_member(self, obj: Person):
        self._members.append(obj)

    def traverse(self, start_pos = 0):
        # 遍历环
        out_order = []
        return out_order

classA = JosephusRing()
mary = Person("Mary Clin", 2014231231, "F", 18)
mary._age
classA.add_member(mary)
classA

classA.add_member("John")
classA.traverse()
classA.traverse(start_pos = 3)
classA._members


classB = JosephusRing()
classB.traverse()
classB._members
