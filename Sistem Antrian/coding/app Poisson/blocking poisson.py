import tkinter as tk
import math

def blocking_poisson(n,a):
    A = int(a)
    N = int(n)
    
    hasil = ((A**N)/(math.factorial(N)))*math.exp(-A)
    labelHasil['text'] = hasil

root = tk.Tk()

canvas = tk.Canvas(height=300, width=400)
canvas.pack()

#frame 1
frame1 = tk.Frame(root, bg='#33ff33', bd=2)
frame1.place(relx=0.1, rely=0.1, relheight=0.5, relwidth=0.8)

labelN = tk.Label(frame1, text='Jumlah Sirkit (N): ', bg='#33ff33', anchor='w')
labelN.place(relx=0, rely=0, relheight=0.25, relwidth=1)

entryN = tk.Entry(frame1, bd=5)
entryN.place(relx=0.75, rely=0, relheight=0.25, relwidth=0.25)

labelA = tk.Label(frame1, text='Jumlah trafic yg ditawarkan (A): ', bg='#33ff33', anchor='w')
labelA.place(relx=0, rely=0.4, relheight=0.25, relwidth=1)

entryA = tk.Entry(frame1, bd=5)
entryA.place(relx=0.75, rely=0.4, relheight=0.25, relwidth=0.25)

tombol = tk.Button(frame1, text='Calculate', command=lambda: blocking_poisson(entryN.get(),entryA.get()))
tombol.place(relx=0.35, rely=0.7, relheight=0.25, relwidth=0.3)

#frame 2
frame2 = tk.Frame(root, bg='#33ff33', bd=2)
frame2.place(relx=0.1, rely=0.7, relheight=0.2, relwidth=0.8)

labelPN = tk.Label(frame2, text='Probabilitas Blocking', bg='#33ff33')
labelPN.place(relheight=0.3, relwidth=1)

labelHasil = tk.Label(frame2, font=40)
labelHasil.place(rely=0.3, relheight=0.7, relwidth=1)

root.mainloop()