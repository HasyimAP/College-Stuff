import tkinter as tk
import math
from tkinter import Button, Entry, Place, font
from tkinter.constants import ANCHOR, LEFT, RIGHT

def rumus(x, y):
    N = int(x)
    A = int(y)
    penyebut = 0

    #pembilang
    pembilang = (A**N)/(math.factorial(N))

    #penyebut
    for a in range(0, N+1):
        penyebut += (A**a)/(math.factorial(a))

    hasil = pembilang/penyebut

    labelHasil['text'] = hasil

root = tk.Tk()

canvas = tk.Canvas(root, height=300, width=300)
canvas.pack()

#frame 1
frame1 = tk.Frame(root, bg="#00e6e6")
frame1.place(relx=0.1, rely=0.05, relheight=0.5, relwidth=0.8)

labelN = tk.Label(frame1, text='Jumlah Sirkit (N): ', bg='#00e6e6', anchor='w')
labelN.place(relx=0, rely=0, relheight=0.25, relwidth=1)

entryN = tk.Entry(frame1, bd=5)
entryN.place(relx=0.75, rely=0, relheight=0.25, relwidth=0.25)

labelA = tk.Label(frame1, text='Jumlah trafic yg ditawarkan (A): ', bg='#00e6e6', anchor='w')
labelA.place(relx=0, rely=0.4, relheight=0.25, relwidth=1)

entryA = tk.Entry(frame1, bd=5)
entryA.place(relx=0.75, rely=0.4, relheight=0.25, relwidth=0.25)

tombol = tk.Button(frame1, text='Calculate', command=lambda: rumus(entryN.get(),entryA.get()))
tombol.place(relx=0.35, rely=0.7, relheight=0.25, relwidth=0.3)

#frame 2
frame2 = tk.Frame(root, bg="#00e6e6", bd=5)
frame2.place(relx=0.1, rely=0.6, relheight=0.3, relwidth=0.8)

labelPN = tk.Label(frame2, text='Probabilitas Blocking', bg='#00e6e6')
labelPN.place(relheight=0.2, relwidth=1)

labelHasil = tk.Label(frame2, font=40)
labelHasil.place(rely=0.25, relheight=0.75, relwidth=1)

root.mainloop()