#!/usr/bin/python3

'''
data  : 0 1 2 3 4 5 6 7 8 -- number
        9 -- mine
status:
     0 close_nothing
     1 flag
     2 query
     ----------
     9 open
'''
import random

STATUS_CLOSE_NOTHING = 0
STATUS_FLAG = 1
STATUS_QUERY = 2
STATUS_OPEN = 9

class mine_bottom:
    def __init__(self, row = 9, column = 9, mineNum = 10):

        if row <= 0 or column <= 0 or mineNum <= 0 or mineNum > row * column:
            row, column, mineNum = 9, 9, 10

        self.row = row
        self.column = column
        self.mineNum = mineNum
        
        self.data = []
        for i in range(self.row):
            self.data.append([])
            for j in range(self.column):
                self.data[i].append(0)

        self.status = []
        for i in range(self.row):
            self.status.append([])
            for j in range(self.column):
                self.status[i].append(STATUS_CLOSE_NOTHING)

        temp = list(range(self.row * self.column))
        for i in range(self.mineNum):
            ch = random.choice(temp)
            self.data[ch // self.row][ch % self.column] = 9
            temp.remove(ch)

        ''' 防止第一次点到雷 '''
        self.backNum = random.choice(temp)
        self.init = True

        self.set_all_auto()

    ''' 检测参数的合法性 '''
    def check(self, row, column):
        if row not in range(self.row): return False
        if column not in range(self.column): return False
        return True

    def FirstIsMine(self, row, column):
        if self.init:
            self.init = False
            firstData = self.GetOneData(row, column)
            if firstData == 9:
                self.SetOneData(row, column, 0)
                ch = self.backNum
                self.data[ch // self.row][ch % self.column] = 9
                self.set_all_auto()
    
    def GetOneData(self, row, column):
        return self.data[row][column]
    def SetOneData(self, row, column, data):
        self.data[row][column] = data
    def GetOneStatus(self, row, column):
        return self.status[row][column]
    def SetOneStatus(self, row, column, status):
        self.status[row][column] = status

    def set_one_auto(self, row, column):
        #if not self.Check(row, column): return
        CurrData = self.GetOneData(row, column)
        if CurrData == 9: return
        temp = 0
        for i in range(row-1, row+2):
            if i not in range(self.row): continue
            for j in range(column-1, column+2):
                if j not in range(self.column): continue
                if self.GetOneData(i, j) == 9: temp = temp + 1
        self.SetOneData(row, column, temp)
    def set_all_auto(self):
        for i in range(self.row):
            for j in range(self.column):
                self.set_one_auto(i, j)

    def Show(self):
        for i in range(self.row):
            for j in range(self.column):
                print('%2d' % self.GetOneData(i, j), end = ' ')
            print()
        print("===========================")
        for i in range(self.row):
            for j in range(self.column):
                print('%2d' % self.GetOneStatus(i, j), end = ' ')
            print()

if __name__ == '__main__':
    a = mine_bottom(20, 20, 20)
    a.Show()

