import requests
from urllib.request import urlopen   #python3中要加'urllib.requests'
import random

Name_URL = "http://learncodethehardway.org/words.txt"
Name_players=[]

try: 
    Name = requests.get(Name_URL)
    print (Name.status_code)  #返回网页状态 = 200 为正常访问

    Name.raise_for_status()
    Name.encoding=Name.apparent_encoding  #r.encoding = r.apparent_encoding,来直接获取网页的编码。
   

except:
    print("失败！")


class Name_List:

    def __init__(self)->None:  #load up the name from the website
        global Name_players
        Name_players = (Name.text).split('\n')    

    def random_name(self):
        return random.randint(0,len(self.Name_players)-1)


if __name__ == '__main__':
    Name_List()
    print(Name_players)