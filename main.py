import random

width = 10
height = 10
mines = 10

field = [[0 for x in range(width)] for y in range(height)]

for i in range(mines):
    while True:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if field[y][x] != 'X':
            field[y][x] = 'X'
            break

import curses

screen = curses.initscr()
curses.curs_set(0)

for y in range(height):
    for x in range(width):
        if field[y][x] == 'X':
            screen.addstr(y, x * 2, 'X')
        else:
            screen.addstr(y, x * 2, '.')
    screen.addstr(y, width * 2, '\n')

while True:
    screen.addstr(height, 0, 'Enter move (row,column): ')
    screen.refresh()
    move = screen.getstr().decode().split(',')
    y = int(move[0])
    x = int(move[1])

    if field[y][x] == 'X':
        screen.addstr(height + 1, 0, 'You lose!')
        break
    else:
        screen.addstr(y, x * 2, str(count_mines_around(field, x, y)))


def open_cell(field, x, y):
    if field[y][x] == 0:
        field[y][x] = '.'
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if x + dx < 0 or x + dx >= width or y + dy < 0 or y + dy >= height:
                    continue
                open_cell(field, x + dx, y + dy)
    else:
        field[y][x] = str(field[y][x])
