
# -*- coding: utf-8 -*-

import ctypes
import time

lib = ctypes.windll.kernel32

def test():
	lib.Beep(400, 1000)
	
test()
