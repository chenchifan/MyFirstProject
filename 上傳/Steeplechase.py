"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()

    # while front_is_clear():
    #     move()
    #     jump()
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     jump()

def jump():
    up()
    cross()
    down()


def up():
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()
    turn_left()
    while not right_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cross():
    # if front_is_clear():
    #    move()
    #    turn_right()
    turn_right()
    move()
    turn_right()
def down():
    while front_is_clear():
        move()
    turn_left()












####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
