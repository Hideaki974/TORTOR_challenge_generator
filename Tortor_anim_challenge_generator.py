# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import random


Emo_list = ['fear', 'anger', 'joy', 'sad', 'under speedy drugs', 'under slowly drugs', 'happy', 'laugh', 'curious', 'confused', 'embarrased', 'nervous', 'tired', 'shocked', 'disgusted']
Act_list = ['boxe', 'fight prepare', 'try to catch', 'jump', 'heavy object', 'run', 'walk', 'dance', 'play guitar', 'play drum', 'skateboarding', 'resting', 'drinking', 'meditate']
Env_list = ['ice place', 'forest', 'hill', 'desert', 'city street', 'on a boat', 'in a car', 'under the sea', 'on the moon', 'in a volcano', 'on a box', 'on bar counter']
oEmo_select = random.choice(Emo_list)
oAct_select = random.choice(Act_list)
oEnv_select = random.choice(Env_list)

print('For the animation challenge:\n - the Choosen Emotion is {}\n - the Choosen Action is {}\n - the Choosen environement is {}'.format(oEmo_select, oAct_select, oEnv_select))
