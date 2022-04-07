from os import utime
from tkinter import *
from tkinter import font

#Probabilitas pelayan (server) sibuk/Utilitas sistem
def Utilitas(x, y):
    nilaiLambda = float(x)
    nilaiMiu = float(y)
    U = nilaiLambda/nilaiMiu
    entry7.delete(0, END)
    entry7.insert(0, U)
    return U
#Probabilitas tidak ada pelanggan dalam sistem atau sistem menganggur
def P0(x, y):
    x = float(x)
    y = float(y)
    nilaiP0 = float(1 - (Utilitas(x, y)))
    entry6.delete(0, END)
    entry6.insert(0, nilaiP0)
    return nilaiP0
#Probabilitas n pelanggan dalam sistem
def Pn(x, y, n):
    nilaiLambda = float(x)
    nilaiMiu = float(y)
    jumlahPelanggan = float(n)
    nilaiPn = float((Utilitas(nilaiLambda, nilaiMiu)**jumlahPelanggan) * P0(nilaiLambda, nilaiMiu))
    entry0.delete(0, END)
    entry0.insert(0, nilaiPn)
    return nilaiPn
#Jumlah rata-rata dalam sistem (L)
def L(x, y):
    nilaiLambda = float(x)
    nilaiMiu = float(y)
    nilaiL = nilaiLambda/(nilaiMiu-nilaiLambda)
    entry5.delete(0, END)
    entry5.insert(0, nilaiL)
    return nilaiL
#Waktu rata-rata dalam sistem (Lq)
def Lq(x, y):
    x = float(x)
    y = float(y)
    nilaiLq = float(L(x, y)*Utilitas(x, y))
    entry3.delete(0, END)
    entry3.insert(0, nilaiLq)
    return nilaiLq
#Jumlah rata-rata dalam antrian (W)
def W(x, y):
    nilaiLambda = float(x)
    nilaiMiu = float(y)
    nilaiW = float(L(nilaiLambda, nilaiMiu)/nilaiLambda)
    entry4.delete(0, END)
    entry4.insert(0, nilaiW)
    return nilaiW
#Waktu rata-rata dalam antrian (Wq)
def Wq(x, y):
    x = float(x)
    y = float(y)
    nilaiWq = float(W(x, y)*Utilitas(x, y))
    entry2.delete(0, END)
    entry2.insert(0, nilaiWq)
    return nilaiWq


window = Tk()

window.geometry("1000x800")
window.configure(bg = "#ffffff")
window.title("Kalkulator M/M/1")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 800,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/background.png")
background = canvas.create_image(
    499.5, 400.0,
    image=background_img)

img0 = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:[
        Utilitas(entry9.get(),entry8.get()),
        P0(entry9.get(),entry8.get()),
        L(entry9.get(),entry8.get()),
        Lq(entry9.get(),entry8.get()),
        W(entry9.get(),entry8.get()),
        Wq(entry9.get(),entry8.get()),
        Pn(entry9.get(),entry8.get(),entry1.get()),
    ],
    relief = "flat")

b0.place(
    x = 303, y = 685,
    width = 375,
    height = 50)

entry0_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox0.png")
entry0_bg = canvas.create_image(
    725.0, 641.0,
    image = entry0_img)
#Probabilitas n pelanggan dalam sistem
entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry0.place(
    x = 555.0, y = 616,
    width = 340.0,
    height = 48)

entry1_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox1.png")
entry1_bg = canvas.create_image(
    275.0, 641.0,
    image = entry1_img)
#Jumlah pelanggan n
entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry1.place(
    x = 105.0, y = 616,
    width = 340.0,
    height = 48)

entry2_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox2.png")
entry2_bg = canvas.create_image(
    725.0, 502.0,
    image = entry2_img)
#waktu rata-rata dalam antrian
entry2 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry2.place(
    x = 555.0, y = 477,
    width = 340.0,
    height = 48)

entry3_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox3.png")
entry3_bg = canvas.create_image(
    275.0, 502.0,
    image = entry3_img)
#Waktu rata-rata dalam sistem
entry3 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry3.place(
    x = 105.0, y = 477,
    width = 340.0,
    height = 48)

entry4_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox4.png")
entry4_bg = canvas.create_image(
    725.0, 414.0,
    image = entry4_img)
#Jumlah rata-rata dalam antrian (W)
entry4 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry4.place(
    x = 555.0, y = 389,
    width = 340.0,
    height = 48)

entry5_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox5.png")
entry5_bg = canvas.create_image(
    275.0, 414.0,
    image = entry5_img)
#jumlah rata-rata dalam sistem (L)
entry5 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry5.place(
    x = 105.0, y = 389,
    width = 340.0,
    height = 48)

entry6_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox6.png")
entry6_bg = canvas.create_image(
    725.0, 326.0,
    image = entry6_img)
#Probabilitas sistem menganggur (P0)
entry6 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry6.place(
    x = 555.0, y = 301,
    width = 340.0,
    height = 48)

entry7_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox7.png")
entry7_bg = canvas.create_image(
    275.0, 326.0,
    image = entry7_img)
#Utilitas sistem (U)
entry7 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry7.place(
    x = 105.0, y = 301,
    width = 340.0,
    height = 48)

entry8_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox8.png")
entry8_bg = canvas.create_image(
    725.0, 182.0,
    image = entry8_img)
#Jumlah pelayanan (miu)
entry8 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry8.place(
    x = 555.0, y = 157,
    width = 340.0,
    height = 48)

entry9_img = PhotoImage(file = f"d:/Matkul/Sistem Antrian/coding/app MM1/Proxlight_Designer_Export/img_textBox9.png")
entry9_bg = canvas.create_image(
    275.0, 182.0,
    image = entry9_img)
#Jumlah kedatangan (lambda)
entry9 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Cambria 18',
    highlightthickness = 0)

entry9.place(
    x = 105.0, y = 157,
    width = 340.0,
    height = 48)

window.resizable(False, False)
window.mainloop()
