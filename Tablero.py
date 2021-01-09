import wx
import wx.grid
import random
from Busquedas import *
from tkinter import messagebox

SIZE = 45


class GridFrame(wx.Frame):
    def __init__(self, parent, obstaculos):
        wx.Frame.__init__(self, parent)
        self.Bind(wx.EVT_KEY_DOWN, self.graficar)
        self.celdas = None
        self.grid = wx.grid.Grid(self, -1)
        self.visitados = []
        self.grid.CreateGrid(SIZE, SIZE)
        self.grid.HideColLabels()
        self.grid.HideRowLabels()
        self.grid.DisableCellEditControl()
        for i in range(SIZE):
            self.grid.DisableColResize(i)
            self.grid.SetColSize(i, 15)
            self.grid.SetRowSize(i, 15)
            for j in range(SIZE):
                self.grid.SetReadOnly(i, j)
                self.grid.DisableRowResize(j)
        # And set grid cell contents as strings
        # grid.SetCellValue(0, 0, 'wxGrid is good')

        # Colours can be specified
        # grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)

        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        # grid.SetColFormatFloat(5, 6, 2)
        # grid.SetCellValue(0, 6, '3.1415')
        self.Show()
        self.celdas = self.elegir_celdas(obstaculos)

    def elegir_celdas(self, cantidad_obstaculos):
        num = (cantidad_obstaculos / 100) * (SIZE ** 2)
        x = random.randrange(SIZE)
        y = random.randrange(SIZE)
        inicio = (x, y)
        self.grid.SetCellBackgroundColour(x, y, wx.GREEN)

        x = random.randrange(SIZE)
        y = random.randrange(SIZE)
        meta = (x, y)
        self.grid.SetCellBackgroundColour(x, y, wx.RED)
        obstaculos = []
        index = 0
        while index < num:
            x = random.randrange(SIZE)
            y = random.randrange(SIZE)
            coor = (x, y)
            if coor not in obstaculos and coor != inicio and coor != meta:
                obstaculos.append(coor)
                index += 1
        for item in obstaculos:
            self.grid.SetCellBackgroundColour(item[0], item[1], wx.BLACK)

        return [inicio, meta, obstaculos]

    def exec_bfs(self):
        self.visitados = bfs([self.celdas[0]], self.celdas[1], [], self.celdas[2])
        if len(self.visitados) == 0:
            messagebox.showinfo('Error', 'No hay solucion')

    def exec_dfs(self):
        self.visitados = dfs([self.celdas[0]], self.celdas[1], [], self.celdas[2])
        if len(self.visitados) == 0:
            messagebox.showinfo('Error', 'No hay solucion')

    def exec_gredy(self):
        self.visitados = gredy([self.celdas[0]], self.celdas[1], [])

    def exec_a_star(self):
        self.visitados = a_star([self.celdas[0]], self.celdas[1], [])

    def cambiar_color(self, celda):
        self.grid.SetCellBackgroundColour(celda[0], wx.YELLOW)

    def graficar(self, e):
        self.visitados.pop(0)
        self.visitados.pop()
        for celda in self.visitados:
            self.grid.SetCellBackgroundColour(celda[0], celda[1], wx.YELLOW)
            self.Refresh()
            self.grid.Update()
