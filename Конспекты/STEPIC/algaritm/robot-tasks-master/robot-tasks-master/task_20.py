#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    x = 1
    y = 1
    while not wall_is_on_the_right():
        move_right()
        x += 1
    move_up
    while not wall_is_beneath():
        move_down()
        y += 1
    move_up()
    move_up()
    for _ in range(x - 2):
        move_left()
        for _ in range(y-2):
            fill_cell()
            move_up()
        for _ in range(y-2):
            move_down()
    move_down()
        
        
        
    

if __name__ == '__main__':
    run_tasks()
