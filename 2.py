from collections import deque

total_num=int(input("The total number:"))
interval=int(input("The step:"))
start=int(input("Which person to start:"))


def init_loop(total_num):
    global players  
    players = deque(range(1,total_num+1))
    return players

def traverse_loop(players,interval,start):
    global order
    players.rotate(-(start))
    order=[]
    while len(players)>0:
        players.rotate(-(interval-1))
        order.append(players[0])
        players.popleft()

    return order

init_loop(total_num)
traverse_loop(players,interval,start)
 
print("The order：%s"%order[0:total_num-1])
print("The final survivor：%s"%order[total_num-1])













