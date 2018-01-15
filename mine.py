#!/usr/bin/python3

'''
data  | 0 1 2 3 4 5 6 7 8 9 -- number
---------------------------------
status:
     0 close
     1 flag
     2 question
    10 open
'''

import random

class mine:
    def __init__(self, row = 9, column = 9, mineNum = 10):
        self.row = row
        self.column = column
        self.mineNum = mineNum

        self.init = True
        
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
        self.SetAllAuto()
        self.backNum = random.choice(temp)

        self.status = []
        for i in range(self.row):
            self.status.append([])
            for j in range(self.column):
                self.status[i].append(0)  # set close

    def WinOver(self):
        status = []
        for i in range(self.row):
            for j in range(self.column):
                if self.IsOpen(i, j):
                    status.append(self.GetOneData(i, j))
        if 9 in status: return 'Over'
        if len(status) == (self.row * self.column - self.mineNum):
                return 'Win'
        return 'Running'

    def Open(self, row, column):
        if not self.Check(row, column): return
        if self.IsOpen(row, column): return
        if self.GetOneStatus(row, column) == 1: return

        if self.init:
            self.init = False
            firstData = self.GetOneData(row, column)
            if firstData == 9:
                self.SetOneData(row, column, 0)
                ch = self.backNum
                self.data[ch // self.row][ch % self.column] = 9
                self.SetAllAuto()
        
        self.SetOpen(row, column)
        CurrData = self.GetOneData(row, column)
        if CurrData == 0:
            for i in range(row-1, row+2):
                for j in range(column-1, column+2):
                    self.Open(i, j)
                    
    def OpenR(self, row, column):
        if not self.Check(row, column): return
        if not self.IsOpen(row, column): return

        temp = 0
        for i in range(row-1,row+2):
            if i not in range(self.row): continue
            for j in range(column-1, column+2):
                if j not in range(self.column): continue
                if i == row and j == column: continue
                if self.GetOneStatus(i, j) == 1: temp = temp + 1
        if self.GetOneData(row, column) == temp:
            for i in range(row-1, row+2):
                for j in range(column-1, column+2):
                    self.Open(i, j)

    def SetFlag(self, row, column):
        if not self.Check(row, column): return
        if self.IsOpen(row, column): return

        CurrStatus = self.GetOneStatus(row, column)
        temp = (CurrStatus + 1) % 3
        self.SetOneStatus(row, column, temp)
            
    def Check(self, row, column):
        if row not in range(self.row): return False
        if column not in range(self.column): return False
        return True
    
    def GetOneData(self, row, column):
        return self.data[row][column]
    def SetOneData(self, row, column, data):
        self.data[row][column] = data
    def GetOneStatus(self, row, column):
        return self.status[row][column]
    def SetOneStatus(self, row, column, status):
        self.status[row][column] = status
    def SetOpen(self, row, column):
        self.status[row][column] = 10
    def IsOpen(self, row, column):
        return self.status[row][column] == 10

    def SetOneAuto(self, row, column):
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

    def SetAllAuto(self):
        for i in range(self.row):
            for j in range(self.column):
                self.SetOneAuto(i, j)

    def Show(self):
        for i in range(self.row):
            for j in range(self.column):
                print('%2d' % self.data[i][j], end = ' ')
            print(' ** ', end = ' ')
            for j in range(self.column):
                print('%2d' % self.status[i][j], end = ' ')
            print()

if __name__ == '__main__':
    a = mine()
    a.Show()













        
