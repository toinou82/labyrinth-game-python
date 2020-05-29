### Lecture 2. Inversion of Control
### 01-3. Math Knowledge Base

import sys
import random
from abc import *
from enum import Enum

from services.command import *

from impl.commands import *


from impl.labyrinth.Labyrinth import *
from impl.labyrinth.Player import Player


def parse_user_input(user_input): 
    tokens = user_input.strip().split(" ")

    if len(tokens) == 0:
        return (None, None, "")

    norm_cmd = tokens[0].lower()

    if norm_cmd in supported_commands:
        cmd = supported_commands[norm_cmd]
        return (cmd, tokens[1:10], "")

    return (None, None, "Command not supported: ")

def eval_command(cmd : IUserCommand, args, labyrinth):
    if cmd.get_args_count() != len(args):
        return (False, "Invalid number of args. Expected: "
            + str(cmd.get_args_count()) + ", " + "got: " + str(len(args)))
    return cmd.evaluate(args,labyrinth)


def make_commands_dict(cmd_lst):
    cmd_dict = dict()
    for cmd in cmd_lst:
        cmd_dict[cmd.get_command_tag().lower().strip()] = cmd
    return cmd_dict

supported_commands = make_commands_dict(
    [ Finish()
    ,MoveLeft()
    ,MoveRight()
    ,MoveUp()
    ,MoveDown()
    ,Skip()
    ])


if __name__ == "__main__":


    finished = False

    print("Labyrinth")
    print("Choose the size")
    user_input = input("$> ")
    user_input=int(user_input)
    lab=Labyrinth(user_input)
    lab.define_exit()
    lab.generate_labyrinth()
    if (user_input<4)or(user_input>10):
        print("Incorrect Size")
        finished=True
    else:
        lab.show_labyrinth()
    
    

    
    state = ""
    message = ""
    args = []
    cmd = None
    try:
        while not(finished):
            
            user_input = input("$> ")
            cmd, args, message = parse_user_input(user_input)
            if cmd == None:
                print(message)
                continue
            
            (finished, message) = eval_command(cmd, args,lab)
            if message != "": print(message)
            lab.moveBear()
            lab.show_labyrinth()
            if lab.Player.life<1:
                print("You are dead")
                finished=True
    except:
        print("Unexpected error:", sys.exc_info()[0])
        lab.show_labyrinth()
    
   