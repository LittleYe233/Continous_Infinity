# -*- coding: utf-8 -*-

import time
import ctypes

lib = ctypes.windll.kernel32

noteTrans = {'-11a': 110.0, '-10s': 116.541, '-10a': 123.471, '-9s': 130.813, '-9a': 138.591, '-8s': 146.832, '-8a': 155.563, '-7s': 164.814, '-7a': 174.614, '-6s': 184.997, '-6a': 195.998, '-5s': 207.652, '-5a': 220.0, '-4s': 233.082, '-4a': 246.942, '-3s': 261.626, '-3a': 277.183, '-2s': 293.665, '-2a': 311.127, '-1s': 329.628, '-1a': 349.228, '0s': 369.994, '0a': 391.995, '1s': 415.305, '1a': 440.0, '2s': 466.164, '2a': 493.883, '3s': 523.251, '3a': 554.365, '4s': 587.33, '4a': 622.254, '5s': 659.255, '5a': 698.456, '6s': 739.989, '6a': 783.991, '7s': 830.609, '7a': 880.0, '8s': 932.328, '8a': 987.767, '9s': 1046.502, '9a': 1108.731, '10s': 1174.659, '10a': 1244.508, '11s': 1318.51, '11a': 1396.913, '12s': 1479.978, '12a': 1567.982, '13s': 1661.219, '13a': 1760.0} # input the location of a note and output the height
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
