#! /usr/bin/env python

from operator import itemgetter
import sys
import fileinput

current_turf = None
current_count = 0

for line in fileinput.input():
      line = line.strip()
   #   print line
      turf, count = line.split('\t')
      try:
         count = int(count)
      except ValueError:
         continue
      if not current_turf:
            current_turf = turf
      if current_turf == turf:
         current_count += count
      else:
#          if current_turf:
               print '%s\t%s' % (current_turf, current_count)
               current_turf = turf
               current_count = 1
               
#      if current_turf == turf:
print '%s\t%s' % (current_turf, (current_count)) 

