---
layout: post
title: Manejo de strings en Pascal
date: 2011-05-31 19:00:00
categories: pascal
published: true
---

Debido a que en Pascal los strings son una sucesión de caracteres que se almacenan en un área contigua de la memoria y que pueden ser leídos o escritos, existen funciones y procedimientos predefinidos que permiten manipular valores de este tipo.

Debe tenerse en cuenta que, implícitamente, un string tiene un índice numérico para cada carácter, comenzando por el 1:

![string con sus índices]({{ site.url }}/assets/2011-05-31-strings-pascal-img1.jpg)


## Length

Esta función recibe como argumento un string y devuelve un valor de tipo integer con la longitud del string.

_Ejemplo:_

<pre><code>longitud := length(cadena);</code></pre>

donde _longitud_ es un integer y _cadena_ es un string. Si, por ejemplo, la variable _cadena_ contuviera el valor 'hola mundo', entonces la función length devolverá el valor 10, ya que la variable tiene 10 caracteres. La asignación hace que la variable llamada _longitud_ almacene este número de caracteres retornado por _length_.



## Pos

Recibe como argumento un sub-string y un string, y devuelve un integer representando la posición de inicio del primero dentro del segundo. Si no se encuentra, devuelve cero. Debido a que un string está compuesto por caracteres, es posible pasarle como parámetro un único carácter, en cuyo caso retornará la posición en que éste se encuentra dentro del string. Si se encuentra más de una vez, sólo retorna la posición de la primera ocurrencia.

_Ejemplos:_

<pre><code>posicion := pos('o', cadena);
posicion := pos('hola', cadena);</code></pre>

donde _posicion_ es un integer y _cadena_ es un string dentro del cual se buscarán los sub-strings.



## Copy

Recibe como argumentos un string y dos enteros y devuelve un valor de tipo string. Permite extraer parte del string que se pasa como parámetro, comenzando en la posición que se le pasa como segundo parámetro, y extrayendo tantos caracteres como el tercer parámetro indique.

_Ejemplo:_

<pre><code>subcadena := copy(cadena, 6, 5);</code></pre>

donde _cadena_ y _subcadena_ son strings. Si la variable _cadena_ contiene el valor 'hola mundo', esta función retorna la subcadena 'mundo'.



## LowerCase

Retorna el string pasado como parámetro con todas sus letras convertidas a minúsculas. Si no existen letras mayúsculas en el string, el string retornado será igual al pasado por parámetro.

_Ejemplo:_

<pre><code>minuscula := lowercase("HoLa")</code></pre>

En este caso, en la variable _minuscula_ queda almacenando el valor "hola".



## UpperCase

Retorna el string pasado como parámetro con todas sus letras convertidas a mayúsculas. Si no existen letras minúsculas en el string, el string retornado será igual al pasado por parámetro.

_Ejemplo:_

<pre><code>mayuscula := lowercase("HoLa")</code></pre>

En este caso, en la variable _mayuscula_ queda almacenando el valor "HOLA".


