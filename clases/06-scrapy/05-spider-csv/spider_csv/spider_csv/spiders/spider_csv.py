import scrapy
from scrapy.spiders import CSVFeedSpider

class AraniaCrawCsv(CSVFeedSpider):
    name = 'vinos'

    delimiter = ';'
    quotechar = '"'
    # Poner todas las columnas siempre, no importa el orden de las mismas
    headers = [
        'fixed density',
        'volatile acidity',
        'citric acid',
        'residual sugar',
        'chlorides',
        'free sulfur dioxide',
        'total sulfur dioxide',
        'density',
        'pH',
        'sulphates',
        'alcohol',
        'quality'
    ]

    start_urls = [
        'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
    ]

    def parse_row(self, response, row):
        print(type(row))
        print('ph', row['pH'])
        # print('citric acid', row['citric acid'])
        with open('vinos.txt','a+', encoding="utf-8") as archivo:
                archivo.write(row['pH'] + "\n")
       