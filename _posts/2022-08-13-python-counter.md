---
layout: post
title: Contar ocurrencias con collections.Counter() en Python
date: 2022-08-13 12:00:00
categories: python
tags: algoritmos colecciones contenedores
published: true
---


Una interesante opción que ofrece Python para contar las ocurrencias de cada elemento de un contenedor.
A tener en cuenta: con la primera opción obtenemos un diccionario mientras que, con la segunda, obtenemos un objeto de tipo collections.Counter 🤓

Para saber más: [https://docs.python.org/3/library/collections.html#collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter)


![Python collections.Counter]({{ site.url }}/assets/2022-08-13-python-counter.png)


{% include accesibilidad.html %}
Python: collections.Counter() crea un diccionario a partir de un objeto iterable (cuyos elementos sean "hashables").

Ejemplo: queremos contar las ocurrencias de cada letra en una lista.

Opción 1: con un diccionario, iterando por la lista para contar "manualmente".

lista = ['a','g','p','s','a','a','p']
cantidades = dict.fromkeys(lista, 0)
for letra in lista:
    cantidades[letra] += 1

Opción 2: con Counter:

from collections import Counter
lista = ['a','g','p','s','a','a','p']
cantidades = Counter(lista)

</div></details>
<hr />
