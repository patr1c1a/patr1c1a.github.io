---
layout: post
title: Ejercicio de examen, resuelto - Analizar código C
date: 2020-08-24 12:00:00
categories: ejercicios
tags: analizar
published: true
---


Veamos un ejercicio de examen de la Universidad de Washington, con su resolución. En esta oportunidad se busca analizar el código de un programa escrito en C.

✏️ Explicación del código:
<br />Las instrucciones <code>#define</code> se utilizan para crear macros. Una macro es un fragmento de código al que se le da un nombre y, cuando se usa ese nombre, se reemplaza textualmente por el código de la macro.
<br />Las macros de este ejercicio tienen parámetros pero no son exactamente iguales a una función, ya que siempre se hace un reemplazo textual del código. Es decir que, donde dice <code>FOO(a+b,c)</code>, debido a que **FOO** está definida como <code>FOO(x,y) x + y</code>, entonces **x** toma el valor de **a+b** mientras que **y** toma el valor de **c**. Haciendo un reemplazo textual nos queda <code>a+b+c</code>. Si **a=2**, **b=3**, **c=5** finalmente nos queda <code>2+3+5</code>.
<br />En el caso de <code>BAR(a+b,c)</code>, al estar definida como <code>BAR(x,y) y * x</code>, entonces se reemplaza **y** por **5**, mientras que **x** se reemplaza por **2+3**, lo que nos deja con <code>5\*2+3</code>. Teniendo en cuenta la precedencia de los operadores, calculamos <code>(5\*2)+3</code> y nos da 13.
<br />En la última operación, <code>BAR(FOO(a,c),BAR(b,b))</code>, el reemplazo hace que quede <code>BAR(2+5,3\*3)</code> que se expande luego a <code>3\*3\*2+5</code>, lo cual nos da como resultado 23 (porque se ejecuta primero 3*3*2 y luego a eso se le suman 5).

💻 [Ver el código en ejecución](https://repl.it/@programacionde1/EjUWCSE-374031512q2){:target="_blank"}

![Ejercicio resuelto de programación en C]({{ site.url }}/assets/2020-08-24-ejercicio-C-univ-washington.png)
