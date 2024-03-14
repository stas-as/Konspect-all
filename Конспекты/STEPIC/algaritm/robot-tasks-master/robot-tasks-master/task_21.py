#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    for i in range(1,14):
        if i % 2 == 1:
            move_down()
            fill_cell()
            for _ in range(1,i):
                fill_cell()
                move_left()
            fill_cell()
        else:

            move_down()
            fill_cell()
            for _ in range(1,i):
                fill_cell()
                move_right()
            fill_cell()
            move_right()
    move_down()


if __name__ == '__main__':
    run_tasks()
