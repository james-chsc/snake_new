from typing import List, Union
import random


class Point:
    def __init__(self, x:int, y:int) -> None:
        """
        給定 x 和 y 然後產生一個點
        """
        self.x = x
        self.y = y


class Region:
    def __init__(self, p1:Point, p2:Point) -> None:
        """
        給兩個點，定義一個矩形範圍
        """
        self.p1 = p1
        self.p2 = p2

    def get_rnd_point(self, except_points:List[Point]=[]) -> Point:
        """
        產生範圍內的隨機一個「點」
        除了except_points(list of Point)之外
        """
        return Point( 
            random.randrange(self.p1.x, self.p2.x), 
            random.randrange(self.p1.y, self.p2.y) 
        )


class Snake:
    def __init__(self, region:Region, head:Union[Point, None]=None) -> None:
        """
        傳入一個蛇活動的「範圍」及蛇頭的「點」\n
        建立一隻貪食蛇
        """
        self.region = region
        if head is None: head = Point(
            (region.p1.x + region.p2.x) // 2,
            (region.p1.y + region.p2.y) // 2                
        )
        self.head = head
        self.body = [self.head,]
        self.score = 0

    def new_target(self) -> Point:
        """
        """
        self.target = self.region.get_rnd_point(self.body)
        return self.target

    def is_eaten(self):
        """
        """
        return (self.head == self.target)

    def is_die(self):
        """
        """
        pass # 怎麼死的
        return False
        
    def go(self, dir:str ='R'):
        """
        往(dir=L、R、U、D)方向走一步
        """
        # self.head.x +=1    # self.head.x -=1
        # self.head.y +=1    # self.head.y -=1
        # if is_eaten(): self.score+=1 加分
        pass
