# -*- coding: utf-8 -*-

from definition import *

# Mob(self, type, name, lvl, exp, hp, mp, hpm, mpm, atk, dfd, spd, pack, coin, skill, weapon, helmet, chestplate, leggings, boots)

# Player
init_player = Mob(PLAYER, '玩家', 1, exp(1), hpm(1), mpm(1), hpm(1), mpm(1), atk(1), dfd(1), spd(1), {}, 0, [], None, None, None, None, None)

# Enemy
# In fact enemies will be various in something like level, hp, atk, etc. Here are some examples for testing.
init_warrior1 = Mob(ENEMY, '战士I', 1, exp(1), hpm(1), mpm(1), hpm(1), mpm(1), atk(1), dfd(1), spd(1), {}, 0, [], None, None, None, None, None)
init_warrior2 = Mob(ENEMY, '战士II', 2, exp(1), hpm(2), mpm(2), hpm(2), mpm(2), atk(2), dfd(2), spd(2), {}, 0, [], None, None, None, None, None)