---
layout: post
title: Abstracción en una iteración fija (for)
date: 2015-06-21 19:00:00
categories: conceptos
published: true
---

En algunos lenguajes, como Python o Java, existe una forma de escribir un "for" que automáticamente itere por los elementos un contenedor. Esta implementación suele usar iteradores: objetos que pertenecen a un contenedor y que, al solicitarles acceder al siguiente elemento, lo retornan; de esta forma el iterador puede obtener cada elemento del contenedor, uno por vez.

_Ejemplo 1:_ en Python esto se escribe:

<pre><code>for elemento in contenedor:
    #instrucciones</code></pre>

En Java esto se escribe:

<pre><code>for (Tipo elemento: contenedor)
    { //instrucciones }</code></pre>

El funcionamiento es sencillo: **contenedor** es una variable de algún tipo de dato correspondiente a un contenedor (vector, conjunto, tupla, diccionario, etc.) y **elemento** es una variable donde se va a guardar el valor de cada elemento que se encuentra en el contenedor.

Entonces, la abstracción nos permite que sólo veamos un nombre de variable (**elemento**) pero la computadora ve concretamente un elemento del contenedor. Entonces, si estuviéramos escribiendo en Python y en la variable _contenedor_ tuviéramos guardada esta tupla de cuatro elementos: ( "ABC", 89, [1, 2], (1==0, 4//2, "x") ), al iterar en la forma indicada anteriormente, la variable _elemento_ irá tomando como valores el contenido de la tupla, en orden desde el elemento en la posición 0 (el primero de la tupla) hasta el último, uno por cada iteración. Entonces, la variable elemento, en la primera iteración hace referencia ("se reemplaza") al string _"ABC"_, en la segunda iteración hace referencia al entero _89_, en la tercera iteración hace referencia a la lista _[1,2]_ y en la cuarta y última iteración hace referencia a la tupla _(False, 2, "x")_, ya que resuelve la abstracción _1==0_ obteniendo el resultado _False_, la abstracción _4//2_ obteniendo el resultado _2_, y la "_x_" es un valor string literal.
