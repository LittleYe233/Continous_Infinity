# -*- coding: utf-8 -*-

from definition import *
from functools import reduce
import mob
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
	level = 0
	enemyList = []
	mobList = []
	
	# Every Level
	while True:
		level += 1
		enemyList = getEnemyList('Level/level{}.dat'.format(level))
		# Print Level Info
		print('===== 当前关卡： 第{}关 ====='.format(level))
		print('怪物列表：')
		print('ID\t名称\t等级\tHP\t武器\t头盔\t胸甲\t腿甲\t靴子')
		for idx in range(len(enemyList)):
			print(idx, enemyList[idx].name, enemyList[idx].lvl, enemyList[idx].hp, enemyList[idx].weapon.name, enemyList[idx].chestplate.name, enemyList[idx].leggings.name, enemyList[idx].boots.name)
		# Judge Mob Order
		aveLvl = reduce(lambda x, y: x.lvl + y.lvl, enemyList) // len(enemyList)
		mobList = enemyList + [player] if aveLvl > player.lvl else [player] + enemyList
		# Every-Round Initilization
		mobIter = None
		# Every Round
		while True:
			try:
				currentMob = mobIter.__next__()
			except:
				mobIter = mobList.__iter__()
				currentMob = mobIter.__next__()
			print('这是{}的回合！'.format(currentMob.name))
			if currentMob.type == ENEMY:
				# Random Skill
				currentSkill = random.choice(currentMob.skill)
				print('{}使用了{}技能！'.format(currentMob.name, currentSkill.name))
			else:
				print('命令列表：')
	
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
#player = mob.initPlayer

welcome()

while True:
	cmd = input('>>> ')
	try:
		lobbyChoiceList[int(cmd)]()
	except:
		pass
