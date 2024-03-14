#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_6_6():
    c = 1
    move_right()
    while not wall_is_on_the_right():
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                fill_cell()
            while not wall_is_beneath():
                move_down()
        move_right()
        c += 1
    else:
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                fill_cell()
            while not wall_is_beneath():
                move_down()
        
    move_left(c)

if __name__ == '__main__':
    run_tasks()
