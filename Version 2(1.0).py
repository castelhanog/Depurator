import csv

class Depuradora(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.arquivo1 = csv.reader(open('%s.csv'%(self.a)), delimiter=';')
        self.arquivo2 = csv.reader(open('%s.csv'%(self.b)), delimiter=';')

        self.inicia()

    def inicia(self):
        lista1 = []
        lista2 = []

        for i in self.arquivo1:
            lista1.append(i)

        for j in self.arquivo2:
            lista2.append(j)

        self.verifica(lista1, lista2)

    def verifica(self, l1,l2):

        if len(l1) > len(l2):
            print('Existem lançamentos a maior em %s.' % (self.a))
        else:
            print('Existem lançamentos a maior em %s.' % (self.b))

        analisa()

    def analisa(self):
        


arq1 = input("Digite o nome do primeiro arquivo (sem a extensão CSV): ")
arq2 = input("Digite o nome do segundo arquivo(sem a extensão CSV): ")

Depuradora(arq1, arq2)