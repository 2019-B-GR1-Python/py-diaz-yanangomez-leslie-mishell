import scrapy

class IntroSpider(scrapy.Spider):
    #Se define el nombre de la araña
    name="introduccion_spider"
    #Se definen las urls a visitar
    urls = [
        "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url) # yield--> Esperar para que se complete la linea (no sea asincrona)

    def parse(self, response):
        self.urls = response.css("div.side_categories > ul > li > ul > li > a::attr(href)").extract()
        def priceToFloat(price):
            return float(price[1:])
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css("h3 > a::text").extract()
        precios = etiqueta_contenedora.css("div.product_price > p.price_color::text").extract()
        precios_float = list(map(priceToFloat, precios))
        links_imagenes = etiqueta_contenedora.css("div.image_container > a > img::attr(src)").extract()
        print(titulos)
        print(precios_float)
        print(links_imagenes)
        print(self.urls)


        #Segundo ejercicio
        #links en la izquierada, extraer todos los links y pasar el primer ejercicio 
        # guardar datos con una archivo
    
    
