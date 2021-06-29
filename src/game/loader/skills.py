# -*- coding: utf-8 -*-

from definition import *

# Skill(self, name, pp, range, senders, targets, affectSender, affectTarget)

# Same Skill
def init_hit(senders, targets):
    def affectSender(mob):
        mob.pp -= 0
        
    def affectTarget(mob):
        mob.hp -= 3
        
    return Skill('撞击', 0, '单个对象', senders, targets, affectSender, affectTarget)

# Player Skill

# Enemy Skill

__all__ = ['init_hit']