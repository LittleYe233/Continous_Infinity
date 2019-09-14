# -*- coding: utf-8 -*-

import sys; sys.path.append('..')
import mob
import skill
import item

# Get object list
mobList = list(map(lambda x: eval('mob.{}'.format(x)), mob.__all__))
skillList = list(map(lambda x: eval('skill.{}'.format(x)), skill.__all__))
itemList = list(map(lambda x: eval('item.{}'.format(x)), item.__all__))