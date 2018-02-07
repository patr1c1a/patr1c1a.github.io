---
layout: post
title: Estructuras de control
date: 2015-06-23 19:00:00
categories: conceptos
tags: paradigma_imperativo selección bucles loops if case switch for while
published: true
---


La **programación imperativa** consiste en dar una serie de instrucciones para que la computadora las ejecute en el orden en que aparecen. Dentro de ésta, la **programación procedural** agrega la posibilidad de usar procedimientos (funciones). Ahondando un poco más, la **programación estructurada** elimina la posibilidad de utilizar la estructura "_goto_" ("go to" ó "ir a"), que se considera una mala práctica debido a que hace que la ejecución de un programa sea impredecible (por lo tanto, difícil de probar y mantener).

Algunos lenguajes que siguen el paradigma imperativo (parte de ellos, además, son orientados a objetos): C, C++, Pascal, Java, C#, Python, VB.Net, PHP, Javascript.

La programación imperativa tiene 3 tipos principales de estructuras de control: secuencias, selecciones e iteraciones.

 

## Secuencia

Una secuencia no es más que una sucesión de órdenes, ejecutadas una tras otra, y es la base de la programación imperativa.

El programa comienza por un punto de inicio y, de ahí en más, ejecuta cada instrucción en el orden en que aparece. Las instrucciones se leen y ejecutan de arriba hacia abajo.

_Ejemplo 1:_

<pre><code>ESCRIBIR "Ingrese su nombre: "
LEER nombre
ESCRIBIR "Hola ", nombre, "!"</code></pre>

En este ejemplo, en primer lugar se escribe en la pantalla un texto, en segundo lugar se lee un dato que el usuario ingresa con el teclado y se lo almacena en la variable "nombre" y, por último, se escribe el texto "Hola ", seguido del valor de la variable "nombre", seguido del símbolo "!".

 

## Selección (o "decisión")

La selección permite decidir qué camino tomar en base a alguna condición. Es decir, la secuencia en este caso se "rompe" para tomar un camino y no el otro.

Generalmente, hay dos tipos de selecciones: simples y múltiples. En la simple se barajan dos opciones: algo es _verdadero_ o es _falso_, y se ejecutan ciertas acciones dependiendo de cuál es el valor de verdad. En la múltiple existen varias opciones que pueden ser verdaderas y, habitualmente, una opción por descarte (si todas las demás opciones son falsas).

 

### Selección simple:

En la mayor parte de los lenguajes la selección simple es indicada con la palabra reservada **IF** que, en inglés, significa "si" (condicional). A este "if" le sigue la **condición** que debe cumplirse para que se ejecuten las instrucciones a continuación. Es decir, lo que sigue al "if" será alguna expresión que pueda tener valor de verdad (_Verdadero_ o _Falso_). En algunos lenguajes, luego de la condición y antes de las instrucciones condicionadas se utiliza la palabra **THEN** ("entonces" en inglés).

_Ejemplo 2:_

<pre><code>ESCRIBIR "Precio: $"
LEER precio
SI precio > 1000 ENTONCES:
    precio=precio-(precio*0.10)</code></pre>

En el pseudocódigo del ejemplo 2 se escribe en la pantalla un texto y luego se lee del teclado un número que el usuario ingresa, almacenándolo en la variable "precio". A continuación, una selección evalúa la condición: _precio > 1000_ y, si ésta resulta ser _verdadera_ (es decir, si el número almacenado en la variable _precio_ es mayor al número 1000), se ejecuta lo que sigue a continuación (la instrucción indica que se le reste un 10% al valor almacenado en "precio" y el resultado se guarde en la misma variable). Si la condición resultara _falsa_, la instrucción incluida dentro de la estructura IF no se ejecutaría y el programa continuaría con la siguiente instrucción fuera del IF.

También es posible indicar qué hacer en caso de que la condición resulte _falsa_, aunque no es obligatorio. Esto se hace utilizando un bloque de instrucciones **ELSE** ("si no" en inglés -muchas veces [confundido con la conjunción "sino"](http://www.fundeu.es/recomendacion/sinoy-si-no-941/) de nuestro idioma español-) :

_Ejemplo 3:_

<pre><code>ESCRIBIR "Precio: $"
LEER precio
SI precio > 1000 ENTONCES:
    precio=precio-(precio*0.10)
SI NO:
    precio=precio-(precio*0.02)</code></pre>

A diferencia del ejemplo 2, la condición se evalúa y, si resulta verdadera se ejecuta la instrucción <code>precio=precio-(precio*0.1)</code> pero, si la condición resulta falsa (es decir, si el número almacenado en "precio" no es mayor que el número 1000), se ejecuta la instrucción <code>precio=precio-(precio*0.02)</code> (que resta el 2% del precio y almacena el resultado en la misma variable).

La selección simple se utiliza cuando sólo hay dos opciones posibles: algo es verdadero o es falso, es blanco o es negro, es "sí" o es "no" (lo que se representa con los _valores booleanos_ "True" y "False"). Si, por ejemplo, debiéramos ejecutar ciertas instrucciones si un número es par y otro grupo de instrucciones si el número es impar, podríamos usar IF-ELSE, ya que decir que un número es impar equivale a decir que no es par (esto es, que la condición "el número es par" resulta falsa).

 

### Selección múltiple:

Cada lenguaje suele tener su propia sintaxis para este tipo de selección (no es tan generalizado como el uso de la palabra "if" para la selección simple): "case", "switch" y "select" son las más comunes. Pero esto es sólo cuestión de terminología. Lo importante es que, en este caso existe más de una posibilidad al evaluar una condición. En realidad, los valores de verdad siguen siendo sólo dos, _verdadero_ y _falso_, pero se construyen varias condiciones, las cuales pueden resultar verdaderas o falsas cada una de ellas y que, cada una tiene un grupo de instrucciones a ejecutar si la condición resulta verdadera. En el código se especifican los distintos casos posibles que podrían darse y las instrucciones a ejecutar si ese caso resultara verdadero.

_Ejemplo 4:_

<pre><code>ESCRIBIR "Precio: $"
LEER precio
SELECCIÓN precio:
    CASO precio < 1000:
        precio=precio-(precio*0.02)
    CASO (precio >= 1000) Y (precio < 5000):
        precio=precio-(precio*0.10)
    CASO precio >= 5000:
        precio=precio-(precio*0.20)
</code></pre>

En el ejemplo 4 vemos que se evalúan tres posibilidades: que el valor de "precio" sea menor a 1000 (en cuyo caso se descuenta un 2%), que esté entre 1000 inclusive y 5000 -es decir, que sea mayor o igual a 1000 y menor a 5000- (en cuyo caso se descuenta un 10%) o que sea mayor o igual a 5000 (en cuyo caso se descuenta un 20%).

Idealmente, sólo una de todas debería resultar verdadera y las demás resultar falsas, entonces se selecciona esa opción para ejecutar sus instrucciones. Si la selección está mal construida y existe la posibilidad de que más de una opción resulte verdadera (por ejemplo, si en la línea 3 se hubiera colocado el operador **<=**, el valor 1000 en "precio" haría que tanto la primera como la segunda opción sean verdaderas), normalmente sólo se ejecutará la que se encuentre primero, ya que las instrucciones se ejecutan en orden secuencial y en una selección sólo se ejecuta una de ellas (esto puede variar según el lenguaje).

A simple vista, podría parecer que el código del ejemplo 4 (con una única selección múltiple) es equivalente al del ejemplo 5 a continuación (que usa tres selecciones simples separadas):

_Ejemplo 5:_

<pre><code>ESCRIBIR "Precio: $"
LEER precio
SI precio < 1000 ENTONCES:
        precio=precio-(precio*0.02)
SI (precio >= 1000) Y (precio < 5000) ENTONCES:
        precio=precio-(precio*0.10)
SI precio >= 5000 ENTONCES:
        precio=precio-(precio*0.20)</code></pre>

Pero hay algunas diferencias: la primera es que, si las condiciones no fueran perfectamente excluyentes (como en la condición mal construida explicada arriba), el ejemplo 5 conduciría a que se ejecute más de un caso.

Por otra parte, puede haber diferencias en cuanto al tiempo de procesamiento utilizado. En muchos lenguajes, con una selección múltiple el procesador sólo evalúa casos hasta encontrar uno que resulte verdadero, y el resto se pasa por alto; pero, en el ejemplo 5, todas las condiciones deben ser evaluadas (porque son selecciones separadas). Entonces, en cuanto a procesamiento, el ejemplo 4 y el ejemplo 5 sólo serían equivalentes si el que se cumple es el último caso (precio es mayor o igual a 5000) debido a que, al llegar a ese punto, debieron haberse evaluado todos los casos previos. Pero, si el caso es el primero (precio es menor a 1000), en el ejemplo 4 dejan de evaluarse las siguientes condiciones y en ejemplo 5 se evalúan todas, a pesar de que ya se encontró la verdadera.

 

## Iteración ("repetición" o "bucle")

Cuando una instrucción o un grupo de ellas deben ejecutarse repetidas veces de manera consecutiva, pueden usarse repeticiones que permiten escribir las instrucciones una única vez e indicar cómo repetirlas.

Existen dos formas básicas de repetición: fija y condicional.

 

### Repetición fija

Antes de comenzar la iteración es posible conocer la cantidad de iteraciones a realizar. Por ejemplo, si el número es un literal, o si le solicitamos al usuario que indique cuántas veces desea repetir algo, o si ese número lo obtenemos mediante una operación o una función. La palabra que suele usarse para indicar este tipo de repetición, en la mayor parte de los lenguajes, es **FOR** ("para"). Normalmente, se utiliza una variable que hará las veces de contador (por costumbre, suele llamarse "i"). Si no se indica lo contrario, esta variable suele comenzar en 0 y aumentar de 1 en 1, hasta llegar a la cantidad de repeticiones indicadas.

En muchos lenguajes se permite que la variable comience en otro número que no sea 0, o que aumente de n en n (por ejemplo, de 2 en 2) o, incluso, que tome los valores de cierto rango de elementos, en vez de ser un contador numérico.

_Ejemplo 6:_

<pre><code>PARA i DESDE 0 HASTA 30 HACER:
   ESCRIBIR "Esta es la línea número ", i</code></pre>

Esto imprime "Esta es la línea número _xxx_" (donde **xxx** representa un número entre 0 y 30, contenido en la variable **i**).

En lenguajes como Python se permite iterar por los elementos de algún tipo de secuencia, y la variable iteradora toma como valor cada uno de dichos elementos. Por ejemplo, los strings se consideran secuencias, entonces se podría iterar de manera que la variable (_i_ o como el programador desee llamarla) tome como valores cada uno de los caracteres que componen al string, en el orden en que aparecen.

_Ejemplo 7:_

<pre><code>PARA i EN "este string" HACER:
   ESCRIBIR "El siguiente carácter es parte del string: ", i</code></pre>

En este caso, la variable i tomará como valor, en la primera iteración, la letra "e", en la segunda iteración la letra "s", en la tercera la "y", y así con cada uno de los caracteres que conforman el string. Si la secuencia es un contenedor (lista, tupla, diccionario...) entonces la variable tomará como valor cada uno de los elementos dentro del contenedor.

 

### Repetición condicional

En este caso, las instrucciones se repiten siempre que una condición resulte verdadera. Normalmente se usa la palabra reservada **WHILE** ("mientras"), seguida de una expresión booleana (similar a lo que sucede con el **IF**). La expresión se evalúa y, mientras resulte _verdadera_, las instrucciones del bloque _while_ se ejecutan, cortando la repetición cuando la expresión se vuelve _falsa_. Entonces, se debe prestar atención a que la expresión (operación, variable, llamada a función...) debe tener la posibilidad de volverse _falsa_ en algún momento, para que la repetición pueda cortarse.

_Ejemplo 8:_

<pre><code>LEER número
MIENTRAS número > 0 HACER:
   ESCRIBIR "repitiendo..."</code></pre>

En el ejemplo 8 vemos que, una vez ingresado el valor de la variable _número_, ese valor no cambia (ya que no hay una nueva instrucción que asigne otro valor a la variable), lo que conduce a un _bucle infinito_.

Para corregir esto, debería darse la posibilidad de que la variable _número_ cambie su valor dentro de la repetición para que, en algún momento, pueda volverse _falsa_. Por ejemplo, si se pide al usuario que ingrese un nuevo valor y se almacena en la variable, podría suceder que ese valor no cumpla la condición.

_Ejemplo 9:_

<pre><code>LEER número
MIENTRAS número > 0 HACER:
    ESCRIBIR "repitiendo..."
    LEER número</code></pre>

En el ejemplo 9, el valor de la variable número va cambiando cada vez que el usuario ingresa un nuevo valor. Supongamos que, en la línea 1 el usuario ingresa el número _10_. Cuando, en la línea 2 se resuelve la expresión _número > 0_, ésta resulta verdadera (ya que 10 es mayor que 0) y se ejecutan las instrucciones dentro de la repetición: se escribe en pantalla "repitiendo..." (línea 3) y luego se vuelve a solicitar al usuario que ingrese un valor, el cual se guarda en la variable _número_, reemplazando al valor anterior (línea 4). Entonces, la repetición hace que vuelva a evaluarse la expresión:Â _número > 0_. Supongamos que, en la línea 4, el usuario ingresó el valor _-25_, al volver a evaluarse la expresión, resulta _falsa_ (ya que -25 no es mayor que 0) y la repetición deja de ejecutarse, pasando a la instrucción que sigue (la línea a continuación, que sería la 5).

También se puede utilizar, en el lugar de la expresión, el valor literal _Verdadero_ ("true"), con lo cual debe existir otra forma de corte de la iteración (ver "break").

 

### Corte de iteraciones: "break" y "continue"

En los lenguajes que las admiten, la sentencia **BREAK** ("romper") permite interrumpir un bucle (sea una repetición fija o una repetición condicional).

_Ejemplo 10:_

<pre>MIENTRAS Verdadero:
    LEER número
    SI número < 0 ENTONCES:
        CORTAR
    ESCRIBIR "repitiendo..."</code></pre>

En el ejemplo 10 se ingresa indefectiblemente en la repetición condicional, ya que la expresión contiene el literal "_Verdadero_". Luego se lee un número ingresado por el usuario y, a continuación, se efectúa una selección para evaluar si se cumple la condición (pero ya dentro de la repetición). Si la condición resulta verdadera, se corta la repetición (observar que la condición en este caso es la inversa a la utilizada en los ejemplos 8 y 9, ya que en este caso la condición se debe cumplir para interrumpir el bucle). Si la condición evaluada resulta falsa, entonces el bucle no se corta y pasa a ejecutarse la siguiente línea dentro del bucle (línea 5).

El caso de **CONTINUE** ("continuar") permite saltear el resto de las instrucciones de repetición, pasando directamente a la siguiente iteración.

_Ejemplo 11:_

<pre><code>PARA i DESDE 0 HASTA 10 HACER:
    LEER número
    SI número < 0 ENTONCES:
        CONTINUAR
    ESCRIBIR "repitiendo..."</code></pre>

En este caso, se repetirá el bloque 10 veces (si es un lenguaje como Python, que toma el rango numérico como intervalo abierto). La primera instrucción pide que el usuario ingrese un valor y éste se guarda en la variable _número_. Luego se evalúa si ese valor es negativo (menor que 0), en cuyo caso se saltea la instrucción de la línea 5 y se pasa a la siguiente iteración, volviendo a leer un valor y almacenándolo en la variable _número_.

Habitualmente se dice que "break" y "continue" son malas prácticas de programación, pero una buena excepción puede ser cuando ayudan a que el código sea más legible y conciso. Lo cierto es que, normalmente, puede encontrarse un algoritmo equivalente sin utilizar "break" ni "continue".

 

## Bloques

Un bloque de código es un conjunto de instrucciones que tienen sentido en forma agrupada. Por ejemplo, las sentencias que se ejecutan dentro de una estructura"if" constituyen un bloque y las que se ejecutan dentro de un "else" son otro bloque. Un bloque podría tener una única instrucción y cada lenguaje define cómo delimitar los bloques: algunos lo hacen mediante llaves { } (como Java), otros mediante sangría o "indentación" (como Python), algunos mediante palabras clave (como Pascal).

Los bloques pueden anidarse, esto es: un bloque puede estar contenido dentro de otro bloque. Y así podríamos ver una estructura "while" que en su bloque de instrucciones contiene a una estructura "if" o, incluso, a otro "while".
