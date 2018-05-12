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

bl_info = {
    "name": "TORTOR_TOOLS",
    "author": "Pierre Fontaine",
    "version": (0, 1),
    "blender": (2, 79, 0),
    "location": "Tools",
    "description": "Set of TORTOR_TOOLS for blender",
    "warning": "experimental state",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Animation"}


import bpy
from bpy.types import Panel, Operator
import random
# import os
# import csv
# import string

class generate_theme(bpy.types.Operator):
    bl_label = "generate_Operator"
    bl_idname = "generate.theme"
    def execute(self,context):
        bpy.ops.object.delete(use_global=False)
        Emo_list = ['fear', 'anger', 'joy', 'sad', 'under speedy drugs', 'under slowly drugs', 'happy', 'laugh', 'curious', 'confused', 'embarrased', 'nervous', 'tired', 'shocked', 'disgusted']
        Act_list = ['boxe', 'fight prepare', 'try to catch', 'jump', 'heavy object', 'run', 'walk', 'dance', 'play guitar', 'play drum', 'skateboarding', 'resting', 'drinking', 'meditate']
        Env_list = ['ice place', 'forest', 'hill', 'desert', 'city street', 'on a boat', 'in a car', 'under the sea', 'on the moon', 'in a volcano', 'on a box', 'on bar counter']
        oEmo_select = random.choice(Emo_list)
        oAct_select = random.choice(Act_list)
        oEnv_select = random.choice(Env_list)
        bpy.ops.mesh.primitive_monkey_add()
        otheme = oEmo_select + '_' + oAct_select + '_' + oEnv_select
        bpy.context.object.name = otheme

        self.report({'INFO'}, 'theme genereted!')
        return {'FINISHED'}

"""Creates a Panel in the toolshellf who generate the animation theme"""
class TORTOR_anim(Panel):
    bl_label = "animation_challenge"
    bl_idname = "AnimGeneratorPannel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "TORTOR"
    bl_contexte = 'objectmode'


    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Ready for it !", icon='WORLD_DATA')
        row = layout.row()
        row.operator("generate.theme", text = 'generate', icon = 'MOD_MASK')




def register():
    bpy.utils.register_class(generate_theme)
    bpy.utils.register_class(TORTOR_anim)


def unregister():
    bpy.utils.unregister_class(generate_theme)
    bpy.utils.unregister_class(TORTOR_anim)


if __name__ == "__main__":
    register()
