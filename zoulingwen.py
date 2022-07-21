from collections import deque
import Homework.Name_list

class Person:
    def __init__(self, name) -> None:
        self.name = name       

class Count_Games:
    
    def __init__ (self,members =[]):  #产生一个空的容器
        self.members = members  #在list前面加两个下划线__，在python类的私有属性前面加__
    
    def push(self,obj: Person)->str:  #入栈：以item和self作为参数
        self.members.append(obj)
    
    def pop(self):        #出栈:删除并返回最左边元素    
        return self.members.pop(0)
    
    def size(self) -> int:       #返回栈中元素个数
        return len(self.members)


    def traverse_josephus(self,start_id=0,offset=0):

        while josephus.size() > 1 :
            
            self.members.rotate(-start_id)    #寻找初始位置
            self.members.rotate(-(offset-1))  #将左边元素放入右边，即左移k-1次，到第k个人 ； .rotate(1)默认将末尾放入左边
            self.members.pop()

        return self.members[0] 


if __name__ == '__main__':
    
       
    josephus = Count_Games()

    mary = Person("Mary Clin")
    
    josephus.push(mary)
    
    Count_Games().traverse_josephus()  #定义在自定义类中的方法需要一个默认的self参数。错误提示没有self 就是说明这个类的对象没有创建成功.所以在定义的类后面加（）

    print(Count_Games.traverse_josephus)
            
