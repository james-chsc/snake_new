import random

class Point:
    def __init__(self, x:int, y:int):
        "給定 x 和 y 然後產生一個點"
        self.x = x
        self.y = y


class Region:
    def __init__(self, p1:Point, p2:Point):
        "給兩個點，定義一個範圍"
        self.p1 = p1
        self.p2 = p2

    def get_rnd_point(self, beside:list=[]) -> Point:
        "產生範圍內的隨機一個座標"
        return Point( 
            random.randrange(self.p1.x, self.p2.x), 
            random.randrange(self.p1.y, self.p2.y) 
        )

class Snake:
    def __init__(self, region:Region) -> None:
        self.region = region
        self.head = region.get_rnd_point()
        self.body = [].append(self.head)
        self.score = 0

    def gen_target(self):    
        self.target = self.region.get_rnd_point(self.body)
        return self.target

    def is_eaten(self):
        return (self.head == self.target)

    def is_die(self):
        pass
        return "怎麼死的"
        
    def go(self, dir='R'):
        "往dir=(L、R、U、D)方向走一步"
        # self.head.x +=1    # self.head.x -=1
        # self.head.y +=1    # self.head.y -=1
        # if is_eaten(): self.score+=1 加分
        pass