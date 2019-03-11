---
layout: post
title: Ejercicios resueltos de if-else-elif ("selección" ó "decisión") en Python
date: 2019-02-26
categories: ejercicios python
tags: algoritmo estructura if selección decisión
published: true
---

Acá encontrarás ejercicios para practicar la estructura de control de decisión o selección (if-else-elif).

En los siguientes videos podrás ver una explicación de la estructura de selección y también la resolución paso a paso de estos ejercicios:
+ [Selección o decisión: if, if-else, if-elif-else](https://www.youtube.com/watch?v=kIkAhld32O8)
+ [Ejercicios con la estructura de selección](https://www.youtube.com/watch?v=PKFKoAN2zEo)
+ [Ejercicio con la estructura de selección](https://www.youtube.com/watch?v=HMfaVLkjIUA)

La resolución de cada ejercicio se muestra al hacer click sobre la consigna.

### 1
<details> 
  <summary>Solicitar al usuario un número de cliente. Si el número es el 1000, imprimir "Ganaste un premio".</summary>
<br>Solución:
<pre><code>numero=int(input("N. de cliente:"))
if numero==1000:
    print("Ganaste un premio!")</code></pre>
</details>


### 2
<details> 
  <summary>Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. No considerar el caso en que ambos números son iguales.</summary>
<br>Solución:
<pre><code>a=int(input("Ingresa un número:"))
b=int(input("Ingresa un número:"))
if a<b:
    print("el primero es menor")
else:
    print("el segundo es menor")</code></pre>
</details>



### 3
<details> 
  <summary>Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales.</summary>
<br>Solución:
<pre><code>a=int(input("Un número:"))
b=int(input("Otro número:"))
if a<b:
    print("El primero es menor")
elif b<a:
	  print("El segundo es menor")
else:
	  print("Son iguales")</code></pre>
</details>


### 4
<details> 
  <summary>Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje</summary>
<br>Solución:
<pre><code>dia=input("Dia de la semana: ")
if (dia=="lunes"):
    print("Oh, no!")
elif (dia==”viernes”):
    print(“¡Ya casi!”)
elif (dia==”sábado” or “domingo”):
    print(“Ahora sí se puede descansar”)
else:
    print(“A esperar el fin de semana”)</code></pre>
</details>


### 5
<details> 
  <summary>Escribir un programa que, dado un número entero, muestre su valor absoluto.
Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).</summary>
<br>Solución:
<pre><code>numero=int(input("Número:"))
if numero<0:
    numero=numero*-1
print("Valor absoluto:", numero)</code></pre>
</details>


### 6
<details> 
  <summary>Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables.
A continuación, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Si no es así, imprimir “no hay coincidencia”.</summary>
<br>Solución:
<pre><code></code></pre>
</details>


### N
<details> 
  <summary></summary>
<br>Solución:
<pre><code></code></pre>
</details>
