# from itertools import cycle
# from time import sleep

# for frame in cycle(r'anaus'):
#     print('\r', frame, sep='', end='', flush=True)
#     sleep(0.2)

# from time import sleep

# def progress(percent=0, width=30):
#     left = width * percent // 100
#     right = width - left
#     print('\r[', '#' * left, ' ' * right, ']',
#           f' {percent:.0f}%',
#           sep='', end='', flush=True)

# for i in range(101):
#     progress(i)
#     sleep(0.1)
# print("\n")
# import sys
# from time import sleep

# for i in range(10):
#     print("Blau ist an ")
#     sys.stdout.write("\033[F")
#     sleep(.5)
#     print("Blau ist aus")
#     sys.stdout.write("\033[F")
#     sleep(.5)

import curses
import time
  
# # Initializing curses 
# stdscr = curses.initscr()
  
# # Setting the cursor to visible by 
# # inserting 1 as argument
# curses.curs_set(1)  
  
# # Delay of 2 seconds
# time.sleep(2)
  
# # Setting the cursor to invisible by 
# # inserting 0 as argument
# curses.curs_set(0) 
  
# # Delay of 2 seconds
# time.sleep(2)
  
# # Setting the cursor to visible by 
# # inserting 1 as argument
# curses.curs_set(1)  
  
# # Delay of 2 seconds
# time.sleep(2)
  
# # Restoring terminal to it's
# # original state
# curses.endwin()

stdscr = curses.initscr()
curses.curs_set(0)
time.sleep(2)
curses.curs_set(1)
curses.endwin()