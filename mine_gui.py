#!/usr/bin/python3

from mine import mine
from tkinter import *

GAMENAME = '扫雷'

class mine_gui():
    def __init__(self, row = 9, column = 9, mineNum = 10):
        #-------- common init -----------------------------
        self.root = Tk()
        self.root.resizable(width = False, height = False)
        self.root.iconbitmap('res\\16X16.ico')
        self.root.title(GAMENAME)
        
        self.everyGridWidth = 16
        self.everyGridHeight = 16
        
        closeBitmap = PhotoImage(file = r'res/close.gif')
        flagBitmap = PhotoImage(file = r'res/flag.gif')
        quesBitmap = PhotoImage(file = r'res/question.gif')
        mineBitmap = PhotoImage(file = r'res/mine.gif')
        flagerrBitmap = PhotoImage(file = r'res/flagerr.gif')

        self.closeBitmap = {'Running':[closeBitmap, flagBitmap, quesBitmap],
                            'Win':[flagBitmap, flagBitmap, flagBitmap],
                            'Over':[[closeBitmap, mineBitmap], [flagerrBitmap, flagBitmap], [quesBitmap, mineBitmap]]}

        self.openBitmap = []
        for i in range(10):
            thisBitmap = PhotoImage(file = r'res/open' + str(i) + r'.gif')
            self.openBitmap.append(thisBitmap)

        self.AppStatus = 'Running'
        #--------------------------------------------------

        self.mine = mine(row, column, mineNum)

        self.allGridWidth = self.everyGridWidth * self.mine.column
        self.allGridHeight = self.everyGridHeight * self.mine.row

        self.currXY = None

        self.frame1 = Frame(self.root)
        self.frame1.pack()
        self.button = Button(self.frame1, text = 'reset', command = self.Reset)
        self.button.pack()

        self.frame2 = Frame(self.root)
        self.frame2.pack()

        self.canvas = Canvas(self.frame2, bg = 'Silver',
            width = self.allGridWidth, height = self.allGridHeight)
        self.canvas.pack()
        
        self.canvas.bind('<Button-1>', self.funcButtonL)
        self.canvas.bind('<B1-Motion>', self.funcButtonL)
        self.canvas.bind('<ButtonRelease-1>', self.funcButtonReleaseL)
        self.canvas.bind('<Button-3>', self.funcButtonR2)
        self.canvas.bind('<B3-Motion>', self.funcButtonR)
        self.canvas.bind('<ButtonRelease-3>', self.funcButtonReleaseR)
        self.DrawInit()
        self.Draw()

        self.root.mainloop()

    def Reset(self):
        row = self.mine.row
        column = self.mine.column
        numMine = self.mine.mineNum
        self.mine = mine(row, column, numMine)
        self.AppStatus = 'Running'
        self.currXY = None
        self.Draw()

    def funcButtonL(self, event):
        if self.AppStatus != 'Running': return
        position = self.GetPosition(event.x-2, event.y-2)
        if position == self.currXY: return
        self.currXY = position
        
        self.Draw((position,))

    def funcButtonR2(self, event):
        if self.AppStatus != 'Running': return
        position = self.GetPosition(event.x-2, event.y-2)
        if position == None: return
        if self.mine.IsOpen(position[0], position[1]):
            self.funcButtonR(event)
        else:
            self.currXY = position
            self.mine.SetFlag(position[0], position[1])
            self.Draw()

    def funcButtonR(self, event):
        if self.AppStatus != 'Running': return
        position = self.GetPosition(event.x-2, event.y-2)
        if position == self.currXY: return
        self.currXY = position
        
        row = position[0]
        column = position[1]
        
        AllPosition = []
        for i in range(row-1, row+2):
            for j in range(column-1, column+2):
                AllPosition.append((i, j))
        self.Draw(tuple(AllPosition))

    def funcButtonReleaseL(self, event):
        if self.AppStatus != 'Running': return
        self.currXY = None
        position = self.GetPosition(event.x-2, event.y-2)
        if position == None: return

        row = position[0]
        column = position[1]

        if self.mine.IsOpen(row, column):
            self.mine.OpenR(row, column)
        else:
            self.mine.Open(row, column)

        self.AppStatus = self.mine.WinOver()
        self.Draw()

    def funcButtonReleaseR(self, event):
        if self.AppStatus != 'Running': return
        self.currXY = None
        position = self.GetPosition(event.x-2, event.y-2)
        if position == None: return

        row = position[0]
        column = position[1]

        if self.mine.IsOpen(row, column):
            self.mine.OpenR(row, column)

        self.AppStatus = self.mine.WinOver()
        self.Draw()

    def drawGrid(self, row, clomn, bitmap, name = 'Grid'):
        thisGridX = clomn * self.everyGridWidth + 2 + 8
        thisGridY = row * self.everyGridHeight + 2 + 8
        self.canvas.create_image(thisGridX, thisGridY, image = bitmap,
                                 tags = name)

    def DrawInit(self):
        bitmap = self.openBitmap[0]
        for i in range(self.mine.row):
            for j in range(self.mine.column):
                self.drawGrid(i, j, bitmap, 'Init')

    def Draw(self, op = ()):
        self.canvas.delete('Grid')
        
        bitmap = None
        status = self.closeBitmap[self.AppStatus]
        
        for i in range(self.mine.row):
            for j in range(self.mine.column):
                CurrStatus = self.mine.GetOneStatus(i, j)
                CurrData = self.mine.GetOneData(i, j)

                if CurrStatus == 0:
                    if (i, j) in op: continue

                if CurrStatus == 10:
                    CurrData = self.mine.GetOneData(i, j)
                    bitmap = self.openBitmap[CurrData]
                else:
                    if self.AppStatus == 'Over':
                        if CurrData == 9: bitmap = status[CurrStatus][1]
                        else: bitmap = status[CurrStatus][0]
                    else:
                        bitmap = status[CurrStatus]
                self.drawGrid(i, j, bitmap)

    def GetPosition(self, x, y):
        row = y // self.everyGridHeight
        if row not in range(self.mine.row): return None
        column = x // self.everyGridWidth
        if column not in range(self.mine.column): return None
        return (row, column)

mine_gui()
