from random import randint

from impl.labyrinth.CellType import CellType
from impl.labyrinth.cells.CellEmpty import CellEmpty
from impl.labyrinth.cells.CellMonolith import CellMonolith
from impl.labyrinth.cells.CellNoWall import CellNoWall
from impl.labyrinth.cells.CellStart import CellStart
from impl.labyrinth.cells.CellTreasure import CellTreasure
from impl.labyrinth.cells.CellWall import CellWall
from impl.labyrinth.cells.CellWormhole import CellWormhole
from impl.labyrinth.cells.CellRiver import CellRiver
from impl.labyrinth.Player import Player


class Labyrinth:
    """Labyrinth Class, it features the generation and the management of cells"""

    def __init__(self, size: int):
        self.__size = size
        self.__labyrinth = []
        self.__exit_i=0
        self.__exit_j=0
        self.Player=Player(False)
        self.Bear=Player(True)


    def get_labyrinth(self):
        return self.__labyrinth

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def set_labyrinth(self, labyrinth):
        self.__labyrinth = labyrinth

    def get_exit_i(self):
        return self.__exit_i

    def set_exit_i(self,exit):
        self.__exit_i=exit

    def get_exit_j(self):
        return self.__exit_j

    def set_exit_j(self,exit):
        self.__exit_j=exit



    def define_exit(self):
        """ Generate a random location for the exit"""
        exit_i = randint(1, self.__size) * 2 -1
        exit_j = randint(1, self.__size) * 2 -1
        p=randint(0,3)
        if p == 0:
            exit_i=0
        if p == 1:
            exit_i=self.__size * 2
        if p == 2:
            exit_j=0
        if p == 3:
            exit_j=self.__size * 2
            
        self.__exit_i=exit_i
        self.__exit_j=exit_j


    def generate_labyrinth(self):
        for i in range(self.__size*2+1):
            row=[]
            for j in range(self.__size*2+1):
                row.append(CellEmpty())
            self.__labyrinth.append(row)
        for i in range(self.__size*2+1):
            for j in range(self.__size*2+1):
                if ((i==0)or(j==0)or(i==self.__size*2)or(j==self.__size*2))and((i!=self.__exit_i)or(j!=self.__exit_j)):
                    self.__labyrinth[i][j]=CellMonolith()
        for i in range(1,self.__size*2):
            for j in range(1,self.__size*2):
                if ((i%2==0)or(j%2==0)):
                    if randint(0,20)<3:
                        self.__labyrinth[i][j]=CellWall()
                    else:
                        self.__labyrinth[i][j]=CellNoWall()

        i=randint(1,self.__size//2+1)*2-1
        j=randint(1,self.__size)*2-1               
        self.__labyrinth[i][j]=CellRiver(1,self.__size//2)
        for n in range(1,self.__size//2):
            self.__labyrinth[i+2*n-1][j]=CellRiver(0,self.__size//2)
            self.__labyrinth[i+2*n][j]=CellRiver(n+1,self.__size//2)

        a=0
        while(a==0):
            i=randint(1,self.__size)*2-1
            j=randint(1,self.__size)*2-1
            typeCell=self.__labyrinth[i][j].get_cell_type()
            if (typeCell!=CellType.RIVER):
                self.__labyrinth[i][j]=CellTreasure()
                a=1

        a=0
        while(a==0):
            i=randint(1,self.__size)*2-1
            j=randint(1,self.__size)*2-1
            typeCell=self.__labyrinth[i][j].get_cell_type()
            if ((typeCell!=CellType.RIVER)and(typeCell!=CellType.TREASURE)):
                self.__labyrinth[i][j]=CellStart()
                self.Player.positionI=i
                self.Player.positionJ=j
                a=1

        a=0
        while(a==0):
            i=randint(1,self.__size)*2-1
            j=randint(1,self.__size)*2-1
            typeCell=self.__labyrinth[i][j].get_cell_type()
            if ((typeCell!=CellType.RIVER)and(typeCell!=CellType.TREASURE)and(typeCell!=CellType.RIVER)):
                self.Bear.positionI=i
                self.Bear.positionJ=j
                print(str(self.Bear.positionI)+"  "+str(self.Bear.positionJ))
                a=1



        acc=0
        while(acc<=4):
            i=randint(1,self.__size)*2-1
            j=randint(1,self.__size)*2-1
            typeCell=self.__labyrinth[i][j].get_cell_type()
            if (typeCell!=CellType.TREASURE)and(typeCell!=CellType.STARTING_CELL)and(typeCell!=CellType.WORMHOLE)and(typeCell!=CellType.RIVER):
                self.__labyrinth[i][j]=CellWormhole(acc,5)
                acc+=1


    




    def goToNextWormhole(self,wormhole):
        for i in range(1,self.__size*2):
            for j in range(1,self.__size*2):
                if self.__labyrinth[i][j].get_cell_type()==CellType.WORMHOLE:
                    if self.__labyrinth[i][j].get_number()==((wormhole.get_number()+1)%5):
                        self.Player.positionI=i
                        self.Player.positionJ=j

    def inTheRiver(self,Pi,Pj):
        if self.__labyrinth[Pi+1][Pj].get_cell_type()==CellType.RIVER:
            self.Player.positionI=Pi+2
            self.Player.positionJ=Pj
            if self.__labyrinth[self.Player.positionI][self.Player.positionJ].get_number()==self.__size//2:
                print("End of the River")
            else:
                print("In the river!!")
        else:
            print("End of the River")

    def moveBear(self):
        v=randint(1,4)
        if v==1:
            self.bearRight()
            print("d")
        if v==2:
            self.bearLeft()
            print("g")
        if v==3:
            self.bearUp()
            print("h")
        if v==4:
            self.bearDown()
            print("b")

        


    def bearRight(self):    
        currentCell=self.__labyrinth[self.Bear.positionI][self.Bear.positionJ+1].get_cell_type()
        if ((currentCell!=CellType.WALL)and(currentCell!=CellType.MONOLITH)and(currentCell!=CellType.EMPTY)):
            if((self.Player.positionI==self.Bear.positionI)and(self.Player.positionJ==self.Bear.positionJ+2)):
                self.Player.life-=1
                print("Player damaged")
            self.Bear.positionJ+=2     
               
            followingCell=self.__labyrinth[self.Bear.positionI][self.Bear.positionJ].get_cell_type()
            if (followingCell==CellType.WORMHOLE):
                self.bearWormhole(self.__labyrinth[self.Bear.positionI][self.Bear.positionJ])
            if (followingCell==CellType.RIVER):
                self.bearInTheRiver(self.Bear.positionI,self.Bear.positionJ)

    def bearLeft(self):    
        currentCell=self.__labyrinth[self.Bear.positionI][self.Bear.positionJ-1].get_cell_type()
        if ((currentCell!=CellType.WALL)and(currentCell!=CellType.MONOLITH)and(currentCell!=CellType.EMPTY)):
            if((self.Player.positionI==self.Bear.positionI)and(self.Player.positionJ==self.Bear.positionJ-2)):
                self.Player.life-=1
                print("Player damaged")
            self.Bear.positionJ-=2     
               
            followingCell=self.__labyrinth[self.Bear.positionI][self.Bear.positionJ].get_cell_type()
            if (followingCell==CellType.WORMHOLE):
                self.bearWormhole(self.__labyrinth[self.Bear.positionI][self.Bear.positionJ])
            if (followingCell==CellType.RIVER):
                self.bearInTheRiver(self.Bear.positionI,self.Bear.positionJ)

    def bearUp(self):    
        currentCell=self.__labyrinth[self.Bear.positionI-1][self.Bear.positionJ].get_cell_type()
        if ((currentCell!=CellType.WALL)and(currentCell!=CellType.MONOLITH)and(currentCell!=CellType.EMPTY)):
            if((self.Player.positionI==self.Bear.positionI-2)and(self.Player.positionJ==self.Bear.positionJ)):
                self.Player.life-=1
                print("Player damaged")
            self.Bear.positionI-=2     
               
            followingCell=self.__labyrinth[self.Bear.positionI][self.Bear.positionJ].get_cell_type()
            if (followingCell==CellType.WORMHOLE):
                self.bearWormhole(self.__labyrinth[self.Bear.positionI][self.Bear.positionJ])
            if (followingCell==CellType.RIVER):
                self.bearInTheRiver(self.Bear.positionI,self.Bear.positionJ)


    def bearDown(self):    
        currentCell=self.__labyrinth[self.Bear.positionI+1][self.Bear.positionJ].get_cell_type()
        if ((currentCell!=CellType.WALL)and(currentCell!=CellType.MONOLITH)and(currentCell!=CellType.EMPTY)):
            if((self.Player.positionI==self.Bear.positionI+2)and(self.Player.positionJ==self.Bear.positionJ)):
                self.Player.life-=1
                print("Player damaged")
            self.Bear.positionI+=2     
               
            followingCell=self.__labyrinth[self.Bear.positionI][self.Bear.positionJ].get_cell_type()
            if (followingCell==CellType.WORMHOLE):
                self.bearWormhole(self.__labyrinth[self.Bear.positionI][self.Bear.positionJ])
            if (followingCell==CellType.RIVER):
                self.bearInTheRiver(self.Bear.positionI,self.Bear.positionJ)


    def bearWormhole(self,wormhole):
        for i in range(1,self.__size*2):
            for j in range(1,self.__size*2):
                if self.__labyrinth[i][j].get_cell_type()==CellType.WORMHOLE:
                    if self.__labyrinth[i][j].get_number()==((wormhole.get_number()+1)%5):
                        self.Bear.positionI=i
                        self.Bear.positionJ=j


    def bearInTheRiver(self,Pi,Pj):
        if self.__labyrinth[Pi+1][Pj].get_cell_type()==CellType.RIVER:
            self.Bear.positionI=Pi+2
            self.Bear.positionJ=Pj


    

   

    def show_labyrinth(self):
        """print each cells of the labyrinth"""
        for i in range(0,self.__size*2+1):
            for j in range(0,self.__size*2+1):
                if ((i==self.Bear.positionI)and(j==self.Bear.positionJ)):
                    print("B", end="")
                else:
                    print(self.__labyrinth[i][j], end="")

            print("")









    def export_labyrinth(self):
        """:returns a string with the labyinth represented by symbols"""
        export = ""
        for i in self.__labyrinth:
            for j in i:
                export += str(j)
            export += "\n"
        return export

  

