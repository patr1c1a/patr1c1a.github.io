---
layout: post
title: Construcción de un algoritmo
date: 2015-06-20 19:00:00
categories: conceptos
published: true
---


La computadora sólo sabe hacer operaciones aritméticas, operaciones lógicas y buscar cosas en la memoria, pero los lenguajes de alto nivel suelen tener muchas cosas construidas para que no tengamos que "reinventar la rueda" cada vez que empezamos a programar algo. Entonces, en un lenguaje como Java, C# o Python no necesitamos "decirle" a la computadora cómo obtener la longitud de un string, porque es una funcionalidad que el lenguaje ya provee. Pero, por ejemplo, si necesitamos saber si un número es par o impar, sí será necesario "decirle" a la computadora cómo. Para eso tenemos que buscar una estrategia: pensar qué características tienen los números pares que los distinguen de los impares. Entonces se podría usar la técnica de dividir al número por 2 y ver si el resto de la división es igual a cero (número par) o si el resto es distinto de cero (número impar).

Para indicarle estas cosas a la computadora puede que haya más de una forma válida, por eso es muy poco probable que dos personas programen algo de la misma manera.

Otras veces hay que usar operaciones más complejas que una simple operación aritmética. Para eso podemos utilizar [módulos](/conceptos/2015/06/20/abstraccion-y-modularizacion.html) ([funciones](/conceptos/2015/06/23/funciones.html), subprogramas, [métodos](/poo/2016/01/07/programacion-orientada-a-objetos.html), o el nombre específico según el lenguaje).

A veces, el lenguaje que estamos usando o sus librerías externas ya tienen funcionalidad agregada que podemos usar. Por ejemplo, podría darse que un lenguaje tuviera una función _par(número)_ que, dado un número, devuelva _True_ si éste es par o _False_ si es impar. Por esto es importante aprender a investigar la documentación del lenguaje y recordar que, la mayoría de las veces, los nombres de las funciones estarán en inglés (en vez de "par" la función podría llamarse "even", que es la misma palabra en inglés).


## Ejemplo práctico:

Construir un programa que reciba números (de cualquier cantidad de dígitos) a través del teclado hasta que se ingrese un número negativo (que no se procesa) y luego informe cuántos de esos números tenían el dígito "0" en ellos. Por ejemplo, si la secuencia que el usuario ingresa por el teclado es: 145, 8, 208, 30072, 496, -506 se debería informar que la cantidad de números que tenían el dígito "0" es 2 (ya que el -506 no se debe procesar, por lo tanto se encuentra un número que contiene el cero al leer el 208 y otro al leer el 30072).

Este enunciado podría analizarse de la siguiente forma:

  * Mi programa va a leer números del teclado hasta que se ingrese uno negativo. ¿Cómo le digo a la computadora que un número es negativo? Haciendo que verifique si es menor a cero.
  * Para que el usuario pueda ingresar más de un número voy a tener que hacer una repetición (también llamada "iteración", "ciclo", "bucle", "loop"&#8230;), porque es una parte del código que se va a ejecutar exactamente igual todas las veces, así que no tiene sentido escribir muchas veces lo mismo. Y como no sé cuántos números va a ingresar el usuario, necesitaré usar una repetición condicional. Entonces voy a usar una estructura "while" ("mientras"), y la condición para que un número se procese va a ser que sea mayor o igual a 0 (es decir, que no sea negativo).
  * ¿Qué cosas voy a poner dentro de la repetición? Voy a tener que ver qué cosas es necesario hacer más de una vez y cuáles no. Las que voy a tener que repetir son: 
      * Leer un número del teclado
      * Ver si ese número tiene el dígito 0. No importa cuántas veces lo tiene, ya que la consigna no pide contar cuántas veces aparece el dígito 0 sino cuántos de los números lo contienen. Ahora voy a tener que buscar la forma de "decirle" a la computadora cuándo un número tiene al 0 entre sus dígitos. Como esto no es una operación simple (como era la de verificar si el número es negativo), podría decir que voy a construir una función que tome el número que el usuario ingresó y devuelva "True" si el dígito 0 aparece en el número ó "False" si no aparece. Pero, como ahora estoy viendo la estructura general, me preocuparé más adelante de construir la función. Solamente tengo en cuenta que la voy a hacer, que esa función necesita el número para trabajar y va a retornar un valor booleano (True o False).
      * Si el número tenía el dígito cero, entonces deberé incrementar un contador. Sería el equivalente a contar con los dedos, pero la computadora, por ahora, ¡no tiene manos! Así que voy a necesitar algo para que la computadora vaya contando. Entonces sé que voy a tener que usar una variable numérica que sirva como contador. La tendré que inicializar en cero para que empiece a contar desde el principio y no desde cualquier lado.
  * Al usar una estructura "while" tengo que tener en cuenta de que la iteración debe interrumpirse en algún momento (para que el programa no siga ejecutándose por siempre sin darnos un resultado). El enunciado dice que, si un número no cumple la condición de corte (o sea, si el número ingresado por el usuario es negativo) no debemos procesarlo, y tenemos dos maneras de hacer esto:

<pre><code>while condición</code></pre>

ó

<pre><code>while True</code></pre>

  *   * Si queremos usar la primera forma (**while condición**), deberemos pedir al usuario que ingrese el número antes del bucle while y poner al lado de la palabra "while" la condición para que se evalúe. Luego debemos recordar que, como el ingreso del número se hizo por fuera del bucle, deberemos repetir esta instrucción dentro del while (como última instrucción del bucle) para que el número que ingresa el usuario pueda ir cambiando. Esto es:

<pre><code>número=int(input("Ingrese un número: "))
while número >= 0:
    #instrucciones del bucle
    número=int(input("Ingrese un número: "))</code></pre>

  * Si queremos usar la segunda forma (**while True**), sólo será necesario hacer una única vez la instrucción que le pide al usuario ingresar el número, y lo haremos como primer paso dentro del bucle. Pero después debemos recordar evaluar la condición (si el número es o no negativo) y, si la condición de corte se cumple, usamos **break** para interrumpir el bucle. Como nos piden no procesar el último dato (el que corta el bucle, es decir, el número negativo), necesitamos interrumpirlo antes de que ese número se procese. Entonces, la evaluación de la condición debe hacerse antes de procesar:

<pre><code>while True:
    número=int(input("Ingrese un número: "))
    if número &gt;= 0:
        #instrucciones del bucle
    else:
        break</code></pre>

  * Cuando termine la repetición, sé que la variable que usé como contador va a tener como resultado final la cantidad total de números que contenían al cero entre sus dígitos. Entonces sé que ese es el dato que necesito mostrarle al usuario. Puedo hacerlo mediante un "print" de esa variable.


Esta estructura general podría plantearse en pseudocódigo de esta forma:

<pre><code>contador=0
ESCRIBIR("Ingresar número positivo para procesar. Número negativo finaliza el programa")
LEER número
MIENTRAS (número MAYOR O IGUAL A 0) REPETIR:
    SI (número TIENE EL DÍGITO 0) ENTONCES:
        contador=contador+1
    FIN DE LA REPETICIÓN
ESCRIBIR("Cantidad de números que tenían el dígito 0: ", contador)</code></pre>

  * Hasta ahí la estructura general. Pero me falta decirle a la computadora cómo puede saber si un número contiene el dígito 0. Si el lenguaje tiene una funcionalidad que hace eso, entonces la uso (por esto es importante investigar y ver documentación). Pero, si no la tiene, tengo que construirla a partir de operaciones más sencillas. Entonces empiezo a analizar, parte por parte, qué voy a necesitar para reducir esto que necesito hacer a algo que la computadora sí pueda entender: 
      * Necesitaré tomar un número que tendrá una cantidad de dígitos desconocida y evaluar uno a uno esos dígitos, comparándolos con el cero. Si el dígito es el cero, entonces detengo el procesamiento de la función y retorno "True" ya que puedo afirmar que el número contiene al cero; si el dígito no es el cero, sigo procesando. Entonces puedo utilizar una variable booleana que empieza con su valor en "False" y se pone en "True" si encuentra al cero. Pero la computadora no sabe, por sí sola, separar los dígitos de un número. Entonces necesito aplicar una estrategia usando algo que la computadora sí sepa hacer. Por ejemplo: 
          * Tomar uno de los dígitos del número y compararlo con el cero. Si el dígito es cero, terminar la función devolviendo "True". Si no es el cero, continuar procesando el número.
          * "Cortar" el número para eliminar el dígito que ya fue evaluado y quedarme con los demás dígitos.
          * Repetir estos dos pasos hasta que haya cortado el número hasta el final (es decir, hasta haber evaluado todos sus dígitos).

  * Habíamos dicho que la computadora no sabe "cortar" los dígitos de un número. Entonces busco una forma de hacer esto con operaciones más básicas. Con unos pequeños "trucos" matemáticos puedo conseguir esta funcionalidad: si divido a un número por 10 y obtengo el resto de la división, estoy en realidad obteniendo el último dígito del número. Por ejemplo: 14678 / 10 = 1467,8. El resto (módulo) de esa división es el dígito 8. Si luego "elimino" el dígito 8 del número, me quedo con 1467. Para "eliminar" el dígito final puedo quedarme solamente con la parte entera del resultado (es decir, lo que está antes de la coma). Luego, si a 1467 lo divido por 10, el resto de esa división será el número 7. Eliminando ese último dígito y quedándome con la parte entera, obtengo ahora el 146. Nuevamente lo divido por 10 y veo que estoy cayendo en una repetición, que terminará cuando ya se haya terminado el número (cuando éste sea cero).

Así, puedo expresar la función en pseudocódigo de la siguiente manera:

<pre>INICIA FUNCIÓN
contieneAlCero(número):
    resultado=False
    MIENTRAS (número DISTINTO DE 0) Y (resultado IGUAL A False):
        dígito=número MÓDULO 10
        SI dígito IGUAL A 0:
            resultado=True
        número=número DIVISIÓN ENTERA 10
    DEVOLVER resultado
FIN FUNCIÓN</code></pre>

Ahora que ya tengo la función construida, puedo "conectarla" al programa principal reemplazando la línea

<pre><code>SI (NÚMERO TIENE EL DÍGITO 0) ENTONCES:</code></pre>

por la línea

<pre><code>SI (ContieneAlCero(número) ES IGUAL A true) ENTONCES:</code></pre>
