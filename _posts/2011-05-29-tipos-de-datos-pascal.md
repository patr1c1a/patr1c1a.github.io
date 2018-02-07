---
layout: post
title: Tipos de datos en Pascal
date: 2011-05-29T19:12:00.000Z
categories: pascal
tags: paradigma_imperativo tipos datos variables
published: true
---

Pascal es un lenguaje de programación fuertemente tipado que tiene algunos tipos de datos predefinidos y otros que pueden ser definidos por el usuario.

Muchas veces será necesario utilizar tipos de datos adaptados a las necesidades del programa, definiendo los valores que una variable de ese tipo puede adoptar. Para crear un tipo de dato reutilizable, la palabra reservada necesaria es **type**, seguida del nombre que se le da al tipo de dato, el signo de igualdad (=) y la construcción del tipo de dato. Una vez definido el tipo, se podrán declarar variables que lo utilicen. Por ejemplo, si se construye un tipo de dato llamado **numeros**, se podrá realizar una declaracón como la siguiente:
<pre><code>var edad: numeros</code></pre>

Pero también puede definirse el tipo al declarar una variable (sólo que, de esta forma, el tipo queda definido únicamente para la variable y no es reutilizable -debe volver a definirse cada vez que se desee utilizar-): 
<pre><code>var variable Vector: array[1..10] of integer;</code></pre>

Además, los tipos de datos pueden ser **simples** o **estructurados**. Son estructurados aquellos datos que pueden contener más de un valor (simple o no) en una misma variable.

Sumado a todo esto, algunos tipos de datos serán **ordinales** y otros no. Son ordinales aquellos en los que, dado un valor del rango que admiten, puede obtenerse un predecesor y un sucesor (a excepción del primer y el último valor de ese rango, respectivamente). En Pascal, el predecesor de un valor ordinal se obtiene mediante la función _pred(valor)_ y el sucesor mediante _succ(valor)_.

&nbsp;

## Tipos predefinidos

### Simples

  * **Integer:** representa números enteros, positivos o negativos. En Pascal, este tipo de dato ocupa 2 bytes en memoria (16 bits), por lo que es posible representar 65.536 (2<sup>16</sup>) números diferentes. Como se abarca tanto negativos como positivos, el rango va desde -32.768 hasta 32.767 (se incluye el 0). Es un tipo de dato ordinal. 
      * **Byte:** entero positivo representado con 1 byte (valores del 0 al 255).
      * **Longint:** entero con signo representado con 4 bytes (valores del -247483648 al 2147483647).
      * **Shortint:** entero con signo representado con 1 byte (valores del -128 al 127).
      * **Word:** entero positivo representado con 2 bytes (valores del 0 al 65535).
  * **Real:** para números reales (con decimales), positivos o negativos. En Pascal cada dato de tipo real ocupa 6 bytes, por lo que puede tomar valores en el rango de 2.910<sup>-39</sup> a 1.710<sup>38</sup>. Es un tipo de dato no ordinal. 
      * **Single:** real representado con 4 bytes (valores del 1.510<sup>-45</sup> al 3.410<sup>38</sup>).
      * **Double:** real representado con 8 bytes (valores del 5.010<sup>-324</sup> al 1.710<sup>-308</sup>).
      * **Extended:** real representado con 10 bytes (valores del 1.910<sup>-4932</sup> al 1.1110<sup>4932</sup>).
      * **Comp:** real representado con 8 bytes (valores del 2<sup>-63</sup>+1 al 2<sup>-63</sup>-1).
  * **Boolean:** ocupa 1 byte en memoria y puede tomar sólo valores lógicos: true (verdadero) o false (falso). Es un tipo de dato ordinal (donde False es antecesor de True).
  * **Char:** permite representar un carácter de la tabla ASCII. Ocupa 1 byte en memoria. En Pascal, los caracteres se representan entre comillas simples. Es un tipo de dato ordinal.

### Estructurados

  * **String:** representa una cadena de caracteres (con un máximo de 256). El tamaño ocupado en memoria varía entre 1 y 255 bytes. Si no se aclara el espacio a reservar, por defecto ocupa 255 bytes. Si se indica el espacio máximo que puede adoptar la variable, ésta ocupará esa cantidad de bytes en memoria, se utilicen o no. Los strings, al igual que los caracteres, se representan entre comillas simples. El tipo string no se encontraba previsto en los compiladores originales de Pascal, pero los modernos lo contemplan.

&nbsp;

## Tipos definidos por el usuario

### Simples

  * **Subrango:** permite limitar el rango de valores que una variable puede adoptar. Sólo puede establecerse un subrango de datos ordinales.
  * **Enumerado:** permite especificar los valores que puede adoptar una variable.
  * **Pointer (puntero):** almacena una dirección de memoria que apunta a un dato de tipo determinado.

### Estructurados

  * **Conjunto:** tal como los conjuntos en matemática, permiten agrupar elementos sin un orden (es un tipo no ordinal) y sin repeticiones. En Pascal, los conjuntos son heterogéneos.
  * **Arreglo:** por _arreglo_ se entiende lo que en matemática se representa mediante vectores (arreglos unidimensionales) y matrices (arreglos multidimensionales). Es un tipo de dato homogéneo, donde todos sus elementos están ordenados mediante un índice y pueden accederse de manera directa indicando el nombre de la variable y el índice.
  * **Registro:** un registro permite agrupar datos de diferentes tipos (heterogéneo). Por ejemplo, si deseáramos agrupar datos personales de empleados de una empresa, podríamos crear registros que agrupen información como nombre, apellido, fecha de nacimiento, lugar de residencia, etc. Los registros se potencian al combinarse con arreglos.
  * **Archivo:** permite la manipulación de archivos en memoria no volátil (disco). Mediante este tipo se pueden abrir, leer y escribir archivos.

&nbsp;

> _La presente información está dada en base al compilador Turbo Pascal._

&nbsp;
