#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    c = 1
    move_right()
    while not wall_is_on_the_right():
        fill_cell()
        for _ in range(c):
            if wall_is_on_the_right():
                break
            move_right()
        c+= 1


if __name__ == '__main__':
    run_tasks()
