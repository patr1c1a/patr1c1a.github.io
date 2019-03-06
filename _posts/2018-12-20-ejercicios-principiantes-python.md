---
layout: post
title: Ejercicios para principiantes, en Python
date: 2018-12-20 19:00:00
categories: ejercicios
tags: resolución_problemas algoritmos python
published: false
---

## Herramientas
Podés resolver los ejercicios descargando Python y generando, por cada ejercicio, un archivo con extensión .py y ejecutándolo mediante el intérprete de Python. Sin embargo, también es posible resolver los ejercicios en cualquier intérprete de Python online, sin necesidad de descargar nada, por ejemplo: Repl.it(https://repl.it/languages/python3). Cada ejercicio de esta página constituye un programa.

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
A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, _[usuario]_”, donde “_[usuario]_” se reemplazará por el nombre que el usuario haya ingresado.

*Ejemplo de ejecución:*
> **Tu nombre:** _Patricia_
> <br> **Ahora estás en la matrix, Patricia**</summary>
<br>Solución:
<pre><code>nombre=input("Tu nombre:")
    print("Ahora estás en la matrix,", nombre)
        print("Ahora estás en la matrix,", nombre)</code></pre>
</details>

---

**Código de ejemplo**
<pre><code>
1variable=23.95
#Arroja error porque los nombres de variables sólo pueden comenzar con letras o guiones bajos (_).
</code></pre>

**Código de ejemplo**
<pre><code>
n1=int(input())
n2=float(input())
#Sabemos que input() lee lo que el usuario escribe en el programa, pero el tipo de eso que lee será siempre string. Si necesitamos que sea un número debemos convertir lo que input() devuelve. Para convertir a número entero usamos int(input()) y para convertir a número con decimales usamos float(input()).
</code></pre>

---

### 2
<details> 
  <summary>Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es _[suma]_”, donde “_[suma]_” se reemplazará por el resultado de la operación.

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
<br>A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

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

**Código de ejemplo**
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
  <summary>Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_
    
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

**Código de ejemplo**
<pre><code>
cadena=""
cadena=cadena+"buen"
cadena=cadena+" día"
print(cadena)
#Cuando se utiliza el operador + en una operación entre strings, se está realizando una concatenación (unión de strings). La instrucción print mostrada arriba imprimirá “buen día”.
</code></pre>

---

### 8
<details> 
  <summary>Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se guardarán en dos variables distintas. A continuación, almacená en una variable la concatenación de la primera palabra, más un espacio, más la segunda palabra. Mostrá este resultado en pantalla. 
    
*Ejemplo de ejecución:*
> **Primera palabra:** _derribando_
> <br> **Segunda palabra:** _muros_
> <br> **derribando muros**
</summary>
<br>Solución:
<pre><code>
palabra1=input("Primera palabra:")
palabra2=input("Segunda palabra:")
frase=palabra1+" "+palabra2
print(frase)
</code></pre>
</details>

---

**Código de ejemplo**
<pre><code>
frase="Estoy programando"
print(frase[0])
i=6
print(frase[i])
#El operador [ ] (corchetes) permite obtener un carácter a partir de un string. La posición del carácter se indica entre los corchetes, ya sea ingresando directamente el número, con una variable que contenga un número o con una operación que de como resultado un número. Siempre, el primer carácter de un string estará ubicado en la posición 0.
</code></pre>

**Código de ejemplo**
<pre><code>
frase="Estoy programando"
print(len(frase))
ultimo_caracter=frase[len(frase)-1]
print(ultimo_caracter)
#Mediante len() podemos obtener la cantidad de caracteres que contiene un string. Este valor siempre será un número entero (tipo int) y puede guardarse en una variable, imprimirse, usarse en una operación aritmética, etc.
</code></pre>

---

### 9
<details> 
  <summary>Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado.
Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada _indice_.
<br>Mostrar en pantalla el carácter del texto ubicado en la posición dada por _indice_.

*Ejemplo de ejecución:*
> **Ingresá un texto:** _En un lugar de la Mancha, de cuyo nombre no quiero acordarme..._
> <br> **El carácter en primer lugar es: E**
> <br> **Ingresá un número positivo menor a 63**
> <br> _7_
> <br> **El carácter en esa posición es: u**
</summary>
<br>Solución:
<pre><code>
cadena=input("Ingresá un texto:")
print("El carácter en primer lugar es:", cadena[0])
print("Ingresá un número positivo menor a", len(cadena))
indice=int(input())
print("El carácter en esa posición es:", cadena[indice])
</code></pre>
</details>

---

**Código de ejemplo**
<pre><code>
a=10
b=4
print(a != b)
#La instrucción print imprimirá True, ya que el valor contenido en a es diferente del valor contenido en b.
</code></pre>

---

### 10
<details> 
  <summary>Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.

*Ejemplo de ejecución:*
> **Shows vistos en el último año:** _3_
> <br> **False**
</summary>
<br>Solución:
<pre><code>
shows=int(input("Shows vistos en el último año:"))
print(shows>3)
</code></pre>
</details>

---

**Código de ejemplo**
<pre><code>
print(58273%10)
print(58273//10)
#La primera instrucción imprimirá el número 3, ya que es el resto de la división de 58273 por 10. La segunda instrucción imprimirá 5827, ya que es la parte entera del resultado de dividir 58273 por 10. Estas operaciones matemáticas son estrategias que se pueden utilizar para obtener partes de un número.
</code></pre>

---

### 11
<details> 
  <summary>Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (_DDMMAAAA_). Este dato debe guardarse en una variable con tipo int (número entero). Finalmente, mostrar al usuario la fecha con el formato _DD / MM / AAAA_.

*Ejemplo de ejecución:*
> **Fecha en formato DDMMAAAA:** _16112017_
> <br> **16 / 11 / 2017**
</summary>
<br>Solución:
<pre><code>
fecha=int(input("Fecha en formato DDMMAAAA:"))
año=fecha%10000
dia=fecha//1000000
mes=(fecha//10000)%100
print(dia,"/",mes,"/",año)
</code></pre>
</details>


### 12
<details> 
  <summary>Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad dependiendo de si el número es par o no. Recordar que un número es par si el resto, al dividirlo por 2, es 0.

*Ejemplo de ejecución:*
> **Número entero:** _7254_
> <br> **True**
</summary>
<br>Solución:
<pre><code>
numero=int(input("Número entero:"))
print((numero%2) == 0)
</code></pre>
</details>


---

**Código de ejemplo**
<pre><code>

a=int(input())
print(a>100  and  a!=1000)
#Primero se calcularán los valores lógicos (True o False) de las dos comparaciones: a > 100 y a != 1000 (lo cual dependerá del número guardado en la variable a). A continuación, se utilizará la tabla de verdad de la operación AND para calcular el resultado.
</code></pre>

---

### 13
<details> 
  <summary>Escribí un programa que le solicite al usuario su edad y la guarde en una variable. Que luego solicite la cantidad de artículos comprados en una tienda y la guarde en otra variable. Finalmente, mostrar en pantalla un valor de verdad (True o False) que indique si el usuario es mayor de 18 años de edad y además compró más de 1 artículo.

*Ejemplo de ejecución:*
> **Tu edad:** _32_
> <br> **Artículos comprados:** _1_
> <br> **False**
</summary>
<br>Solución:
<pre><code>
edad=int(input("Tu edad:"))
articulos=int(input("Artículos comprados:"))
print((edad>18) and (articulos>1))
</code></pre>
</details>

---

### 14
<details> 
  <summary>Escribí un programa que, dada una cadena de texto por el usuario, imprima True si la cantidad de caracteres en la cadena es un número impar, o False si no lo es.

*Ejemplo de ejecución:*
> **Ingresá una frase:** _Era el mejor de los tiempos, era el peor de los tiempos._
> <br> **True**
</summary>
<br>Solución:
<pre><code>
cadena=input("Ingresá una frase:")
longitud=len(cadena)
print(longitud%2 == 0)
</code></pre>
</details>

---

**Código de ejemplo**
<pre><code>
"animal" > "piedra"
"bailar” > "bebida"
#Ambas comparaciones arrojan True porque el string “animal” es menor que “piedra” y el string “bailar” es menor que “bebida”. El orden está dado por cómo aparecen las letras en el alfabeto. En el caso de “animal” y “piedra”, la “a” es menor que la “p”. En el caso de “bailar” y “bebida”, como la primera letra es la misma se evalúa la segunda, y en este caso “a” es menor que “e”.
</code></pre>

---

### 15
<details> 
  <summary>Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es. 

*Ejemplo de ejecución:*
> **Una palabra:** _complejidad_
> <br> **Otra palabra:** _algoritmo_
> <br> **False**
</summary>
<br>Solución:
<pre><code>
palabra1=input("Una palabra:")
palabra2=input("Otra palabra:")
print(palabra1<palabra2)
</code></pre>
</details>


### 16
<details> 
  <summary>Escribí un programa para pedir al usuario su nombre y luego el nombre de otra persona, almacenando cada nombre en una variable. Luego mostrar en pantalla un valor de verdad que indique si: los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Por ejemplo, si los nombres ingresados son _María_ y _Marcos_, se mostrará True, ya que ambos comienzan con la misma letra. Si los nombres son _Ricardo_ y_ Gonzalo_ se mostrará True, ya que ambos terminan con la misma letra. Si los nombres son _Florencia_ y _Lautaro_ se mostrará False, ya que no coinciden ni la primera ni la última letra.

*Ejemplo de ejecución:*
> **Tu nombre:** _Alfredo_
> <br> **Otro nombre:** _Eduardo_
> <br> **True**
</summary>
<br>Solución:
<pre><code>
nombre1=input("Tu nombre:")
nombre2=input("Otro nombre:")
posicion_final_nombre1=len(nombre1)-1
posicion_final_nombre2=len(nombre2)-1
print((nombre1[0] == nombre2[0]) or (nombre1[posicion_final_nombre1] == nombre2[posicion_final_nombre2]))
</code></pre>
</details>



---

### N
<details> 
  <summary>

*Ejemplo de ejecución:*
> **
> <br> **
</summary>
<br>Solución:
<pre><code>

</code></pre>
</details>

