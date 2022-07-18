from collections import deque

class Person:
    def __init__(self, name, id, gender, age) -> None:
        self.name = name
        self.id = id
        self.gender = gender
        self._age = age

class Count_Games():
    
    def __init__ (self,members =[]):  #产生一个空的容器
        self._members = members  #在list前面加两个下划线__，在python类的私有属性前面加__
    
    def push(self,obj: Person)->str:  #入栈：以item和self作为参数
        self._members.append(obj)
    
    def pop(self):        #出栈:删除并返回最左边元素    
        return self.members.pop(0)
    
    def size(self) -> int:       #返回栈中元素个数
        return len(self._members)


    def traverse_josephus(self,start_id = 0,offset=0):

        while josephus.size > 1 :
            self.members.rotate(-start_id)    #寻找初始位置
            self.members.rotate(-(offset-1))  #将左边元素放入右边，即左移k-1次，到第k个人 ； .rotate(1)默认将末尾放入左边
            self.members.pop()
        return self.members[0] 
      

if __name__ == '__main__':

        
    josephus = Count_Games()
    

    mary = Person("Mary Clin", 2014231231, "F", 18)

    josephus.push(mary)
    
    
    Count_Games.traverse_josephus()

    print('The last one is:' ,  Count_Games.traverse_josephus)
            
