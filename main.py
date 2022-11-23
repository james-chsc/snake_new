import random
# import pygame


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Region:
    def __init__(self, p1:tuple, p2:tuple) -> None:
        self.p1 = p1
        self.p2 = p2
        self.xx = (p1[0], p2[0])
        self.yy = (p1[1], p2[1])
    
    def get_rnd_point(self) -> Point:
        return Point( 
            random.randrange(*self.xx), 
            random.randrange(*self.yy) 
        )

class Snake:
    
    def __init__(self) -> None:
        
        self.region = {
            'p1': Point(0, 0), 
            'p2': Point(100, 100)
        }
        self.head = Point(0, 0)
        self.target = Point(0, 0)
        self.body = []