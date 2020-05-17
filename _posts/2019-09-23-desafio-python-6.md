---
layout: post
title: Desafío Python número 6
date: 2019-09-23 21:00:00
categories: desafios python
tags: funciones
published: true
---

👉 Desafío Python número 6.

Estos videos pueden ayudarte a resolverlo:

▶️ [Funciones](youtu.be/IF34NgjldXs){:target="_blank"}

▶️ [Listas](youtu.be/TEHBEGj1MSU){:target="_blank"}

▶️ [Conjuntos](youtu.be/OJRJRxmaLY8){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />
<br />✏️ Explicación:
<br />🔹 funcion1 recibe la lista [1,2,3,3,2,4] y retorna el resultado de convertirlo a conjunto y eliminar el elemento que es igual a la cantidad de veces que aparece el 3 en esa lista (es decir, el número 2). Para poder eliminar, primero coloca a ese número en una lista y luego la convierte a conjunto. Es decir, retorna el conjunto {1, 3, 4}.
<br />🔹 funcion2 recibe a la lista [1,2,3,3,2,4] y al conjunto resultado de funcion1. A la lista le agrega el número 5 y luego retorna el resultado de convertir la lista a conjunto (lo que da el conjunto {1,2,3,4,5}) y realizar una unión con el conjunto {1,3,4}. Entonces retorna el conjunto {1,2,3,4,5}.
<br />🔹 funcion3 recibe a un conjunto compuesto por los elementos únicos de la lista [1,2,3,3,2,4] (es decir: {1,2,3,4}) y el conjunto retornado por funcion2 (es decir, {1,2,3,4,5}). Retorna el resultado de evaluar si el primero es menor que el segundo, lo cual es verdadero, entonces el valor de retorno es True.
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-09-23-desafio-python-6-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇

![]({{ site.url }}/assets/2019-09-23-desafio-python-6.png)
