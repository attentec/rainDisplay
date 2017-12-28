#!/usr/bin/env python

import random
import time
import sys
import subprocess

rows = 4
columns = 8

#1234567
heart="""
  R R   
 RRRRR  
  RRR   
   R    
"""
heart = [row for row in heart.split("\n")[1:rows+1]]

def render_text_matrix(text, spaces):
    p = subprocess.Popen(["./display/figlet.sh", text.upper()], stdout=subprocess.PIPE)
    out, _ = p.communicate()
    space = " " * spaces
    matrix = [space + row + space for row in out.decode("utf-8").split("\n")[:rows]]
    return matrix


def _get_color(char, color=(255, 255, 255)):
    if char == " ":
        return (0, 0, 0)
    elif char == "R":
        return (255, 0, 0)
    else:
        return color


def _get_multi_color(char):
    if char == "8":
        return (100, 100, 255)
    if char in "wbP":
        return (255, 100, 100)
    elif char in ".Y":
        return (0, 0, 100)
    elif char == " ":
        return (0, 0, 0)
    elif char in "X":
        return (255, 255, 255)
    elif char in "R":
        return (255, 0, 0)
    else:
        return (100, 255, 100)


def render_matrix_offset(matrix, offset, blackwhite=True):
    import unicornhat as unicorn
    unicorn.clear()
    for y in range(0, rows):
        for x in range(0, columns):
            if blackwhite:
                r, g, b = _get_color(matrix[y][x+offset])
            else:
                r, g, b = _get_multi_color(matrix[y][x+offset])
            unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()


def show_heart():
    render_matrix_offset(heart, 0, blackwhite=False)


def show(text, loops, time_delta, spaces):
    matrix = render_text_matrix(text, spaces)
    assert len(matrix) == rows
    for i in range(loops):
        for offset in range(len(matrix[0]) - columns):
            render_matrix_offset(matrix, offset)
            time.sleep(time_delta)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = "TESTING"
    if len(sys.argv) > 2:
        loops = int(sys.argv[2])
    text_matrix = render_text_matrix(text, 0)
    for row in text_matrix:
        print("OUT", row, len(row))
    for row in heart:
        print("OUT", row, len(row))

