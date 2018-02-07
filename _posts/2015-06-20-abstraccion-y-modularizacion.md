---
layout: post
title: Abstracción y modularización
date: 2015-06-20 19:00:00
categories: conceptos
tags: abstracción buenas_prácticas resolución_problemas paradigma_imperativo
published: true
---

Cuando se divide un programa en módulos, la intención es crear una resolución de un problema "grande" a través de soluciones a cada una de sus partes por separado, para luego integrarlas a todas.

Un módulo puede ser cualquier parte de un programa que se encuentra "separada": es decir, para su utilización deberemos referir a esa otra parte, que se encuentra en otro lugar. En algunos casos se llama módulo a otros archivos; así, podríamos tener un programa grande dividido en varios archivos (por ejemplo, en el caso de un juego, un archivo para la pantalla de inicio, otro para la ayuda y otro para el juego concretamente). En otras ocasiones se denomina módulo a porciones de código que pueden estar o no dentro del mismo archivo donde se utilizan; tal es el caso de los subprogramas, rutinas, funciones, procedimientos, métodos. Es a este último tipo de módulos que nos referiremos en este artículo.

Según el lenguaje y el tipo de módulo del que estemos hablando, un módulo podría retornar un valor o no retornar nada (en Python este "nada" se representa con el valor <code>None</code>, en Java se representa con <code>void</code>, que indican que no hay ningún valor).

Donde en el código aparece una llamada (o "invocación") a una función, nosotros vemos esa abstracción, pero la computadora ve una indicación para ejecutar el código de la función y obtener un resultado. Entonces, cuando aparece una invocación a una función, se puede decir que, de manera abstracta, esa instrucción de invocación se "reemplaza" por el valor que la función retorna.

_Ejemplo 1:_

Supongamos una función muy simple en Python, que recibe dos parámetros, los suma y devuelve el resultado, como la que sigue:

<pre><code>def sumarDosNúmeros(numA, numB):
    return numA+numB</code></pre>

Esta función devuelve un número (el resultado de la suma de otros dos números). Entonces, podríamos usar esa función en una expresión, representando a un número:

<pre><code>4 + sumarDosNúmeros(5, 10)</code></pre>

En este caso, la computadora ve el 15 donde nosotros vemos la abstracción _sumarDosNúmeros(5, 10)_ y luego ve el 19 donde nosotros nos abstraemos para ver la expresión completa: 4 + sumarDosNúmeros(5, 10)

Esto suele ser muy útil cuando necesitamos procesar una condición compleja para usar en una iteración o en una selección, porque podemos crear un módulo que resuelva esa condición y devuelva el valor True si la condición se cumple o False si no se cumple. Por ejemplo, supongamos que le pedimos al usuario ingresar un número entero y lo guardamos en la variable llamada **num**. Y que queremos mostrar el mensaje "este número no me gusta" si se cumple la condición de que el número ingresado por el usuario tiene menos de 3 dígitos, es un múltiplo de 15 y no contiene ningún dígito 0. Si la condición no se cumple, entonces mostramos el mensaje "este número me gusta". Esta decisión podría escribirse con una estructura como la siguiente:

<pre><code>if condición:
    print("este número no me gusta")
else:
    print("este número me gusta")</code></pre>

Si recordamos que las estructuras como "if" o "while" requieren un valor booleano (True ó False) para decidir si ejecutan las instrucciones que contienen; entonces, en el fragmento de código anterior podemos deducir que **condición** es una variable booleana (contiene el valor True o el valor False) porque, cuando la computadora resuelva esa abstracción, reemplazará el nombre de la variable por su valor concreto. Por ejemplo, si _condición_ contiene el valor _True_, la computadora "verá":

<pre><code>if True:
    print("este número no me gusta")
else:
    print("este número me gusta")</code></pre>

Ahora, para lograr que la variable _condición_ contenga _True_ si la condición descripta en el enunciado es verdadera, o _False_ si la condición es falsa, podemos usar un módulo que lo determine, almacenando su valor de retorno en la variable:

<pre><code>condición = evaluarNúmero(num)</code></pre>

Sabemos, entonces, que la función llamada <code>evaluarNúmero(num)</code> se dedicará a comprobar si la condición se cumple o no, y retornará un valor booleano. Pero podemos dedicarnos a construir el resto del programa, dejando la función para después, y así escribir:

<pre><code>num = int(input())
condición = evaluarNúmero(num)
if condición:
    print("este número no me gusta")
else:
    print("este número me gusta")</code></pre>

O, lo que es equivalente:

<pre><code>num = int(input())
if evaluarNúmero(num):
    print("este número no me gusta")
else:
    print("este número me gusta")</code></pre>

¿Por qué es equivalente? Porque en realidad no necesitamos guardar el resultado de la función en una variable para después usarla: si sabemos que la llamada a la función es una abstracción que la máquina luego reemplaza por el valor que retorna, podemos deducir que donde dice _evaluarNúmero(num)_ habrá un _True_ o un _False_. Sería similar a escribir:

<pre><code>unValor = 4+11
if unValor==0</code></pre>

...que equivale a poner directamente

<pre><code>if 4+11==0</code></pre>

Ahora que ya tenemos la instrucción de selección que imprime un mensaje u otro dependiendo de si la condición se cumple o no, podemos dedicarnos a construir la función evaluarNúmero(num) que evalúe la condición y retorne True o False. Recordemos que la condición debe ser verdadera si se cumple que: el número ingresado por el usuario tiene menos de 3 dígitos, es un múltiplo de 15 y no contiene ningún dígito 0. Así que necesitamos construir un algoritmo como el siguiente dentro de la función:

<pre><code>def evaluarNúmero(num):
   if num/100 &lt; 1:        #Aclaración 1
      if num%15==0:              #Aclaración 2
          hayCero=False            #Aclaración 3
          while num != 0:
              ultimoDigito=num%10
              if ultimoDigito==0:
                  hayCero=True           #Aclaración 4
              num=num//10
          if hayCero:              #Aclaración 5
              return False
          else:                    #Aclaración 6
              return True
      else:
          return False       #Aclaración 7
   else:
      return False     #Aclaración 8</code></pre>

Las aclaraciones sobre cómo se construyó el algoritmo (escritas aparte para no "ensuciar" el código):

* Aclaración 1: un número de menos de 3 digitos tiene la particularidad de que, al dividirlo por 100, da un resultado menor a 1, entonces usamos esta estrategia.
* Aclaración 2: un número múltiplo de 15, al dividirlo por 15 da resto 0.
* Aclaración 3: vamos a empezar a buscar si hay algún cero, entonces, si lo encontramos, ponemos la variable _hayCero_ en True.
* Aclaración 4: si sucede que encuentra un cero en el número, entonces pone la variable hayCero en True.
* Aclaración 5: si hay algún 0, la condición no se cumple.
* Aclaración 6: si la variable hayCero tiene el valor False, la condición termina por cumplirse.
* Aclaración 7: si el número no es múltiplo de 15, la condición no se cumple.
* Aclaración 8: si el número no tiene menos de 3 dígitos, la condición no se cumple.
