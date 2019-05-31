# -*- coding: utf-8 -*-

import numpy as np
import pickle
#from mob import *
#from item import *
#from skill import *

# Class
class Mob(object): # Player and enemy
	def __init__(self, type, name, lvl, exp, hp, mp, hpm, mpm, atk, dfd, spd, pack, coin, skill, weapon, helmet, chestplate, leggings, boots):
		self.type = type
		self.name = name
		self.lvl = lvl
		self.exp = exp
		self.hp = hp
		self.mp = mp
		self.hpm = hpm
		self.mpm = mpm
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
	def __init__(self, type, name, mobs, affectSingle):
		self.type = type
		self.name = name
		self.mobs = mobs
		self.affectSingle = affectSingle
		
	def affect(self):
		for mob in self.mobs:
			self.affectSingle(mob)
	
class Skill(object): # How to attack
	def __init__(self, name, senders, targets, affectSender, affectTarget):
		self.name = name
		self.senders = senders
		self.targets = targets
		self.affectSender = affectSender
		self.affectTarget = affectTarget
		
	def affect(self):
		for sender in self.senders:
			self.affectSender(sender)
		for target in self.targets:
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

# Function
exp = lambda x: int(5 * x ** np.e / np.log(x ** 2 - x + 1.25) - 22)
hpm = lambda x: 10 * x
mpm = lambda x: 5 * x
atk = lambda x: 5 * x
dfd = lambda x: 5 * x
spd = lambda x: 5 * x

def getEnemyList(path):
	with open(path, 'wb') as f:
		data = pickle.load(f)
		
	return data