"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    go_in()
    put_99()
    go_out()
    go_in()
    put_99()
    go_out()
    go_in()
    put_99()
    go_out()
    def main():
        for i in range(3):
            go _in()
            put_99()
            go_out()
    def go_in():
        pre_condition: karel is at the upper left of the pothole,facing_east
        post_condition: karel is in the pothole, facing_south
        move()
        turn_right()
        move()
    def go_out():
        pre_condition:karel is in the pothole, facing_south

    """
    pass
    for i in range(3):
            go_in()
            put_99()
            go_out()

def go_in():
        """
        pre_condition: karel is at the upper left of the pothole,facing_east
        post_condition: karel is in the pothole, facing_south
        """
        move()
        turn_right()
        move()
def go_out():
        """
        pre_condition: karel is in the pothole, facing_south
        post_condition: karel is at the upper left of the pothole,facing_east
        """
        turn_around()
        move()
        turn_right()
        move()

def turn_right():
        for i in range(3):
             turn_left()

def put_99():
    for i in range(99):
            put_beeper()

def turn_around():
    for i in range(2):
            turn_left()












####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
