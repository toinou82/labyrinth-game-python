import sys
import random
from abc import *
from enum import Enum

from services.command import IUserCommand
from services.knowledge_base.knowledge_base import IKnowledgeBase


from impl.labyrinth.Labyrinth import *
from impl.labyrinth.Player import Player

class Finish(IUserCommand):


    def get_command_tag(self):
        return "finish"

    def get_args_count(self):
        return 0

    def evaluate(self, args,labyrinth):
        return (True, "Finished.")


class Skip(IUserCommand):
    def get_command_tag(self):
        return "p"
    def get_args_count(self):
        return 0
    def evaluate(self, args,labyrinth):    
        if labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ].get_cell_type()==CellType.RIVER:
            labyrinth.inTheRiver(labyrinth.Player.positionI,labyrinth.Player.positionJ)
        else:
            print("Skiped")
        return (False, "")


class MoveRight(IUserCommand):
    def get_command_tag(self):
        return "d"
    def get_args_count(self):
        return 0
    def evaluate(self, args,labyrinth):
        currentCell=labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ+1].get_cell_type()
        if currentCell==CellType.WALL:
            print("Impossible there is a wall")
        elif currentCell==CellType.MONOLITH:
            print("Impossible there is a monolith")
        elif (currentCell==CellType.EMPTY):
            if labyrinth.Player.HaveTreasure:
                print("You Won !!!")
                return (True, "")
            else:
                print("No Treasure")
                return (False, "")
        elif((labyrinth.Player.positionI==labyrinth.Bear.positionI)and(labyrinth.Player.positionJ+2==labyrinth.Bear.positionJ)):
            labyrinth.Player.life-=1
            print("Player damaged")

        else:
            labyrinth.Player.positionJ+=2
            print("step executed")
            followingCell=labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ].get_cell_type()
            if (followingCell==CellType.TREASURE)and not(labyrinth.Player.HaveTreasure):
                labyrinth.Player.HaveTreasure=True
                print("You get the treasure")
            if (followingCell==CellType.WORMHOLE):
                labyrinth.goToNextWormhole(labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ])
                print("Wormhole!!")
            if (followingCell==CellType.RIVER):
                labyrinth.inTheRiver(labyrinth.Player.positionI,labyrinth.Player.positionJ)
        return (False, "")

class MoveLeft(IUserCommand):
    def get_command_tag(self):
        return "q"
    def get_args_count(self):
        return 0
    def evaluate(self, args,labyrinth):
        currentCell=labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ-1].get_cell_type()
        if currentCell==CellType.WALL:
            print("Impossible there is a wall")
        elif currentCell==CellType.MONOLITH:
            print("Impossible there is a monolith")
        elif (currentCell==CellType.EMPTY):
            if labyrinth.Player.HaveTreasure:
                print("You Won !!!")
                return (True, "")
            else:
                print("No Treasure")
                return (False, "")
        elif((labyrinth.Player.positionI==labyrinth.Bear.positionI)and(labyrinth.Player.positionJ-2==labyrinth.Bear.positionJ)):
            labyrinth.Player.life-=1
            print("Player damaged")
        else:
            labyrinth.Player.positionJ-=2
            print("step executed")
            followingCell=labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ].get_cell_type()
            if (followingCell==CellType.TREASURE)and not(labyrinth.Player.HaveTreasure):
                labyrinth.Player.HaveTreasure=True
                print("You get the treasure")
            if (followingCell==CellType.WORMHOLE):
                labyrinth.goToNextWormhole(labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ])
                print("Wormhole!!")
            if (followingCell==CellType.RIVER):
                labyrinth.inTheRiver(labyrinth.Player.positionI,labyrinth.Player.positionJ)
        return (False, "")


class MoveUp(IUserCommand):
    def get_command_tag(self):
        return "z"
    def get_args_count(self):
        return 0
    def evaluate(self, args,labyrinth):
        currentCell=labyrinth.get_labyrinth()[labyrinth.Player.positionI-1][labyrinth.Player.positionJ].get_cell_type()
        if currentCell==CellType.WALL:
            print("Impossible there is a wall")
        elif currentCell==CellType.MONOLITH:
            print("Impossible there is a monolith")
        elif (currentCell==CellType.EMPTY):
            if labyrinth.Player.HaveTreasure:
                print("You Won !!!")
                return (True, "")
            else:
                print("No Treasure")
                return (False, "")
        elif((labyrinth.Player.positionI-2==labyrinth.Bear.positionI)and(labyrinth.Player.positionJ==labyrinth.Bear.positionJ)):
            labyrinth.Player.life-=1
            print("Player damaged")
        else:
            labyrinth.Player.positionI-=2
            print("step executed")
            followingCell=labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ].get_cell_type()
            if (followingCell==CellType.TREASURE)and not(labyrinth.Player.HaveTreasure):
                labyrinth.Player.HaveTreasure=True
                print("You get the treasure")
            if (followingCell==CellType.WORMHOLE):
                labyrinth.goToNextWormhole(labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ])
                print("Wormhole!!")
            if (followingCell==CellType.RIVER):
                labyrinth.inTheRiver(labyrinth.Player.positionI,labyrinth.Player.positionJ)
        return (False, "")



class MoveDown(IUserCommand):
    def get_command_tag(self):
        return "s"
    def get_args_count(self):
        return 0
    def evaluate(self, args,labyrinth):
        currentCell=labyrinth.get_labyrinth()[labyrinth.Player.positionI+1][labyrinth.Player.positionJ].get_cell_type()
        if currentCell==CellType.WALL:
            print("Impossible there is a wall")
        elif currentCell==CellType.MONOLITH:
            print("Impossible there is a monolith")
        elif (currentCell==CellType.EMPTY):
            if labyrinth.Player.HaveTreasure:
                print("You Won !!!")
                return (True, "")
            else:
                print("No Treasure")
                return (False, "")
        elif((labyrinth.Player.positionI+2==labyrinth.Bear.positionI)and(labyrinth.Player.positionJ==labyrinth.Bear.positionJ)):
            labyrinth.Player.life-=1
            print("Player damaged")
        else:
            labyrinth.Player.positionI+=2
            print("step executed")
            followingCell=labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ].get_cell_type()
            if (followingCell==CellType.TREASURE)and not(labyrinth.Player.HaveTreasure):
                labyrinth.Player.HaveTreasure=True
                print("You get the treasure")
            if (followingCell==CellType.WORMHOLE):
                labyrinth.goToNextWormhole(labyrinth.get_labyrinth()[labyrinth.Player.positionI][labyrinth.Player.positionJ])
                print("Wormhole!!")
            if (followingCell==CellType.RIVER):
                labyrinth.inTheRiver(labyrinth.Player.positionI,labyrinth.Player.positionJ)
        return (False, "")

    
