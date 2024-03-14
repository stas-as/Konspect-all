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

@task(delay=0.02)
def task_2_4():
    star()
    for _ in range(9):
        for i in range(4):
            move_right()
        star()
    for _ in range(4):
        move_left(36)
        move_down(4)
        star()
        for _ in range(9):
            for i in range(4):
                move_right()
            star()
    move_left(36)
    

if __name__ == '__main__':
    run_tasks()
