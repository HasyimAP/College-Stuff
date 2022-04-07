import tkinter as tk
import math
from typing import Text

def rumus_engset(a, s, n):
    A = float(a)
    S = int(s)
    N = int(n)

    #pembilang
    pembilang = ((A**N)/math.factorial(N))*(math.factorial(S)/math.factorial(S-N))

    #penyebut
    penyebut = 0
    for x in range(0, N+1):
        penyebut = penyebut + (((A**x)/math.factorial(x))*(math.factorial(S)/math.factorial(S-x)))
        print(penyebut)
    
    hasil = pembilang/penyebut

    labelHasil['text'] = hasil

root = tk.Tk()

canvas = tk.Canvas(root, height=300, width=400)
canvas.pack()

#frame 1
frame1 = tk.Frame(root, bg='#4080bf', bd=5)
frame1.place(relx=0.1, rely=0.1, relheight=0.5, relwidth=0.8)

label1 = tk.Label(frame1, text='Traffic yang ditawarkan (A)\t\t:', bg='#4080bf', anchor='e')
label1.place(relx=0, rely=0, relheight=0.2, relwidth=0.69)

entryA = tk.Entry(frame1, bd=2)
entryA.place(relx=0.7, rely=0, relheight=0.2, relwidth=0.3)

label2 = tk.Label(frame1, text='Sumber traffic (S)\t\t:', bg='#4080bf', anchor='e')
label2.place(relx=0, rely=0.3, relheight=0.2, relwidth=0.69)

entryS = tk.Entry(frame1, bd=2)
entryS.place(relx=0.7, rely=0.3, relheight=0.2, relwidth=0.3)

label3 = tk.Label(frame1, text='Jumlah sirkuit (N)\t\t:', bg='#4080bf', anchor='e')
label3.place(relx=0, rely=0.6, relheight=0.2, relwidth=0.69)

entryN = tk.Entry(frame1, bd=2)
entryN.place(relx=0.7, rely=0.6, relheight=0.2, relwidth=0.3)

tombol = tk.Button(frame1, text='Calculate', command=lambda: rumus_engset(entryA.get(), entryS.get(), entryN.get()))
tombol.place(relx=0.3, rely=0.85, relheight=0.15, relwidth=0.4)

#frame 2
frame2 = tk.Frame(root, bg='#4080bf', bd=5)
frame2.place(relheight=0.3, relwidth=0.8, relx=0.1, rely=0.65)

labelP = tk.Label(frame2, text='Probabilitas Blocking', bg='#4080bf')
labelP.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0)

labelHasil = tk.Label(frame2, font=40)
labelHasil.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.25)

root.mainloop()