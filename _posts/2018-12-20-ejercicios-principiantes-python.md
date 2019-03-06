---
layout: post
title: Ejercicios para principiantes, en Python
date: 2018-12-20 19:00:00
categories: ejercicios
tags: resolución_problemas algoritmos python
published: false
---

## Herramientas
Podés resolver los ejercicios descargando Python y generando, por cada ejercicio, un archivo con extensión .py y ejecutándolo mediante el intérprete de Python. Sin embargo, también es posible resolver los ejercicios en cualquier intérprete de Python online, sin necesidad de descargar nada, por ejemplo: Repl.it[https://repl.it/languages/python3]. Cada ejercicio de esta página constituye un programa.

&nbsp;
## Importante
Cuando resuelvas los ejercicios estarás actuando como el “programador” (la persona que crea el programa). Pero luego tendrás que ejecutar tu código y probar si funciona correctamente, y en este caso actuarás como el “usuario” (alguien que utiliza el programa). No siempre el programador y el usuario son la misma persona y, generalmente, los usuarios no conocen los detalles técnicos ni pueden ver el código. Sólo verán la salida en pantalla que les muestre el programa.
Considerá que, en cada ejecución del programa, el usuario podría ingresar datos diferentes. El programa debería funcionar de forma consistente y sin errores en todos los casos.

&nbsp;
## Sobre los ejercicios
Junto a los ejercicios se encuentran algunos ejemplos con explicaciones, a modo de guía para su resolución. 
Además, por cada ejercicio se muestra un ejemplo de salida en pantalla indicando cómo debería quedar el programa luego de su ejecución. El texto en negrita representa la salida del programa y el texto en cursiva representa el texto ingresado por el usuario.

&nbsp;
## Soluciones
Haciendo click sobre cada ejercicio se desplegará su solución. Es importante tener en cuenta que, en algunos casos, es posible obtener el mismo resultado utilizando diferentes estrategias o algoritmos. En este caso se plantea una solución posible para cada ejercicio.

<hr>

# Sección 1
**Entrada/salida de datos - Variables - Tipos de datos**
<pre><code>Variable=5
variable=3
VaRiAbLe=8
#Son todas variables distintas porque Python (como muchos otros lenguajes) distingue mayúsculas y minúsculas.</code></pre>

<pre><code>a=5
a=18
#a tomará el último valor asignado (lo que tuviera guardado anteriormente la variable, se pierde).</code></pre>

---

### 1
<details> 
  <summary>Escribí un programa que solicite al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada nombre.
A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.

*Ejemplo de ejecución:*
> **Tu nombre:** _Patricia_
> <br> **Ahora estás en la matrix, Patricia**</summary>
<br>Solución:
<pre><code>nombre=input("Tu nombre:")
    print("Ahora estás en la matrix,", nombre)
        print("Ahora estás en la matrix,", nombre)</code></pre>
</details>

---

<pre><code>
1variable=23.95
#Arroja error porque los nombres de variables sólo pueden comenzar con letras o guiones bajos (_).
</code></pre>

<pre><code>
n1=int(input())
n2=float(input())
#Sabemos que input() lee lo que el usuario escribe en el programa, pero el tipo de eso que lee será siempre string. Si necesitamos que sea un número debemos convertir lo que input() devuelve. Para convertir a número entero usamos int(input()) y para convertir a número con decimales usamos float(input()).
</code></pre>

---

### 2
<details> 
  <summary>Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación.

*Ejemplo de ejecución:*
> **Primer número:** _14.2_
> <br> **Segundo número:** _19_
> <br> **El resultado de la suma es 33.2**
</summary>
<br>Solución:
<pre><code>
a=float(input("Primer número:"))
b=int(input("Segundo número:"))
c=a+b
print("El resultado de la suma es", c)
</code></pre>
</details>


### 3
<details> 
  <summary>Escribí un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

*Ejemplo de ejecución:*
> **Ingresá un número:** _1_
> <br> **Ingresá otro número:** _2_
> <br> **Suman: 3**
> <br> **Ingresá un nuevo número:** _3_
> <br> **Multiplicación de la suma por el último número: 9**
</summary>
<br>Solución:
<pre><code>
n1=int(input("Ingresá un número:"))
n2=int(input("Ingresá otro número:"))
suma=n1+n2
print("Suman:", suma)
n3=int(input("Ingresá un nuevo número:"))
print("Multiplicación de la suma por el último número:",suma*n3)
</code></pre>
</details>

---

<pre><code>
a=a+1
a+=1
#Las dos instrucciones de arriba son equivalentes (cualquiera de ellas hace lo mismo: sumar 1 al valor almacenado en la variable a y reemplazar el valor anterior de a con el nuevo resultado).
</code></pre>

---

### 4
<details> 
  <summary>Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.

*Ejemplo de ejecución:*
> Kilómetros recorridos: 260
> <br> **Litros de combustible gastados:** _12.5_
> <br> **El consumo por kilómetro es de 20.8**
</summary>
<br>Solución:
<pre><code>
kilometros=float(input("Kilómetros recorridos:"))
litros=float(input("Litros de combustible gastados:"))
print("El consumo por kilómetro es de", kilometros/litros)
</code></pre>
</details>



### 5
<details> 
  <summary>Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: Celsius = (5/9) * (Fahrenheit-32)
    
*Ejemplo de ejecución:*
> **Ingresá una temperatura expresada en Farenheit:** _75_
> <br> **23.88888888888889**
</summary>
<br>Solución:
<pre><code>
Fahrenheit=float(input("Ingresá una temperatura expresada en Fahrenheit:"))
print((5/9) * (Fahrenheit-32))
</code></pre>
</details>


### 6
<details> 
  <summary>Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres. 
    
*Ejemplo de ejecución:*
> **Primer número:** _8.5_
> <br> **Segundo número:** _10_
> <br> **Tercer número:** _5.5_
> <br> **El promedio de los tres es 8.0**
</summary>
<br>Solución:
<pre><code>
n1=float(input("Primer número:"))
n2=float(input("Segundo número:"))
n3=float(input("Tercer número:"))
print("El promedio de los tres es", (n1+n2+n3)/3)
</code></pre>
</details>


### 7
<details> 
  <summary>Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla. 
    
*Ejemplo de ejecución:*
> **Ingresá un número:** _260_
> <br> **Descontando el 15% queda: 221.0**
</summary>
<br>Solución:
<pre><code>
numero=int(input("Ingresá un número:"))
print("Descontando el 15% queda:", numero-(numero*15)/100)
</code></pre>
</details>

---

<pre><code>
cadena=""
cadena=cadena+"buen"
cadena=cadena+" día"
print(cadena)
#Cuando se utiliza el operador + en una operación entre strings, se está realizando una concatenación (unión de strings). La instrucción print mostrada arriba imprimirá “buen día”.
</code></pre>

---

<pre><code>
</code></pre>

<pre><code>
</code></pre>

<pre><code>
</code></pre>

<pre><code>
</code></pre>

<pre><code>
</code></pre>

<pre><code>
</code></pre>

<pre><code>
</code></pre>

<pre><code>
</code></pre>

<pre><code>
</code></pre>

<pre><code>
</code></pre>

<pre><code>
</code></pre>
