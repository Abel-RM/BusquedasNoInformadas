from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from Tablero import *

window = Tk()
window.title("Busquedas no informadas")
window.geometry('300x250')
combo = Combobox(window)


def clicked():
    nombre_busqueda = combo.get()

    try:
        obstaculos = int(spin.get())
        app = wx.App(0)
        if nombre_busqueda == 'BFS' and 0 < obstaculos <= 80:
            tablero = GridFrame(None, obstaculos)
            tablero.exec_bfs()
            app.MainLoop()

        elif nombre_busqueda == 'DFS' and 0 < obstaculos <= 80:
            tablero = GridFrame(None, obstaculos)
            tablero.exec_dfs()
            app.MainLoop()
        elif nombre_busqueda == 'Greedy' and 0 < obstaculos <= 80:
            tablero = GridFrame(None, obstaculos)
            tablero.exec_greedy()
            app.MainLoop()
        elif nombre_busqueda == 'A*' and 0 < obstaculos <= 80:
            tablero = GridFrame(None, obstaculos)
            tablero.exec_a_star()
            app.MainLoop()
        else:
            messagebox.showinfo('Error', 'Opciones invalidas')

    except ValueError:
        messagebox.showinfo('Error', 'Opciones invalidas')


if __name__ == '__main__':
    combo['values'] = ('BFS', 'DFS', 'Greedy', 'A*')
    combo.grid(column=0, row=0, padx=80, pady=10)
    spin = Spinbox(window, from_=1, to=80, width=5)
    spin.set(5)
    spin.grid(column=0, row=4, pady=10)
    btn = Button(window, text="Aceptar", command=clicked)
    btn.grid(column=0, row=6, pady=10)
    window.mainloop()
