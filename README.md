ASCII timer in the terminal, because I got bored in a lecture.

usage:

$ python timer.py [[[ h ] m ] s]

where h, m and s specify the timer's duration. The default is 5 minutes.

CTRL+C to quit at any time.

Flashes and beeps annoyingly on completion if you enable the visual and
audible bells of your terminal (resp.).

Feel free to do

$ cp timer.py /usr/local/bin/timer

to access it from anywhere with

$ timer [[[ h ] m ] s]

... it is that cool after all.
