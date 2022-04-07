from array import *
import math

n = 0
i = 1
data = array('i', [])
print("Input data (ketik 0 untuk berhenti menginput)")
while i != 0:
    print("Data ke-",n+1, "= ", end="") 
    x = int(input())
    data.append(x)
    if data[n]==0:
        break
    n = n+1
print("Jumlah data: ", n)
#sorting/pengurutan
sort = False
while not sort:
    sort = True
    for a in range(0, n-1):
        if data[a] > data[a+1]:
            sort = False
            data[a], data[a+1] = data[a+1], data[a]
print("Data setelah diurutkan:")
for a in range(0, n):
    print(data[a], end=" ")
#Hasil penjumlahan semua data
total = 0
for a in range(0, n):
    total += data[a]
print("Total =",total)
#Mean atau Rata-Rata
mean = total/n
print("\nMean =", mean)
#Modus
modus = (0, 0) #(jumlah data, nilai data)
for a in data:
    muncul = data.count(a)
    if muncul>modus[0]:
        modus = (muncul, a)
print("Modus =",modus[1])
#Quartil 1 sampai 3
q1 = (n+1)/4
q2 = (2*(n+1))/4
q3 = (3*(n+1))/4
print("Q1 =",q1," Q2 =", q2," Q3 =", q3)
#Nilai quartil 1 sampai 3
q1b = int(q1)
q2b = int(q2)
q3b = int(q3)
nq1 = int
nq2 = int
nq3 = int
nq1 = data[q1b-1] + ((data[q1b] - data[q1b-1])*(q1-q1b))
nq2 = data[q2b-1] + ((data[q2b] - data[q2b-1])*(q2-q2b))
nq3 = data[q3b-1] + ((data[q3b] - data[q3b-1])*(q3-q3b))
print("Nilai Q1 =", nq1,"\nNilai Q2 =", nq2,"\nNilai Q3 =",nq3)
#Mid-Range
MidRange = (data[0]+data[n-1])/2
print("Mid-Range =",MidRange)
#Mid-Hinge
MidHinge = (nq1+nq3)/2
print("Mid-Hinge =",MidHinge)
#Range
Range = data[n-1]-data[0]
print("Range =",Range)
#IQR
iqr = nq3 - nq1
print("IQR =",iqr)
#SIQR
siqr = iqr/2
print("SIQR =",siqr)
#Variance
sigma = 0
for a in range(0, n):
    sigma = sigma + ((data[a]-mean)**2)
v = sigma/(n-1)
print("Variance: ", v)
#Standard deviation
s = math.sqrt(v)
print("Standar Deviation: ", s)
#One step
onestep = iqr*1.5
print("One Step =", onestep)
#Two step
twostep = iqr*3
print("Two Step =", twostep)
#lower fences
lif = nq1 - onestep
lof = nq1 - twostep
print("LIF =",lif,"\nLOF =",lof)
#upper fences
uif = nq3 + onestep
uof = nq3 + twostep
print("UIF =",uif,"\nUOF =",uof)