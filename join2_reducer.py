#!/usr/bin/env python
#--------------
#this reducer code will input a line of text and
#    output <word, total-count>
# ---------------------------------------------------------------
import sys

last_key      = None              #initialize these variables
running_total = 0
programs = ["" for x in range(100)]

# -----------------------------------
# Loop thru file
#  --------------------------------
for input_line in sys.stdin:
    input_line = input_line.strip()

    # --------------------------------
    # Get Next Word    # --------------------------------
    this_key, value = input_line.split(",")  #the Hadoop default is tab separates key value
    if this_key=="ABC":
        programs.append(value)           #int() will convert a string to integer (this program does no error checking)
    else:       # this will be numbers
        if this_key in programs:
            if last_key == this_key:
                running_total += int(value)
            else:
                if last_key:
                    print( "{0}\t{1}".format(last_key, running_total) )
                running_total = int(value)
                last_key = this_key
if last_key == this_key:
    print( "{0}\t{1}".format(last_key, running_total))
