import csv

class Depuradora(object):
    def __init__(self, a, b):
        self.arquivo1 = csv.reader(open('%s.csv'%(a)), delimiter=';')
        self.arquivo2 = csv.reader(open('%s.csv'%(b)), delimiter=';')

        self.inicia()

    def inicia(self):
        lista1 = []
        lista2 = []

        for i in self.arquivo1:
            lista1.append(i)

        for j in self.arquivo2:
            lista2.append(j)

arq1 = input("Digite o nome do primeiro arquivo (sem a extensão CSV)")
arq2 = input("Digite o nome do segundo arquivo(sem a extensão CSV)")

Depuradora(arq1, arq2)