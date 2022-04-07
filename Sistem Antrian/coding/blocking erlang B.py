import math

N = int(input("Jumlah sirkit (N): "))
A = int(input("Jumlah trafic yg ditawarkan (A): "))
penyebut = 0

#pembilang
pembilang = (A**N)/(math.factorial(N))

#penyebut
for a in range(0, N+1):
    penyebut += (A**a)/(math.factorial(a))

hasil = pembilang/penyebut
print("Probabilitas blocking=",pembilang,"/",penyebut,"=", hasil)

