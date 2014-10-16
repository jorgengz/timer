#! /usr/bin/env python
import sys
import time
import curses
from timer import write, number_to_ASCII, combine_ASCII, symbols

if __name__ == "__main__":
    try:
        stdscreen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        while True:
            t = time.localtime()
            hour = number_to_ASCII(t.tm_hour)
            minute = number_to_ASCII(t.tm_min)
            sec = number_to_ASCII(t.tm_sec)
            colon = symbols()[10]
            whitespace = symbols()[11]

            out = combine_ASCII(whitespace, hour, colon, minute, colon, sec)

            write(stdscreen, out, alarm=False, x=7)
    except:
        sys.exit(0)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
