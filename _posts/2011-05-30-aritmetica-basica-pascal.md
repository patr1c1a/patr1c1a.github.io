---
layout: post
title: Aritmética básica en Pascal
date: 2011-05-30 19:00:00
categories: pascal
tags: paradigma_imperativo operaciones cociente resto aritmética datos_primitivos 
published: true
---

Las operaciones con datos de tipo numérico (datos de tipo integer o real) admiten, además de las operaciones básicas de suma (con el signo +), resta (con el signo -), multiplicación (con el signo *) y división (con el signo /), algunas formas de operaciones y funciones especiales.

La división con barra (/) en Pascal siempre retorna un dato de tipo real, aunque sus operandos sean integer, ya que el resultado es un número con decimales.

Para indicar que un número es negativo, se antepone el operador de resta (-), por ejemplo: -20.

&nbsp;

## División

Además de la división expresada por medio de la barra es posible obtener sólo la parte entera o sólo el resto. Para obtener la parte entera se utiliza el operador **div** y para el resto se utiliza el operador **mod**. Estos operadores sólo funcionan sobre datos de tipo entero.

Ejemplos de los resultados obtenidos mediante la división con cada uno de los tres operadores (dividiendo, en este ejemplo, 328 entre 6):

<pre><code>328 / 6 = 5.4666666667E+01
328 div 6 = 54
328 mod 6 = 4
</code></pre>
Los operadores div y mod pueden servir a varios fines, para manipular datos numéricos. Por ejemplo, dividiendo a un número por 2 con el operador _mod_ puede determinarse si el número es par (si arroja resto 0) o impar (si arroja resto diferente de 0). También, puede obtenerse el último dígito de un número si se lo divide por 10 utilizando el operador _mod_, o se puede obtener todo el número excepto el último dígito si se divide el número por 10 utilizando _div_.

&nbsp;

## Decimales

Obsérvese que el primer resultado del ejemplo anterior (un número real) se expresa por medio de un número con exponente. Para evitar una impresión por pantalla de este tipo y limitar la cantidad de dígitos decimales a visualizar, se deben colocar dos puntos seguidos de la cantidad de dígitos a incluir de la parte entera, y otros dos puntos seguidos de la cantidad de decimales. Por ejemplo:
  
<pre><code>writeln(328/6:4:2)</code></pre> mostrará 54.67.

El rol del primer número colocado después de los dos puntos (en el ejemplo, el 4) es forzar la cantidad de dígitos a incluir en la parte entera. Es decir, en el caso anterior el número convertido en verdad es 0054.67, pero los dos primeros ceros no se muestran al imprimirse por pantalla. Esto es útil, por ejemplo, si se están guardando datos en un
  
registro en el que se necesita que el número almacenado ocupe obligatoriamente 4 dígitos. Es importante notar que este operador no limita la cantidad de dígitos. Es decir, si se indica :1:2, el número mostrado seguirá siendo 54.67.

&nbsp;

## Funciones aritméticas

|Función|Descripción|Tipo del parámetro|Tipo del valor de retorno|
|-------|--------|---------|---------|
|abs(x)|Valor absoluto de x|integer o real|el mismo que x|
|sin(x)|Seno de x (en radianes)|integer o real|real|
|cos(x)|Coseno de x (en radianes)|integer o real|real|
|arctan(x)|Arco tangente de x (en radianes)|integer o real|real|
|exp(x)|Función exponencial de x|integer o real|real|
|ln(x)|Logaritmo natural de x|integer o real|real|
|round(x)|x redondeado al entero inmediatamente siguiente|real|integer|
|trunc(x)|x redondeado a su parte entera|real|integer|
|sqr(x)|x al cuadrado|integer o real|el mismo que x|
|sqrt(x)|Raíz cuadrada de x|integer o real|real|

&nbsp;

## Número aleatorio

Para generar un número aleatorio se utiliza la función **random**, que recibe un parámetro representando el valor máximo del rango en que debe generarse el número, tomando como valor mínimo al 0. Por ejemplo, con _random(100)_ se obtendrá un número al azar entre 0 y 100.

Como la función sólo acepta un parámetro, si se quisiera determinar un rango con un valor mínimo y uno máximo, se debe hacer máximo - mínimo y obtener un número aleatorio en ese rango. Luego, sumar el valor mínimo a ese resultado. Por ejemplo, para obtener un número aleatorio entre 450 y 500, como 500-400=50, se utilizará random(50) y se le sumará 400:

<pre><code>numeroEntre450Y500 := random(50) + 400</code></pre>

&nbsp;

&nbsp;
