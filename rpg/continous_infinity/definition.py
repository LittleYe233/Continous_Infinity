# -*- coding: utf-8 -*-

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
	def __init__(self, name, mobs, affectSingle):
		self.name = name
		self.mobs = mobs
		self.affectSingle = affectSingle
		
	def affect(self):
		for mob in self.mobs:
			self.affectSingle(mob)
	
# Constant
MAX_LEVEL = 0
SHOP_PERIOD = 10
