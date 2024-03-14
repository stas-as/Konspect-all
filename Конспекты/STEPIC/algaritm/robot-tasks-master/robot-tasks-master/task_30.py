#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.03)
def task_9_3():
    c = 1
    while not wall_is_beneath():
        c += 1
        move_down()
    x = c-2
    for _ in range(c//2):
        for i in range(x):
            move_right()
            fill_cell()
        move_right()
        for i in range(x):
            move_up()
            fill_cell()
        move_up()       
        for i in range(x):
            move_left()
            fill_cell()
        move_left()
        for i in range(x):
            move_down()
            fill_cell()
        move_down()
        x = x -2
        move_up()
        move_right()
    move_left(c//2)
    move_down(c//2)
if __name__ == '__main__':
    run_tasks()
