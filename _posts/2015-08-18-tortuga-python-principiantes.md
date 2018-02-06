---
layout: post
title: La tortuga (Python para principiantes)
date: 2015-08-18 19:00:00
categories: python
published: true
---

La "tortuga" es un concepto que surgió hace varias décadas para enseñar elementos básicos de programación, especialmente a los niños (aunque es también muy buen punto de inicio para los adultos). Básicamente, el usuario ve una "tortuga" en pantalla que permite dibujar gráficos siguiendo un algoritmo.

En Python, el módulo "turtle" ya viene incorporado con la instalación básica (es decir que no es necesario agregar nada). Entonces, es posible usar las estructuras que se usan normalmente en Python, agregándoles las instrucciones específicas de Turtle. Para poder agregar estas instrucciones, debemos escribir _from turtle import *_ al principio del programa.

La tortuga en Python siempre empieza "mirando" hacia la derecha y, a medida que camina, deja una línea dibujada. Si se la hace caminar hacia adelante, empezará haciendo una línea de izquierda a derecha.

## Algunas órdenes básicas de Turtle (hay muchas más):

<table>
  <tr>
    <td>
      forward(x)
    </td>
    <td>
      Caminar hacia adelante (la cantidad de pixeles indicada en el número x)
    </td>
  </tr>
  <tr>
    <td>
      backward(x)
    </td>
    <td>
      Caminar hacia atrás (la cantidad de pixeles indicada en el número x)
    </td>
  </tr>
  <tr>
    <td>
      right(x)
    </td>
    <td>
      Girar la tortuga hacia la derecha en un ángulo de x grados
    </td>
  </tr>
  <tr>
    <td>
      left(x)
    </td>
    <td>
      Girar la tortuga hacia la izquierda en un ángulo de x grados
    </td>
  </tr>
  <tr>
    <td>
      begin_fill()
    </td>
    <td>
      Las figuras cerradas dibujadas a continuación serán pintadas con un color x especificado por fillcolor(x)
    </td>
  </tr>
  <tr>
    <td>
      end_fill()
    </td>
    <td>
      Pinta todas las figuras cerradas que se hayan dibujado a partir de donde dice begin_fill() y hasta donde se coloca end_fill()
    </td>
  </tr>
  <tr>
    <td>
      fillcolor(x)
    </td>
    <td>
      Rellena, con el color indicado en el string x, la figura dibujada por las instrucciones incluidas entre begin_fill() y end_fill()<br /> Algunos ejemplos de colores: 'red', 'green', 'yellow' (deben escribirse entre comillas)
    </td>
  </tr>
  <tr>
    <td>
      pencolor(x)
    </td>
    <td>
      Indica que, todo lo que se dibuje, en adelante será del color indicado por el string x
    </td>
  </tr>
  <tr>
    <td>
      circle(x)
    </td>
    <td>
      Dibuja un círculo del radio indicado por el número x
    </td>
  </tr>
</table>

## Ejemplos:

Veamos algunos ejemplos de código para dibujar formas geométricas. Para interpretar código, una buena idea es seguirlo en papel, respetando las instrucciones en el orden en que están escritas.

_Ejemplo 1:_

<pre><code>from turtle import *
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)</code></pre>

Esto dibuja un cuadrado, porque hace 4 veces lo mismo: dibuja una línea recta y gira a la izquierda en 90º. Como esas dos órdenes se repiten 4 veces, lo mejor es escribirlo con alguna herramienta que permita repetir algo. Por ejemplo, un **for** que itere 4 veces:

<pre><code>from turtle import *
for i in range(4):
    forward(50)
    left(90)</code></pre>

![cuadrado]({{ site.url }}/assets/2015-08-18-tortuga-python-principiantes-img1.png)

_Ejemplo 2:_

En este caso dibuja un triángulo, entonces las instrucciones se repiten tres veces y, en vez de girar 90º, gira 120º:

<pre><code>from turtle import *
for i in range(3):
    forward(100)
    left(120)</code></pre>

(el ángulo de 120 es porque se dividen los 360 grados totales por la cantidad de lados que tiene la figura a formar: 360/3=120)

![triángulo]({{ site.url }}/assets/2015-08-18-tortuga-python-principiantes-img2.png)

Para hacer el mismo triángulo, pero relleno de color rojo:

<pre><code>from turtle import *
fillcolor('red')
begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()</code></pre>

![triángulo rojo]({{ site.url }}/assets/2015-08-18-tortuga-python-principiantes-img3.png)

_Ejemplo 3:_

Para hacer una estrella:

<pre><code>from turtle import *
for i in range(5):
    forward(100)
    right(144)</code></pre>

![estrella]({{ site.url }}/assets/2015-08-18-tortuga-python-principiantes-img4.png)

_Ejemplo 4:_

Para dibujar una cuadrícula de 3x3 habrá que usar iteraciones anidadas: por un lado, la iteración más interna que dibuja un cuadrado (la misma vista en ejemplo 1), por otro lado la que forma las columnas y por otro la que forma las filas:

<pre><code>from turtle import *
for fila in range(3):   #qué quiero hacer en cada fila
    for columna in range(3):   #qué quiero hacer en cada columna
        for cuadrado in range(4):   #dibujo un cuadrado
            forward(50)  
            right(90)
        forward(50)   #para no empezar otra vez en el mismo punto al terminar una fila, me corro a la derecha en el ancho de 1 cuadradito
    backward(50*3)   #vuelvo 3 cuadraditos para atrás (cada uno mide 50 de ancho) para quedar nuevamente en la primera columna
    right(90)
    forward(50)
    left(90)   #con las últimas 3 líneas me vuelvo a posicionar para empezar a dibujar la siguiente fila</code></pre>

![cuadrícula]({{ site.url }}/assets/2015-08-18-tortuga-python-principiantes-img5.png)

Si quisiera que cada cuadrado quede pintado de un color, alternando entre 2 colores, entonces tengo que usar alguna estrategia: por ejemplo, empiezo contando del 1 en adelante cada cuadrado que dibujo; si el número es par pinto de un color y si es impar pinto de otro. Para contar los cuadrados uso una variable:

<pre><code>from turtle import *
recuadro = 1   #número de cuadrado
for fila in range(3):
    for columna in range(3):
        begin_fill()   #lo que quiero pintar es lo que se dibuja a continuación: un cuadrado
        for cuadrado in range(4):
            forward(50)
            right(90)
        if recuadro % 2 == 0:   #si el número es par
                fillcolor('red')   #pinto de rojo
        else:   #si el número no es par
                fillcolor('green')  #pinto de verde
        end_fill()   #terminé de dibujar un cuadrado, entonces lo pinto
            recuadro += 1;   #paso a contabilizar el siguiente cuadrado
            forward(50)
    backward(150)
    right(90)
    forward(50)
    left(90)</code></pre>

![cuadrícula con colores]({{ site.url }}/assets/2015-08-18-tortuga-python-principiantes-img6.png)
