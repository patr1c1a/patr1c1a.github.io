---
layout: post
title: Ejercicios resueltos de bucles "while" en Python
date: 2019-02-26 23:52
categories: ejercicios python
tags: algoritmo estructura repeticion bucle iteracion
published: true
---

Acá encontrarás ejercicios para practicar la estructura de control de bucle o repetición condicional (while).

En los siguientes videos podrás ver una explicación de la estructura y también la resolución paso a paso de estos ejercicios:
+ [Repetición condicional: while](https://youtu.be/Rkv3GtEZEnw)
+ [Ejercicios con la estructura de repetición condicional]
+ [Ejercicio con la estructura de repetición condicional]

La resolución de cada ejercicio se muestra al hacer click sobre la consigna.

### 1
<details> 
  <summary>Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.</summary>
  <pre><code>total=0
nro=int(input("Número: "))
while nro != 0:
    total+=nro
    nro=int(input("Número: "))</code></pre>
</details>


### 2
<details> 
  <summary>Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.</summary>
<br>Solución:
<pre><code>positivos=0
n=int(input("Número (0 para terminar): "))
while n!=0:
    if n>0:
        positivos+=1
    n=int(input("Número (0 para terminar): "))
print("Cantidad de positivos:", positivos)</code></pre>
</details>



### 3
<details> 
  <summary>Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.</summary>
<br>Solución:
<pre><code>mayor=-1
n=int(input("Número positivo:"))
while n>=0:
   if n>mayor:
       mayor=n
   n=int(input("Número positivo:"))
print("Mayor número ingresado:", mayor)</code></pre>
</details>


### 4
<details> 
  <summary>Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.</summary>
<br>Solución:
<pre><code>suma=0
n=int(input("Número positivo:"))
while n!=0:
    digito=n%10
    suma+=digito
    n=n//10
print("Suma de los dígitos:", suma)</code></pre>
</details>


### 5
<details> 
  <summary>Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.</summary>
<br>Solución:
<pre><code>pares=0
n=int(input("Número (-1 para terminar el programa): "))
while n!=-1:
    if n%2 == 0:
        pares+=1
    suma=0
    while n!=0:
        digito=n%10
        suma+=digito
        n=n//10
    print("Suma de sus dígitos:", suma)
    n=int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron", pares, "números pares")</code></pre>
</details>



### 6
<details> 
  <summary>Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.</summary>
<br>Solución:
<pre><code>while True:
    print("Opción 1 - comenzar programa")
    print("Opción 2 - imprimir listado")
    print("Opción 3 - finalizar programa")
    opcion=int(input("Opción elegida: "))
    if opcion==1:
        print("¡Comenzamos!")
    elif opcion==2:
        print("Listado:")
        print("Nadia, Esteban, Mariela, Fernanda")
    elif opcion==3:
        print("Hasta la próxima")
        break
    else:
        print("Opción incorrecta. Debe ingresar 1, 2 o 3")</code></pre>
</details>

### 7
<details> 
  <summary>Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.</summary>
<br>Solución:
<pre><code>frase=input("Frase: ")
l=input("Letra para buscar su posición: ")
i=0
while i!=len(frase):
    if l!=frase[i]:
        print("No se encontró en la posición", i)
        i+=1
        continue
    print("Se encontró en la posición", i)
    break</code></pre>
</details>

### 8
<details> 
  <summary>Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
<br />Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
</summary>
<br>Solución:
<pre><code>total=0
monto=float(input("Monto de una venta: $"))
while monto!=0:
    if monto<0:
        print("Monto no válido.")
    else:
        total+=monto
    monto=float(input("Monto de una venta: $"))
if total>1000:
    total-=total*0.1
print("Monto total a pagar: $", total)</code></pre>
</details>

### 9
<details> 
  <summary>Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
<br />Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
</summary>
<br>Solución:
<pre><code>numero=int(input("numero: "))
totalPares=0
totalImpares=0
while numero!=0:
   pares=0
   impares=0
   while numero!=0:   
     ultimodigito=numero%10
     if ultimodigito%2==0:
       pares+=1
       totalPares+=1
     else:
       impares+=1
       totalImpares+=1
     numero=numero//10
   print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
   numero=int(input("Otro número: "))
print("Total de dígitos pares:", totalPares)
print("Total de dígitos impares:", totalImpares)</code></pre>
</details>

### 10
<details> 
  <summary>Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea.Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
<br />**Ejemplo de ejecución:**
<br />Libro: Los 3 mosqueteros
<br />Libro: Historia de 2 ciudades
<br />Libro: /
<br />Línea completa. Aparecen 2 dígitos numéricos.
<br />Libro: 20000 leguas de viaje submarino
<br />Libro: El señor de los anillos
<br />Libro: /
<br />Línea completa. Aparecen 5 dígitos numéricos.
<br />Libro: 20 años después
<br />Libro: *
<br />Fin. Se leyeron 2 líneas completas.</summary>
<br>Solución:
<pre><code>lineas=0
digitos="0123456789"
cantidadDigitos=0
cadena=input("Cadena: ")
while cadena!="*":
    for caracter in cadena:
        if caracter in digitos:
            cantidadDigitos+=1
    if cadena=="/":
        lineas+=1
        print("Aparecen ", cantidadDigitos, " dígitos en la línea")
        cantidadDigitos=0
    cadena=input("Cadena: ")
print("Se leyeron ",lineas," líneas completas")</code></pre>
</details>


### 11
<details> 
  <summary>Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. 
Imprimir la cantidad de números primos ingresados.</summary>
<br>Solución:
<pre><code>cantidad=0
n=int(input("Número: "))
while n!=0:
 primo=True
 for i in range(2,n):
   if n%i==0:
     primo=False
     break
 if primo:
   cantidad+=1
 n=int(input("Número: "))
print("primos: ", cantidad)</code></pre>
</details>


### 12
<details> 
  <summary>Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.</summary>
<br>Solución:
<pre><code>anioInicio=int(input("Año inicial:"))
anioFin=int(input("Año final:"))
for anio in range(anioInicio, anioFin+1):
   if not anio%10==0:
       continue
   if not anio%4==0:
       continue
   if anio%100!=0 or anio%400==0:
       print(anio)</code></pre>
</details>


### 13
<details> 
  <summary>Escribir un programa que procese un texto. Se debe ofrecer al usuario un menú para realizar distintas funcionalidades  de forma iterativa:
<br />a) Ingresar texto a procesar.
<br />b) Imprimir la cantidad de consonantes en el texto.
<br />c) Imprimir la la cantidad de caracteres de cada palabra, cantidad de palabras en el texto y la palabra más larga.
<br />d) Imprimir la frecuencia de los caracteres repetidos en el texto (sólo una vez por cada carácter).
<br />e) Salir del programa.
<br />Se debe validar que la opción del menú elegida sea a, b, c, d ó e, dejando al usuario en un bucle en caso de ingreso inválido.
<br />Precondiciones: El texto no será vacío. Cada palabra estará delimitada por un espacio en blanco, sin importar si las palabras tienen sentido o no.
</summary>
<br>Solución:
<pre><code>cadena=""
while True:
  print("Seleccione opción:")
  print("a. Texto a procesar")
  print("b. Cantidad de consonantes en el texto")
  print("c. Cantidad de palabras, caracteres de cada palabra y palabra más larga")
  print("d. Caracteres repetidos")
  print("e. Salir del programa")

  #validación
  opcion=input()
  while len(opcion)!=1 or opcion not in "abcde":
      opcion=input("Ingreso no válido. Vuelva a intentar: ")

  if opcion=="a":
      cadena=input("Nuevo texto a procesar: ")

  elif opcion=="b":
      consonantes="bcdfghjklmnñpqrstvwxyz"
      cantConsonantes=0
      for caracter in cadena:
          if caracter in consonantes:
              cantConsonantes+=1
      print("Cantidad de consonantes", cantConsonantes)
    
  elif opcion=="c":
      palabraMasLarga=""
      lenMasLarga=0
      cantPalabras=0
      texto=cadena.strip()
      if len(texto)!=0:
          texto+=" "
      while " " in texto:
          cantPalabras+=1
          palabra=texto[0:texto.find(" ")]
          print("Cantidad de caracteres de",palabra, ":", len(palabra))
          if len(palabra) > lenMasLarga:
              lenMasLarga=len(palabra)
              palabraMasLarga=palabra
          texto=texto[texto.find(" ")+1:]
      print("Palabra mas larga: ",palabraMasLarga)
      print("Cantidad total de palabras: ",cantPalabras)

  elif opcion=="d":
      mostrados=""
      for c in cadena:
          if (cadena.count(c)>1) and (c not in mostrados):
              print("Cantidad de", c, ":", cadena.count(c))
              mostrados+=c
      if len(mostrados)==0:
          print("No hay caracteres repetidos")
  
  elif opcion=="e":
      break</code></pre>
</details>
