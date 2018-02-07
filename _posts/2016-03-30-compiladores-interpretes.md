---
layout: post
title: Compiladores e intérpretes, lenguajes compilados e interpretados
date: 2016-03-30 19:00:00
categories: conceptos
published: true
---

## Código de máquina

Cuando escribimos código en algún lenguaje de programación, normalmente éste necesita ser convertido a un lenguaje que la máquina pueda entender, que normalmente se llama "código de máquina" y son instrucciones específicas para el procesador, en números binarios. El tipo y cantidad de instrucciones depende de la marca y modelo del procesador (es por esto que los programas compilados para un tipo de procesador suelen no ser "portables" para cualquier otro).

Absolutamente todo se traduce en este tipo de instrucciones. Los lenguajes de más alto nivel brindan una abstracción mucho mayor, es decir, nos evitan tener que involucrarnos con los detalles de cada instrucción. Esto es porque, habitualmente, una instrucción de alto nivel equivale a varias de bajo nivel (ver "[Lenguajes de bajo y alto nivel](/conceptos/2016/03/29/lenguajes-de-bajo-y-alto-nivel.html)").

Esta tarea de traducción del código que escribe un programador al código que entiende una máquina es realizada por otro programa: un _compilador_ o un _intérprete_, dependiendo del lenguaje. Así, podemos decir que hay "lenguajes compilados" y "lenguajes interpretados".

![traducción]({{ site.url }}/assets/2016-03-30-compiladores-interpretes-img1.jpg)

## Lenguajes compilados

En un lenguaje compilado el programa que hace la traducción se llama "compilador" y se ejecuta una única vez sobre todo el código, generando uno o más archivos de código intermedio, que luego son finalmente convertidos en un archivo ejecutable. Luego de compilado y generado este archivo, el programa corre a partir del archivo ejecutable y no del código del programador. Es más: el código que escribió el programador se "pierde", ya que el usuario sólo necesita el archivo ejecutable para poder correr el programa.

## Lenguajes interpretados

En un lenguaje interpretado el programa que traduce se llama "intérprete" y toma de a una instrucción por vez, traduciéndola y ejecutándola. Este trabajo debe realizarse cada vez que se desee correr el programa, por lo que el código escrito por el programador persiste.

## Categoría intermedia: bytecodes

Con una forma intermedia entre compilados e interpretados, se encuentran los lenguajes que requieren de una máquina virtual además de un compilador, y cuyo código es convertido a "bytecodes" (por ejemplo, Java). En este caso, el compilador no traduce a código de máquina directamente, sino que _compila_ a una forma intermedia, llamada bytecodes. Éstos son instrucciones similares a las ejecutadas por un intérprete. La máquina virtual luego se encarga de _interpretar_ y ejecutar los bytecodes directamente, uno a uno. Se suele utilizar esta técnica para facilitar la portabilidad e independencia de hardware y sistemas operativos.

## Análisis de código Python

Python incluye el módulo **dis** que permite el análisis del código generado. A modo de ejemplo, se analizará una función muy sencilla, tal como es compilada por el compilador CPython.

Lo primero que se debe hacer es importar el módulo. Para esto en el intérprete interactivo, ejecutar la instrucción <code>import dis</code>.

A continuación, definimos la siguiente función:

<pre><code>def funcion():
x = 4
z = 8
return x + z</code></pre>

Para analizar los bytecodes de esta función, deberemos ejecutar la instrucción <code>dis.dis(funcion)</code>, lo que brindará la siguiente información:

![análisis de bytecodes en python]({{ site.url }}/assets/2016-03-30-compiladores-interpretes-img2.png)

Se pueden distinguir tres columnas de datos: la primera contiene números que identifican los números de línea de código (siendo la 1 la de la definición de la función, la 2 la línea donde se almacena el valor 4 en la variable x, etc.); la segunda columna indica el código de máquina ejecutado (precedido de su dirección específica) y la tercera indica el dato involucrado en la operación. Así, pueden verse las siguientes instrucciones:

* En la línea 2 se carga (load) una constante (aquí se llama "constante" a los literales) con el valor 4 en la pila (un segmento especial de la memoria) y luego se la almacena (store) en la variable x.
* En la línea 3 se repite lo mismo pero con la constante de valor 8 en la variable llamada z.
* Finalmente, la línea 4 carga (load) los valores de las variables x y z en la pila, realiza la suma (binary_add) y retorna el valor resultante.

Puede verse una descripción de todas las instrucciones existentes en la documentación oficial, [aquí](https://docs.python.org/3/library/dis.html).
