#!/usr/bin/python3

'''
status:
     0 close_nothing
     1 flag
     2 query
     ----------
     9 open
'''

import random
from mine_bottom import mine_bottom

DATA_UNKNOW = 10

STATUS_CLOSE_NOTHING = 0
STATUS_FLAG = 1
STATUS_QUERY = 2
STATUS_OPEN = 9

class mine_top(mine_bottom):
    def __init__(self, row = 9, column = 9, mineNum = 10):
        self.mine_base = mine_bottom(row, column, mineNum)

    def FirstTimeOpen(self, row, column):
        if self.Open(row, column):
            self.mine_base.FirstIsMine(row, column)
            return True
        return False

    def Open(self, row, column):
        if self.IsOpen(row, column): return False
        if self.IsFlag(row, column): return False
        self.mine_base.SetOneStatus(row, column, STATUS_OPEN)
        return True

    def SetFlag(self, row, column, status):
        if self.IsOpen(row, column): return False
        self.mine_base.SetOneStatus(row, column, status)
        return True

    def GetOneStatus(self, row, column):
        return self.mine_base.GetOneStatus(row, column)
    def GetOneData(self, row, column):
        if self.IsOpen(row, column): return self.mine_base.GetOneData(row, column)
        else return DATA_UNKNOW
    def IsOpen(self, row, column):
        return self.mine_base.GetOneStatus(row, column) == STATUS_OPEN
    def IsFlag(self, row, column):
        return self.mine_base.GetOneStatus(row, column) == STATUS_FLAG

    def Show(self): self.mine_base.Show()

if __name__ == '__main__':
    a = mine_top(20, 20, 20)
    a.Show()

