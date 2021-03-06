import wx
import wx.grid
import random
from wx import Colour, ALPHA_OPAQUE

from Busquedas import *
from tkinter import messagebox

SIZE = 45


class GridFrame(wx.Frame):
    def __init__(self, parent, obstaculos):
        wx.Frame.__init__(self, parent)
        self.Bind(wx.EVT_KEY_DOWN, self.graficar)
        self.celdas = None
        self.dic = {}
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
        self.visitados = bfs([self.celdas[0]], self.celdas[1], [], self.celdas[2], self.dic)
        if len(self.visitados) == 0:
            messagebox.showinfo('Error', 'No hay solucion')

    def exec_dfs(self):
        self.visitados = dfs([self.celdas[0]], self.celdas[1], [], self.celdas[2], self.dic)
        if len(self.visitados) == 0:
            messagebox.showinfo('Error', 'No hay solucion')

    def exec_greedy(self):
        self.visitados = greedy([self.celdas[0]], [], self.celdas[1],  self.celdas[2], self.dic)
        if len(self.visitados) == 0:
            messagebox.showinfo('Error', 'No hay solucion')

    def exec_a_star(self):
        obs = []
        for item in self.celdas[2]:
            obs.append(Nodo(item[0], item[1]))
        self.visitados = a_star([Nodo(self.celdas[0][0], self.celdas[0][1])], [], Nodo(self.celdas[1][0], self.celdas[1][1]), obs, self.dic)
        if len(self.visitados) == 0:
            messagebox.showinfo('Error', 'No hay solucion')

    def cambiar_color(self, celda):
        self.grid.SetCellBackgroundColour(celda[0], wx.YELLOW)

    def graficar(self, e):
        if type(self.visitados[0]) != Nodo:
            self.visitados.pop(0)
        self.visitados.pop()
        for celda in self.visitados:
            if type(celda) == Nodo:
                self.grid.SetCellBackgroundColour(celda.x, celda.y, wx.YELLOW)
            else:
                self.grid.SetCellBackgroundColour(celda[0], celda[1], wx.YELLOW)
            self.grid.Update()
            self.grid.ForceRefresh()

        camino = []
        if type(self.celdas[0]) == Nodo:
            inicio = (self.celdas[0].x, self.celdas[0].y)
            meta = (self.celdas[1].x, self.celdas[1].y)
        else:
            inicio = self.celdas[0]
            meta = self.celdas[1]
        actual = meta

        if type(self.dic.get(actual)) != Nodo:
            while actual != inicio:
                actual = self.dic.get(actual)
                camino.append(actual)

        for item in reversed(camino):
            if item != inicio:
                if type(item) == Nodo:
                    self.grid.SetCellBackgroundColour(item.x, item.y, Colour(0, 0, 255, alpha=ALPHA_OPAQUE))
                else:
                    self.grid.SetCellBackgroundColour(item[0], item[1], Colour(0, 0, 255, alpha=ALPHA_OPAQUE))
                self.grid.Update()
                self.grid.ForceRefresh()
