from typing import List, Tuple
import random


class Point(object):
    """
    一個點的類別(Class)
    """
    def __init__(self, x:int, y:int) -> None:
        """
        給定 x 和 y 然後產生一個點
        """
        self.x = x
        self.y = y


class Region:
    """
    一個範圍的Class(類別)
    """
    def __init__(self, p1:Point, p2:Point) -> None:
        """
        給兩個點，定義一個矩形範圍
        """
        self.p1 = p1
        self.p2 = p2

    def rnd_point(self, except_points:List[Point] = []) -> Point:
        """
        產生範圍內的隨機一個「點」
        除了except_points(list of Point)之外
        """
        while True:
            pt = Point( 
                random.randrange(self.p1.x, self.p2.x), 
                random.randrange(self.p1.y, self.p2.y) 
            )
            if not (pt in except_points): break     # 新點座標不是排除名單之外就行了
        return pt

    def is_in_region(self, pt: Point) -> bool:
        """
        傳入一個點pt，判斷該點是不是在範圍(region)內
        """
        if (self.p1.x <= pt.x <= self.p2.x and
            self.p1.y <= pt.y <= self.p2.y):
            return True
        else:
            return False

class Snake:
    """
    一個貪食蛇Class(類別)
    """
    def __init__(self, region: Region) -> None:
        """
        建立一隻貪食蛇instanc(實體(例))
        傳入一個蛇活動的「範圍」
        初始化這實例(self)相關的屬性變數
        """
        self.region = region
        self.head = Point(  # 預設蛇頭位置在活動範圍的中央
            (region.p1.x + region.p2.x) // 2,
            (region.p1.y + region.p2.y) // 2                
        )
        self.body = [self.head]
        self.food = self.new_food()
        self.score = 0
        self.dir_ = None

    def new_food(self) -> Point:
        """
        在活動範圍(region)內，新增一個食物
        而且避免食物出現在蛇的身體上
        """
        self.food = self.region.rnd_point(except_points = self.body)
        return self.food

    def is_eaten(self) -> bool:
        """
        判斷是否有吃到食物
        """
        return self.head == self.food

    def is_died(self) -> bool:
        """
        判斷是否死掉
        1.碰到四周牆壁
        2.吃到自己身體
        """
        if (self.head in self.body[1:] and 
            self.region.is_in_region(self.head)):
            return True
        else:
            return False
        
    def go(self, dir_: str = '右') -> None:
        """
        往目前方向(dir=左、右、上、下)走一步
        """
        # 不能回轉
        if ((self.dir_ in "左右" and dir_ in "左右") or 
            (self.dir_ in "上下" and dir_ in "上下")):
            return

        else:   #可以轉彎
            self.dir_ = dir_

        if   dir_ == '左': self.head.x +=1
        elif dir_ == '左': self.head.x -=1
        elif dir_ == '上': self.head.y -=1
        else:              self.head.y +=1  # dir_ == '下'
