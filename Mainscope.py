import csv

reader = csv.reader(open('teste1.csv'), delimiter=';')
reader1 = csv.reader(open('teste2.csv'), delimiter=';')

b = []
c = []

for i in reader:
    b.append(i)

for i in reader1:
    c.append(i)

def analisa(a1, a2):
    depurado1=[]
    depurado2=[]

    if len(b) > len(c):
        print('Teste 1 possui mais elementos.')
        for i in b:
            if i not in c:
                depurador1.append(i)
        for a in depurador1:
            print (a)
    else:
        print('Teste 2 possúi mais elementos.')
        for h in c:
            if h not in b:
                depurado2.append(h)
        for z in depurado2:
            print(z)

analisa(b,c)