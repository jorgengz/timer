#! /usr/bin/env python
"""ASCII countdown timer for the Terminal."""
__author__ = "Jorgen Granseth"
__copyright__ = "Jorgen Granseth"
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Jorgen Granseth"
__email__ = "jorgengranseth@gmail.com"
import sys
import time
import curses

def write(screen, message, alarm=True, delay=0.2, x=0, y=0):
    if alarm:
        sys.stdout.write("\a")
    screen.addstr(x, y, message)
    screen.refresh()
    time.sleep(delay)

def _string_to_whitespace(s):
    """
    Convert a multiline string using newline characters to whitespace in the
    corresponding area.
    """
    out = ""
    for line in [x for x in s.split("\n") if x != ""]:
        out += len(line) * " " + "\n"

    return out

def symbols():
    """
    Returns a list of the numbers 0-9 on ASCII form.  Colon (' :') is on index
    10, and whitespace for fitting in a standard 80 x 24 terminal on index 11.
    """
    ZERO = "\
  #### \n\
 #    #\n\
 #    #\n\
 #    #\n\
 #    #\n\
 #    #\n\
  #### \n\
"

    ONE = "\
   ##  \n\
  # #  \n\
 #  #  \n\
    #  \n\
    #  \n\
    #  \n\
 ######\n\
"
    TWO = "\
  #### \n\
 #    #\n\
 #   # \n\
    #  \n\
   #   \n\
  #    \n\
 ######\n\
"

    THREE = "\
  #### \n\
 #    #\n\
      #\n\
    ## \n\
      #\n\
 #    #\n\
  #### \n\
"

    FOUR = "\
 #   # \n\
 #   # \n\
 #   # \n\
 ######\n\
     # \n\
     # \n\
     # \n\
"
    FIVE = "\
 ######\n\
 #     \n\
 #     \n\
 ##### \n\
      #\n\
 #    #\n\
  #### \n\
"

    SIX = "\
  #### \n\
 #    #\n\
 #     \n\
 ##### \n\
 #    #\n\
 #    #\n\
  #### \n\
"

    SEVEN = "\
 #######\n\
 #    # \n\
     #  \n\
   ###  \n\
   #    \n\
  #     \n\
 #      \n\
"

    EIGHT = "\
  #### \n\
 #    #\n\
 #    #\n\
  #### \n\
 #    #\n\
 #    #\n\
  #### \n\
"

    NINE = "\
  #### \n\
 #    #\n\
 #    #\n\
  #####\n\
      #\n\
 #    #\n\
  #### \n\
"

    COLON = "\
  \n\
  \n\
 #\n\
  \n\
 #\n\
  \n\
  \n\
"
    WHITESPACE = "\
                \n\
                \n\
                \n\
                \n\
                \n\
                \n\
                \n\
"
    return [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE,\
            COLON, WHITESPACE]

def combine_ASCII(*nums):
    """Combines ASCII art characters to one string."""
    output = []
    for k in range(len(nums)):
        output.append([line for line in nums[k].split("\n") if line != ""])

    ret = ""

    for k in range(len(output[0])):
        for number in output:
            ret += number[k]
        ret += "\n"

    return ret

def number_to_ASCII(n):
    """
    Returns integer n on ASCII form with two digits,
    so 3 is returned as 03 while 15 is returned as 15.
    """
    s = "{:02d}".format(n)
    num = symbols()
    m = num[int(s[0])]
    n = num[int(s[1])]

    return combine_ASCII(m, n)

def done(screen):
    done = "\
                    #####     #####    ##     #   ######   #\n\
                    #    #   #     #   # #    #   #        #\n\
                    #    #   #     #   #  #   #   #        #\n\
                    #    #   #     #   #   #  #   ####     #\n\
                    #    #   #     #   #    # #   #        #\n\
                    #    #   #     #   #     ##   #         \n\
                    #####     #####    #      #   ######   #\n"

    empty = _string_to_whitespace(done)

    while True:
        write(screen, empty, x=7)
        write(screen, done, x=7)

def out(t):
    """
    Converts a time 't' in seconds to ASCII output.
    """
    hour = number_to_ASCII(int(t/3600.))
    minute = number_to_ASCII(int((t % 3600) / 60.))
    second = number_to_ASCII(t % 60)
    colon = symbols()[10]
    whitespace = symbols()[11]

    return combine_ASCII(whitespace, hour, colon, minute, colon, second)

def get_duration():
    """
    Gets the duration of the timer from the cml.

    Defaults to 5 minutes if nothing is given.
    """
    num_args = len(sys.argv)
    t = 300         # Default time: 5 minutes
    if num_args == 2:
        t = float(sys.argv[1])
    elif num_args == 3:
        t = float(sys.argv[1]) * 60 + float(sys.argv[2])
    elif num_args == 4:
        t = float(sys.argv[1]) * 3600\
            + float(sys.argv[2]) * 60\
            + float(sys.argv[3])
    return int(t)

if __name__ == "__main__":
    try:
        t = get_duration()
        stdscreen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        while t > 0:
            write(stdscreen, out(t), alarm=False, delay=1, x=7)
            t -= 1
        done(stdscreen)
    except:
        sys.stdout.write("")
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()

