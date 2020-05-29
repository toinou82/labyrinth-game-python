





class Player:
    """Labyrinth Class, it features the generation and the management of cells"""

    def __init__(self, isBear:bool):
        self.positionI=0
        self.positionJ=0
        self.HaveTreasure=False
        self.isBear= isBear
        self.life=2
        


    def get_positionI(self):
        return self.positionI


    def set_positionI(self,pos):
        self.positionI=pos

    def get_positionJ(self):
        return self.positionJ


    def set_positionJ(self,pos):
        self.positionJ=pos

    def get_HaveTreasure(self):
        return self.HaveTreasure


    def set_positionJ(self,b):
        self._HaveTreasure=b

     

    