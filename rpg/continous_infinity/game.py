# -*- coding: utf-8 -*-

from definition import *
import os
import sys

# Definitions
# lobbyChoiceList
def welcome():
	print('==========================')
	print('    Continous Infinity')
	print('==========================')
	print('   命令列表：')
	print('   0：开始游戏')
	print('   1：设置')
	print('   2：规则')
	print('   3：关于')
	print('   4：退出')
	print('==========================')
	
def play():
	pass
	
def option():
	pass
	
def rule():
	pass
	
def about():
	pass
	
def quit():
	os._exit(0);
	
lobbyChoiceList = [play, option, rule, about, quit]
	
# Main Function
#player = Mob()
enemyList = []
mobList = []

welcome()

while True:
	cmd = input('>>> ')
	try:
		lobbyChoiceList[int(cmd)]()
	except:
		pass
