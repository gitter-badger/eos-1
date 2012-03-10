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


from eos.dataHandler.exception import ExpressionFetchError
from eos.util.callableData import CallableData


class DataHandler:

    def __init__(self, expressionData):
        self.__expressionData = expressionData

    def getExpression(self, expId):
        try:
            expression = self.__expressionData[expId]
        except KeyError:
            raise ExpressionFetchError(expId)
        return expression


def callize(expression):
    dataHandler = DataHandler({expression.id: expression})
    return CallableData(callable=dataHandler.getExpression, args=(expression.id,), kwargs={})
