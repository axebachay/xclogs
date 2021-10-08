#!/usr/bin/python3

import os
import glob
import re

wc = "/home/alex/XCTrack/TrackLogs/*.igc"
sec = 0

logfiles = glob.glob(wc)
for logfile in logfiles:
    with open(logfile) as f:
#        sec = 0
        for line in f:
            if re.match("B",line):
                sec = sec + 1
        print(sec/3600)        
