#!/usr/bin/python3

from pyrob.api import *
def star():
    move_right()
    fill_cell()
    for _ in range(2):
        move_down()
        fill_cell()
    move_up()
    move_right()
    fill_cell()
    for _ in range(2):
        move_left()
        fill_cell()
    move_up()

@task
def task_2_2():
    move_down()
    star()
    for _ in range(4):
        for i in range(4):
            move_right()
        star()


if __name__ == '__main__':
    run_tasks()
