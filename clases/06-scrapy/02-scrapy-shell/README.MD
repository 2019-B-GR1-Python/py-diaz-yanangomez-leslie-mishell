# Scrapy
## Instalación
Se utiliza el siguiente comando en `Anaconda Prompt`
```
pip install scrapy
conda install -c conda-forge scrapy 
```
o una alternativa es
```
conda install -c conda-forge scrapy 
```
## Comandos Generales
* `scrapy bench` .- Da las caracteristicas para poder hacer web scraping o web crawling de ese computador

![]('./resources/scrapy-view-bien.PNG')

* `scrapy settings`. - Visualizar las configuraciones extra

![]('./resources/scrapy-view-bien.PNG')

* `scrapy version`. - Visualizar la version de Scrapy

![]('./resources/scrapy-view-bien.PNG')


### scrapy view 'url'
Se abre una nueva ventana del navegador. Antes de hacer scrapy es necesario comprobar con este comando si el contenudo de la pagina web es accesible (esté en HTML5)

* Ejem bien: Pagina Authors Pluralsight

![]('./resources/scrapy-view-bien.PNG')

* Ejem mal: Pagina SRI

![]('./resources/scrapy-view.PNG')

### scrapy shell 'url'
Trabajar con la ventana, permite interactuar con la respuesta del scrapy mediante un shell

![]('./resources/scrapy-shell.PNG')

#### response.css('title')
![]('./resources/shell-title')
#### response.css('title').extract()
![]('./resources/shell-title-extract.PNG')
#### response.css('title::text').extract()
![]('./resources/shell-title-extract-only-text.PNG')
#### response.css('.author::text').extract()
![]('./resources/shell-title-extract-only-text-author.PNG')

#### response.css('.author::text')[0].extract()
![]('./resources/extract-only-first.PNG')

o se utiliza el metodo `extract_first()`
![]('./resources/extract-first.PNG')

#### Extraer texto de un etiqueta con una clase
![]('./resources/extract-label-class.PNG')

#### Extraer texto de una clase dentro de otra clase

![]('./resources/extract-class-into-class.PNG')

#### Extraer texto de una propiedad de una etiqueta

![]('./resources/extract-atrib-label.PNG')