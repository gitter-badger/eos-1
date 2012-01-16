#===============================================================================
# Copyright (C) 2011 Diego Duclos
# Copyright (C) 2011-2012 Anton Vorobyov
#
# This file is part of Eos.
#
# Eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Eos. If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from eos import const
from eos.calc.mutableAttributeHolder import MutableAttributeHolder

class Skill(MutableAttributeHolder):

    @property
    def location(self):
        return const.locChar

    def __init__(self, invType):
        super().__init__(invType)

    @property
    def level(self):
        level = self.attributes[const.attrSkillLevel]
        return level

    @level.setter
    def level(self, value):
        self.attributes[const.attrSkillLevel] = value
