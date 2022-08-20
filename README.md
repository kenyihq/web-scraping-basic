# [Web Scraping](https://platzi.com/cursos/web-scraping/)

## ¿Qué es HTML?

HTML es una lenguaje que permite definir la estructura de una página web.
Estrucutra, estilo, partes interactivas. En el contexto de webscraping HTML es muy importante

Etiquetas está encerrado en angle brakets.**<>**
Una etiqueta peude contener a otras etiquetas, las etiquetas tienen atributos.

El conocimiento de los atributos será crucial porque con ellos podremos conectar el scraper para extraer información.

* [script](https://developer.mozilla.org/es/docs/Web/SVG/Element/script) Se utiliza para insertar o hacer referencia a un script ejecutable dentro de un docuemnto HTML.

* [meta](https://es.wikipedia.org/wiki/Etiqueta_meta) aporta información extra al documento, metadatos como autor, título, fehca, palabras clave
es de suma importancia para el navegador.

* [iframe](https://developer.mozilla.org/es/docs/Web/HTML/Elemento/iframe) Puedo anidar un elemento HTML sobre otro elemento.

## Robots.txt

Los archivos **robots.txt** exiten como una forma de administrar una página web, proporciona información a los rastreadores de los buscadores sobre las páginas o los archivos que pueden solicitar o no de tu sitio web.
Principalmente, se utiliza para evitar que tu sitio web se sobrecargue con solicitudes.
En el contexto de webscraping, le dice al scraper que puede y no extraer, es decir hasta donde puede llegar, ya que infrigir en la violación
de estas directivas puede acarrear un problema legal con el sitio web al que estamos scrapeando.

**Robots.txt**
Contiene entre otros elementos:

* USER-AGENT: Identificadores de quienes acceden a tu sitio web, puede ser un archivo.py hasta un googlebot.

**DIRECTIVAS**

* ALLOW: Utiliza esta directiva para permitir a los motores de búsqueda rastrear un subdirectorio o una página, incluso en un directorio que de otro modo no estaría permitido
* DISALLOW: Utiliza esta directiva para indicar a los motores de búsqueda que no accedan a archivos y páginas que se encuentren bajo una ruta específica

Ejemplo:

```
url/robots.txt
Pro ejemplo:

# Robots.txt file from http://www.nasa.gov
#
# All robots will spider the domain

User-agent: *
Disallow: /worldbook/
Disallow: /offices/oce/llis/

```

Para conocer más información de [robots.txt](https://ahrefs.com/blog/es/robots-txt/)

## XML Path Language

Sirvio para definir interfaces, es un lenguaje de nodos o etiquetas.
Una técnica para extraer datos de allí es Xpath.

Xpath es a HTML lo que las REGEX son a un texto.
Es decir, Xpath es un lenguaje de patrones, expresiones que me permitirá extraer datos de un HTML. Puntualmente sirve para apuntar a partes de un documento XML.

### Tipos de nodos

Un nodo es lo mismo que la etiqueta y su contenid, puede contener a otros nodos.
En otras palabras Xpath nos permitirá navegar en los diferentes niveles de profundidad deseados con el fin extraer información. Para describir los nodos y relaciones con Xpath se usan una sintaxis de ejes.

[Toscrape](http://toscrape.com/) es un sandbox para practicar.

### Expresiones en XPath

**/** : Significa la raiz o root de todo el documento, tambien significa un salto entre nodos. Puedo navegar entre niveles

**//** : Puedo ir por varios niveles en el esquema que construimos.

Ejemplo:

```
# Fuente de trabajo Quotes to Scrape:

url ="http://quotes.toscrape.com/"

#Quiero extraer el texto de mi nodo h1.

$x('//h1/a/text()').map(x => x.wholeText)
# Devuelve en consola: ["Quotes to Scrape"]
#La función map pertenece a Js y la estoy usando para que me muestre todo el texto de la 
selección de Xpath.
```

Existen otras expresiones

**/..** : Acceder a todos los nodos padre de x nodo.
**/@atribute_name** : Me permite extraer atributos

```
#Estoy trayendo todos los atributos class de los nodos span.
$x('//span/@class')
```

### Predicados

Para ser específicos con los datos a extraer se usan predicados.

**[predicado]** :Para encontrar nuestra información debemos ser más especificos, para ello
sirve los predicados.

**Predicados :**

**n** : Hace referencia al n elemento de la lista.
**last()**: Al último elemento de la lista.
**@atribute_name** : Al usarse como predicado me trae todos los nodos
que contienen este atributo
**@atribute_name=""** : Al usarse como predicado me trae todos los nodos
que contienen este atributo, incluso el value de este atributo.
Ejemplos:

```
# Para extraer solo uno de los div del div container usamos un predicado

$x('/html/body/div/div[1]')
# Devuelve [div.row.header-box]

$x('//span[@class="text"]/text()').map(x=>x.wholeText)
# Devuelve (10) ["“The world as we have created it is a process of o…cannot be changed without changing our thinking.”", "“It is our choices, Harry, that show what we truly are, far more than our abilities.”", "“There are only two ways to live your life. One is… The other is as though everything is a miracle.”", "“The person, be it gentleman or lady, who has not …ure in a good novel, must be intolerably stupid.”", "“Imperfection is beauty, madness is genius and it'…be absolutely ridiculous than absolutely boring.”", "“Try not to become a man of success. Rather become a man of value.”", "“It is better to be hated for what you are than to be loved for what you are not.”", "“I have not failed. I've just found 10,000 ways that won't work.”", "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", "“A day without sunshine is like, you know, night.”"]
```

