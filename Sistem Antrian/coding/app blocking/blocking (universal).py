import math


A = int(input("Intensitas Trafik (A): "))
N = int(input("Jumlah Saluran (N): "))
penyebut = 0.00

for i in range(0,N+1):
    penyebut += (A**(i/math.factorial(i)))
    print(penyebut)

Bc = (A**(N/math.factorial(N)))/penyebut
print("Hasil = ", Bc)
R = A*Bc
print("Traffic loss = ",R)