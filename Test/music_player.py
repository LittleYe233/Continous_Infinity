# -*- coding: utf-8 -*-

import time
import ctypes

lib = ctypes.windll.kernel32

noteTrans = {} # input the location of a note and output the height
bpm = 120 # beat per minute
mspb = 60000 / bpm # msecond per beat

def play(filelist):
    notelist = filelist.split()
    notelist = [note.split(',') for note in notelist]
    for note in notelist:
        lib.beep(noteTrans[note[0]], mspb * float(note[1]))
    return None

with open('notelist.txt', 'r') as f:
    filelist = f.read()

play(filelist)
