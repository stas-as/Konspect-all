#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while not wall_is_on_the_left():
        
        if not wall_is_beneath():
            while not wall_is_beneath():
                move_down()
            while not wall_is_on_the_right():
                move_right()
        move_left()


if __name__ == '__main__':
    run_tasks()
