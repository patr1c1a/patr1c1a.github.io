---
layout: post
title: Ejercicios resueltos de funciones en Python
date: 2019-03-10 23:53
categories: ejercicios python
tags: algoritmo estructura funciones
published: true
---

Acá encontrarás ejercicios para practicar programar usando funciones.

En los siguientes videos podrás ver una explicación del tema y también la resolución paso a paso de estos ejercicios:
+ [Funciones](https://www.youtube.com/watch?v=IF34NgjldXs)
+ [Ejemplos de funciones](https://www.youtube.com/watch?v=ivcnLfOkbrU)
+ [Errores comunes con funciones](https://youtu.be/LD61E3g6GjM)

La resolución de cada ejercicio se muestra al hacer click sobre la consigna.

### 1
<details> 
  <summary>Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".</summary>
  <br>Solución:
  <pre><code>def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c==caracterBuscado:
            return True
    return False
<br>&nbsp;
direccion=input("Tu email: ")
if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")</code></pre>
</details>


### 2
<details> 
  <summary>Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).</summary>
<br>Solución:
<pre><code>def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
<br>&nbsp;
num=int(input("Número a procesar: "))
while num!=0:
	  print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar: "))</code></pre>
</details>



### 3
<details> 
  <summary>Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos.
Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.</summary>
<br>Solución:
<pre><code>def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
<br>&nbsp;
sumatoria=0
num=int(input("Número a procesar: "))
while num!=0:
	  print("Suma:",sumaDigitos(num))
    sumatoria=sumatoria+num
    num=int(input("Número a procesar: "))
print("Sumatoria:", sumatoria)
print("Dígitos:", sumaDigitos(sumatoria))</code></pre>
</details>


### 4
<details> 
  <summary>Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.</summary>
<br>Solución:
<pre><code>def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True
<br>&nbsp;
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")</code></pre>
</details>


### 5
<details> 
  <summary>Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.</summary>
<br>Solución:
<pre><code>def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad
<br>&nbsp;
num=int(input("Número: "))
un_digito=int(input("Dígito: "))
print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))</code></pre>
</details>


### 6
<details> 
  <summary>Escribir un programa que pida números al usuario,emuestra el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.</summary>
<br>Solución:
<pre><code>def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f
<br>&nbsp;
cantidad=0
num=int(input("Número (-1 para cortar): "))
while num!=-1:
    print("Factorial:", factorial(num))
    cantidad+=1
    num=int(input("Número (-1 para cortar): "))
print("Se leyeron",cantidad,"números")</code></pre>
</details>


### 7
<details> 
  <summary>Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.</summary>
<br>Solución:
<pre><code>def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma
<br>&nbsp;
cantidad=0
mayor=-1
numero=int(input("Número positivo: "))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma > mayor:
          mayor=suma
          n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
    numero=int(input("Número positivo: "))
print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
print("Cantidad con sumatoria menor a 10:",cantidad)</code></pre>
</details>


### 8
<details> 
  <summary>Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.</summary>
<br>Solución:
<pre><code>def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True
<br>&nbsp;
def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad
<br>&nbsp;
def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f
<br>&nbsp;
def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma
<br>&nbsp;
mayor=0
numero=int(input("Número primo: "))
while primo(numero):
    print("Suma de los dígitos:",sumaDigitos(numero))
    digito=int(input("Dígito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veces")
    if numero > mayor:
          mayor=numero
    numero=int(input("Número primo: "))
print("Factorial de",mayor,":",factorial(mayor))</code></pre>
</details>

