# -*- coding: utf-8 -*-

import numpy as np
import pickle
#from mob import *
#from item import *
#from skill import *

# Class
class Mob(object): # Player and enemy
	def __init__(self, type, name, lvl, exp, hp, pp, hpm, ppm, atk, dfd, spd, pack, coin, skill, weapon, helmet, chestplate, leggings, boots):
		self.type = type
		self.name = name
		self.lvl = lvl
		self.exp = exp
		self.hp = hp
		self.pp = pp
		self.hpm = hpm
		self.ppm = ppm
		self.atk = atk
		self.dfd = dfd
		self.spd = spd
		self.pack = pack
		self.coin = coin
		self.skill = skill
		self.weapon = weapon
		self.helmet = helmet
		self.chestplate = chestplate
		self.leggings = leggings
		self.boots = boots

class Item(object): # Potion, armor, weapon, etc
	def __init__(self, type, name, range, mobs, affectSingle):
		self.type = type
		self.name = name
		self.range = range
		self.mobs = mobs
		self.affectSingle = affectSingle
		
	def affect(self):
		for mob in self.mobs:
			self.affectSingle(mob)
	
class Skill(object): # How to attack
	def __init__(self, name, pp, range, senders, targets, affectSender, affectTarget):
		self.name = name
		self.pp = pp
		self.range = range
		self.senders = senders # It is a selector
		self.targets = targets # It is a selector
		self.affectSender = affectSender
		self.affectTarget = affectTarget
		
	def getMobs(self, selector, sender, target, player, enemyList): # Here 'sender' means who uses the skill (who has got this skill), not same as 'senders' in class 'Skill' definition. In fact 'senders' is often equal to a list only containing the 'sender'
		operation = {SELF: [sender], CERTAIN_ENEMY: [target], ALL_ENEMY: enemyList if sender.type == PLAYER else [player]}
		return operation[selector]
		
	def affect(self, sender, target, player, enemyList):
		for sender in self.getMobs(self.senders, sender, target, player, enemyList):
			self.affectSender(sender)
		for target in self.getMobs(self.targets, sender, target, player, enemyList):
			self.affectTarget(target)
	
# Constant
MAX_LEVEL = 0
SHOP_PERIOD = 10

PLAYER = 0
ENEMY = 1
WEAPON = 2
HELMET = 3
CHESTPLATE = 4
LEGGINGS = 5
BOOTS = 6

ALIVE = 7
DEAD = 8

SELF = 9
CERTAIN_ENEMY = 10
ALL_ENEMY = 11

# Function
exp = lambda x: int(5 * x ** np.e / np.log(x ** 2 - x + 1.25) - 22)
hpm = lambda x: 10 * x
ppm = lambda x: 5 * x
atk = lambda x: 5 * x
dfd = lambda x: 5 * x
spd = lambda x: 5 * x

def getEnemyList(path):
	with open(path, 'wb') as f:
		data = pickle.load(f)
	return data
	
def printMobListInfo(moblist):
	print('生物列表：')
	print('ID\t名称\t等级\tHP\t武器\t头盔\t胸甲\t腿甲\t靴子')
	for idx in range(len(moblist)):
		print(idx, moblist[idx].name, moblist[idx].lvl, moblist[idx].hp, moblist[idx].weapon.name, moblist[idx].chestplate.name, moblist[idx].leggings.name, moblist[idx].boots.name)
		
def printPlayerSkillInfo(player):
	print('技能列表：')
	print('ID\t名称\tPP\t范围')
	for idx in range(len(player.skill)):
		print(idx, player.skill[idx].name, player.skill[idx].pp, player.skill[idx].range)
	
def printPlayerItemInfo(player):
	keyList = list(player.pack.keys())
	valueList = list(player.pack.values())
	print('物品列表：')
	print('ID\t名称\t数量\t范围')
	for idx in range(len(player.pack)):
		print(idx, keyList[idx].name, valueList[idx], keyList[idx].range)