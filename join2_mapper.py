#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <date word, value> input file, and move date into
#  the value field for output
#
#  Note, this program is written in a simple style and does not full advantage of Python
#     data structures,but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------



for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item

    #print key_in
    if value_in.isdigit()==False and  value_in=='ABC':           #if this entry has show name in key
        tvshow = key_in      #now get channel from key field
        channel="ABC"
        count= "*"
        print( '%s,%s' % (channel,tvshow))
    else:
        if value_in.isdigit()==True:
                channel ="*"
                tvshow = key_in
                count = value_in
                print( '%s,%s' % (tvshow,count))
