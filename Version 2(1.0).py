import csv

class Depuradora(object):
    def __init__(self, a, b):
        self.arquivo1 = csv.reader(open('%s.csv'%(a)), delimiter=';')
        self.arquivo2 = csv.reader(open('%s.csv'%(b)), delimiter=';')

        self.imprime()

    def imprime(self):
        for i in self.arquivo1:
            h = i.index('Valor')
            for b in self.arquivo1:
                print(b[h])
        print('\n')
        for j in self.arquivo2:
            k = i.index('Valor')
            for p in self.arquivo2:
                print(p[k])

arq1 = input("Digite o nome do primeiro arquivo (sem a extensão CSV)")
arq2 = input("Digite o nome do segundo arquivo(sem a extensão CSV)")

Depuradora(arq1, arq2)