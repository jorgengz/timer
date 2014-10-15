#! /usr/bin/env python
import sys
import time
import curses

# TODO:
#   Add support for hours, maybe days?
#   Make ASCII numbers

def clear_and_delay(d):
    sys.stdout.write(empty)
    sys.stdout.flush()
    time.sleep(d)

def write_to_terminal(message, delay):
    sys.stdout.write(message)
    sys.stdout.flush()
    time.sleep(delay)

def write(screen, message, alarm=True, delay=0.2, x=0, y=0):
    if alarm:
        sys.stdout.write("\a")
    screen.addstr(x, y, message)
    screen.refresh()
    time.sleep(delay)

def msg_to_whitespace(s):
    out = ""
    for char in s:
        if char != "\n":
            out += " "
        else:
            out += char
    return out


def done(screen):
    # done = "\a###DONE###\r"
    # empty = "\a" + " " * max(50, len(done)) + "\r"
    done = "\
                    #####     #####   ##     #    ######  #\n\
                    #    #   #     #  # #    #    #       #\n\
                    #    #   #     #  #  #   #    #       #\n\
                    #    #   #     #  #   #  #    ####    #\n\
                    #    #   #     #  #    # #    #       #\n\
                    #    #   #     #  #     ##    #        \n\
                    #####     #####   #      #    ######  #\n"

    empty = msg_to_whitespace(done)

    write(screen, " " * 50, alarm=False, delay=0, x=11, y=30)
    while True:
        write(screen, empty, x=7)
        write(screen, done, x=7)
        # sys.stdout.write("\a")
        # write_to_terminal(empty, 0.2)
        # write_to_terminal(done, 0.2)

if len(sys.argv) > 1:
    x = int(sys.argv[1])
else:
    x = 300

out = "Time left: %02d:%02d"

try:
    stdscreen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    while x > 0:
        msg = out % (int(x / 60.), x % 60)
        write(stdscreen, msg, alarm=False, delay=1, x=11, y=30)
        # write_to_terminal(msg, 1)
        x -= 1
    done(stdscreen)
except:
    sys.stdout.write("")
finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()

