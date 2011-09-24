from elements import Element
from block import Block
from player import Player
from terrain import Terrain
from Level import Level
from monster import Monster
from Goal import Goal
from GoalBlock import GoalBlock
from Spike import Spike

class TutLevel(Level):
    def __init__(self, width, height):
        super(TutLevel, self).__init__(width, height)
        ##initialize blocks##
        boxtop = Terrain(20, -19, 40, 2, 0, 0,100, self, 0.5)
        boxleft= Terrain(-1,-5,2,30,0,0,100,self,0.5)
        boxbottom= Terrain(20,9,40,2,0,0,100,self,0.5)
        boxright= Terrain(41,-5,2,30,0,0,100,self,0.5)
        mon= Monster(4,5,1,2,0,0,1,self,.5,3,0)

        goal= Goal(38,5,1,5,0,0,100,self,0.5)
        
        
        b =   Block(20, 5,  2, 2, 0, 0,  1, self, 0.5)
        c =  Player(15, 5,  1, 2, 0, 0,  1, self, 0.5)
        d =   Block(27, 5, 2, 2, 0, 5,  2, self, 0.5)  
        a =   GoalBlock(17, 5, 2, 2, 0, 5,  2, self, 0.5)  
        e = Spike(20, 8, 1, 1, 0, 0, 100, self, 0.5)
        self.add_elem(c)
        self.add_elem(b)
        self.add_elem(a)
        self.add_elem(d)
        self.add_elem(e)
        self.add_elem(boxtop)
        self.add_elem(boxright)
        self.add_elem(boxbottom)
        self.add_elem(boxleft)
        self.add_elem(mon)
        self.add_elem(goal)
