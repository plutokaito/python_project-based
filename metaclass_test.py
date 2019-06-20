#  -*- coding: utf-8 -*-
import yaml
import warnings

warnings.simplefilter("ignore", yaml.YAMLLoadWarning) ## 当用load出现警告时，用这个可以暂时避免警告

class Monster(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!Monster'
    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks
    def __repr__(self):
        return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)

print(yaml.safe_load("""
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
""")) # the problem is that the default loader for load is now FullLoader, but the YAMLObject still uses yaml.Loader