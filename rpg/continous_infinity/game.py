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
	mobIter = None
	playerStatus = ALIVE
	score = 0
	
	# Every Level
	while True:
		level += 1
		enemyList = getEnemyList('Level/level{}.dat'.format(level))
		# Judge Mob Order
		aveLvl = reduce(lambda x, y: x.lvl + y.lvl, enemyList) / len(enemyList)
		mobList = enemyList + [player] if aveLvl > player.lvl else [player] + enemyList
		# Print Level Info
		print('===== 当前关卡： 第{}关 ====='.format(level))
		print(printMobListInfo(mobList))
		# Every-Round Initilization
		mobIter = None
		# Every Round
		while True:
			# Get Legal Mob
			while True:
				try:
					currentMob = mobIter.__next__()
				except:
					mobIter = mobList.__iter__()
					currentMob = mobIter.__next__()
				# Legal Mob Should Have Healthpoint
				if currentMob.hp > 0:
					break
			print('这是{}的回合！'.format(currentMob.name))
			if currentMob.type == ENEMY:
				# Random Skill
				currentSkill = random.choice(currentMob.skill)
				print('{}使用了{}技能！'.format(currentMob.name, currentSkill.name))
				# Print Skill Effects
				# ...
				# ...
				# ...
			else:
				print('命令列表：')
				print('显示技能(0) 显示背包(1) 使用技能(2) 使用背包(3)')
				print('命令用法：0 或 1 或 2 <技能ID> 或 3 <物品ID>')
				while True:
					cmd = input('>>> ')
					if cmd == '0':
						printPlayerSkillInfo(player)
					elif cmd == '1':
						printPlayerItemInfo(player)
					elif cmd == '2':
						pass
					elif cmd == '3':
						pass
			# Print Everyone Info
			printMobListInfo(mobList)
			for idx in mobList:
				if idx.hp <= 0:
					print('{}死亡！'.format(idx.name))
			# Judge If Player Is Dead
			if player.hp <= 0:
				playerStatus = DEAD
				print('玩家死亡，游戏结束！')
				break
		if playerStatus == DEAD:
			break
	if playerStatus == DEAD:
		break
		
	# Calculate Scores
	print('==========================')
	print('你的分数：', score, sep = '')
	print('==========================')
	
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