#Probabilitas pelayan (server) sibuk/Utilitas sistem
def Utilitas(x, y):
    nilaiLambda = x
    nilaiMiu = y
    U = nilaiLambda/nilaiMiu
    return U
#Probabilitas tidak ada pelanggan dalam sistem atau sistem menganggur
def P0(x, y):
    nilaiP0 = 1 - (Utilitas(x, y))
    return nilaiP0
#Probabilitas n pelanggan dalam sistem
def Pn(x, y, n):
    nilaiLambda = x
    nilaiMiu = y
    jumlahPelanggan = n
    nilaiPn = (Utilitas(nilaiLambda, nilaiMiu)**jumlahPelanggan) * P0(nilaiLambda, nilaiMiu)
    return nilaiPn
#Jumlah rata-rata dalam sistem
def L(x, y):
    nilaiLambda = x
    nilaiMiu = y
    nilaiL = nilaiLambda/(nilaiMiu-nilaiLambda)
    return nilaiL
#Waktu rata-rata dalam sistem
def Lq(x, y):
    nilaiLq = L(x, y)*Utilitas(x, y)
    return nilaiLq
#Jumlah rata-rata dalam antrian
def W(x, y):
    nilaiLambda = x
    nilaiMiu = y
    nilaiW = L(nilaiLambda, nilaiMiu)/nilaiLambda
    return nilaiW
#Waktu rata-rata dalam antrian
def Wq(x, y):
    nilaiWq = W(x, y)*Utilitas(x, y)
    return nilaiWq
#input
inputLambda = int(input("Nilai Lambda\t: "))
inputMiu = int(input("Nilai Miu\t: "))
#output
print("\nUtilitas sistem\t\t\t: ", Utilitas(inputLambda,inputMiu))
print("Jumlah rata-rata dalam sistem\t: ", L(inputLambda, inputMiu))
print("Waktu rata-rata dalam sistem\t: ", Lq(inputLambda, inputMiu))
print("Jumlah rata-rata dalam antrian\t: ", W(inputLambda, inputMiu))
print("Waktu rata-rata dalam antrian\t: ", Wq(inputLambda, inputMiu))