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

STATUS_CLOSE_NOTHING = 0
STATUS_FLAG = 1
STATUS_QUERY = 2
STATUS_OPEN = 9

class mine_top(mine_bottom):
    def __init__(self, row = 9, column = 9, mineNum = 10):
        mine_bottom.__init__(self, row, column, mineNum)

        self.status = []
        for i in range(self.row):
            self.status.append([])
            for j in range(self.column):
                self.status[i].append(STATUS_CLOSE_NOTHING)

    def Open(self, row, column):
        if not self.Check(row, column): return False
        if self.IsOpen(row, column): return False
        ''' 这个限制不在一个层次处理 '''
        ''' if self.GetOneStatus(row, column) == STATUS_FLAG: return False '''

        self.SetOneStatus(row, column, STATUS_FLAG)
        return True

    def SetFlag(self, row, column, status):
        if not self.Check(row, column): return False
        if self.IsOpen(row, column): return False
        if status != STATUS_CLOSE_NOTHING and status != STATUS_FLAG and status != STATUS_QUERY:
            return False

        self.SetOneStatus(row, column, status)
        return True

    def GetOneStatus(self, row, column):
        return self.status[row][column]
    def SetOneStatus(self, row, column, status):
        self.status[row][column] = status
    def IsOpen(self, row, column):
        return self.status[row][column] == STATUS_OPEN

    def Show(self):
        mine_bottom.Show(self)
        print("===========================")
        for i in range(self.row):
            for j in range(self.column):
                print('%2d' % self.GetOneStatus(i, j), end = ' ')
            print()

if __name__ == '__main__':
    a = mine_top(20, 20, 20)
    a.Show()

