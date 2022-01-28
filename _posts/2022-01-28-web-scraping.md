---
layout: post
title: Extraer datos públicos de la web mediante "web scraping"
date: 2022-01-28 12:00:00
categories: otros
tags: selenium automation html css
published: true
---


Si tuviéramos que extraer grandes cantidades de datos de algún sitio web, lo mejor sería saber crear nuestra propia herramienta de "web scraping". Es un concepto interesante porque comparte varias de las técnicas con la automatización de pruebas que hace un QA "automator".
Algunos de los frameworks y bibliotecas más conocidos se utilizan sobre Python, aunque también pueden usarse otros lenguajes. Y luego del "scraping" viene una segunda etapa, que es la de procesar y analizar los datos recolectados, pero eso queda para otra publicación 😉.


![Web scraping]({{ site.url }}/assets/2022-01-28-web-scraping.png)


{% include accesibilidad.html %}
Web scraping

Es una técnica para extracción de datos de sitios web públicos para su posterior uso, usualmente copiándolos a partir del código HTML.

Puede hacerse de forma manual, pero lo más común es que se utilice software que automatice el proceso.

Ejemplos de uso: recolectar datos estadísticos, analizar opiniones sobre un producto, detectar variaciones de precios, etc.

Herramientas: Suelen ser similares a las usadas en QA para automatizar  pruebas. Son necesarios conocimientos sobre HTML y CSS, además de dominar las herramientas específicas. Algunos frameworks y bibliotecas: Selenium, Beautiful Soup, Scrapy…

¿Cómo se hace? Luego de acceder al código fuente de la página web se seleccionan los elementos que contienen los datos, que son luego volcados a un archivo o una base de datos para su posterior análisis.

</div></details>
<hr />
