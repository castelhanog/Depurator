import csv

reader = csv.reader(open('débito.csv'), delimiter=';')
reader1 = csv.reader(open('crédito.csv'), delimiter=';')

b = []
c = []

for i in reader:
    b.append(i)

for i in reader1:
    c.append(i)

def analisa(a1, a2):
    depurado1=[]
    depurado2=[]

    print ('Valores encontrados no débito e não encontrados no crédito (Liquidados mas sem entrada no estoque):'"\n \n ")
    for i in b:
        if i not in c:
            depurado1.append(i)
    for a in depurado1:
        print (a)

    print ('Valores encontrados no créditos e não encontrados no débito (Com entrada no estoque, mas registro semelhante de liquidação:\n\n')
    for h in c:
        if h not in b:
            depurado2.append(h)
    for z in depurado2:
        print(z)

analisa(b,c)