#! /usr/bin/env python

import fileinput


#x= sys.stdin
for line in fileinput.input():
#    print line
    line = line.strip()
    stadium, capacity, expanded, location, surface, turf, team, opened, weather, roof, elevation  = line.split(",")
    #print turf

    if turf == 'FALSE':
           print '%s\t %s' % (turf, 1)
    elif turf == 'TRUE':  #((turfs == 'T') and (turfs == 'R') and (turfs == 'U') and (turfs == 'E')): 
                   print '%s\t %s' % (turf, 1)
