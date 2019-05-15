# -*- coding: utf-8 -*-

from definition import *

# Mob(self, type, name, lvl, exp, hp, mp, hpm, mpm, atk, dfd, spd, pack, coin, skill, weapon, helmet, chestplate, leggings, boots)
# Item(self, type, name, mobs, affectSingle)
# Skill(self, name, mobs, affectSingle)

# Player
init_player = Mob(PLAYER, 'Player', 1, exp(1), hpm(1), mpm(1), hpm(1), mpm(1), atk(1), dfd(1), spd(1), {}, 0, {}, None, None, None, None, None)

# Enemy
