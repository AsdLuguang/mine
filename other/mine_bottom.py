#!/usr/bin/python3

'''
data  | 0 1 2 3 4 5 6 7 8 -- number
      | 9 -- mine
'''

import random

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

    def GetOneData(self, row, column):
        if not self.check(row, column): return
        if self.init:
            self.init = False
            firstData = self.get_one_data(row, column)
            if firstData == 9:
                self.set_one_data(row, column, 0)
                ch = self.backNum
                self.data[ch // self.row][ch % self.column] = 9
                self.set_all_auto()

        return self.get_one_data(row, column)
    
    def SetOneData(self, row, column, data):
        if not self.check(row, column): return
        self.set_one_data(row, column, data)

    def get_one_data(self, row, column):
        return self.data[row][column]
    def set_one_data(self, row, column, data):
        self.data[row][column] = data
    def set_one_auto(self, row, column):
        #if not self.Check(row, column): return
        CurrData = self.get_one_data(row, column)
        if CurrData == 9: return
        temp = 0
        for i in range(row-1, row+2):
            if i not in range(self.row): continue
            for j in range(column-1, column+2):
                if j not in range(self.column): continue
                if self.get_one_data(i, j) == 9: temp = temp + 1
        self.set_one_data(row, column, temp)
    def set_all_auto(self):
        for i in range(self.row):
            for j in range(self.column):
                self.set_one_auto(i, j)

    def Show(self):
        for i in range(self.row):
            for j in range(self.column):
                print('%2d' % self.get_one_data(i, j), end = ' ')
            print()

if __name__ == '__main__':
    a = mine_bottom(20, 20, 20)
    a.Show()

