from mrjob.job import MRJob
class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        company, price, date = line.split(',')
        lista = [float(price), date]
        yield company, lista
    def reducer(self, sector, values):
        l = list(values)
        menor = 10000000000
        mayor = 0
        dia_mayor = ""
        dia_menor = ""
        for i in l:
            if i[0]>mayor:
                if mayor != 0 and mayor < menor:
                    dia_menor = dia_mayor
                    menor = mayor
                dia_mayor = i[1]
                mayor = i[0]
            elif i[0]<menor:
                dia_menor = i[1]
                menor = i[0]
        yield sector, (dia_mayor, dia_menor)
if __name__ == '__main__':
    MRWordFrequencyCount.run()