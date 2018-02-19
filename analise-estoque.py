import csv

reader = csv.reader(open('pge-as.csv'), delimiter=',')
reader1 = csv.reader(open('beas.csv'), delimiter=';')

b = []
c = []

for i in reader:
    b.append(i)

for t in reader1:
    c.append(t)

print(len(b))
print(len(c))


for a in b:
    aaa = a[11]
    for m in c:
        mmm=m[1]
        if aaa[0:3] == mmm[0:3] and a[13] == m[11]:
            print(a[11],": ", a[13], ' | ', m[1],": ", m[11])
            print('-' *40)
            c.remove(m)
            break

almox = input('Digite o nome do Almoxarifado desta conferência: ')

print(almox)

for h in c:
    print('código: ', h[0], h[1], h[11])


         


