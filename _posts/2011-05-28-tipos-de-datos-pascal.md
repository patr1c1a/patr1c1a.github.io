---
layout: post
title: Tipos de datos en Pascal
date: 2011-05-28 19:12:00
categories: pascal
published: false
---

Pascal es un lenguaje de programación _fuertemente tipado_ que tiene algunos tipos de datos predefinidos y otros que pueden ser definidos por el usuario.

Muchas veces será necesario utilizar tipos de datos adaptados a las necesidades del programa, definiendo los valores que una variable de ese tipo puede adoptar. Para crear un tipo de dato reutilizable, la palabra reservada necesaria es â€œ**type**â€, seguida del nombre que se le da al tipo de dato, el signo de igual (â€œ=â€) y la construcciÃ³n del tipo de dato. Una vez definido el tipo, se podrÃ¡n declarar variables que lo utilicen. Por ejemplo, si se construye un tipo de dato llamado â€œnumerosâ€, se podrÃ¡ realizar una declaracón como la siguiente: <code class="EnlighterJSRAW" data-enlighter-language="generic">var edad: numeros</code>

Pero tambiÃ©n puede definirse el tipo al declarar una variable (sÃ³lo que, de esta forma, el tipo queda definido Ãºnicamente para la variable y no es reutilizable -debe volver a definirse cada vez que se desee utilizar-):Â <code class="EnlighterJSRAW" data-enlighter-language="generic">var variableVector: array[1..10] of integer;</code>

AdemÃ¡s, los tipos de datos pueden ser simples o estructurados. Son estructurados aquellos datos que pueden contener mÃ¡s de un valor (simple o no) en una misma variable.

Sumado a todo esto, algunos tipos de datos serÃ¡n **ordinales** y otros no. Son ordinales aquellos en los que, dado un valor del rango que admiten, puede obtenerse un predecesor y un sucesor (a excepciÃ³n del primer y el Ãºltimo valor de ese rango, respectivamente). En Pascal, el predecesor de un valor ordinal se obtiene mediante la funciÃ³n _pred(valor)_ y el sucesor mediante _succ(valor)_.

&nbsp;

### Tipos predefinidos

#### Simples

  * **Integer:** representa nÃºmeros enteros, positivos o negativos. En Pascal, este tipo de dato ocupa 2 bytes en memoria (16 bits), por lo que es posible representar 65.536 (2<sup>16</sup>) nÃºmeros diferentes. Como se abarca tanto negativos como positivos, el rango va desde -32.768 hasta 32.767 (se incluye el 0). Es un tipo de dato ordinal. 
      * **Byte:** entero positivo representado con 1 byte (valores del 0 al 255).
      * **Longint:** entero con signo representado con 4 bytes (valores del -247483648 al 2147483647).
      * **Shortint:** entero con signo representado con 1 byte (valores del -128 al 127).
      * **Word:** entero positivo representado con 2 bytes (valores del 0 al 65535).
  * **Real:** para nÃºmeros reales (con decimales), positivos o negativos. En Pascal cada dato de tipo real ocupa 6 bytes, por lo que puede tomar valores en el rango de 2.910<sup>-39</sup> a 1.710<sup>38</sup>. Es un tipo de dato no ordinal. 
      * **Single:** real representado con 4 bytes (valores del 1.510<sup>-45</sup> al 3.410<sup>38</sup>).
      * **Double:** real representado con 8 bytes (valores del 5.010<sup>-324</sup> al 1.710<sup>-308</sup>).
      * **Extended:** real representado con 10 bytes (valores del 1.910<sup>-4932</sup> al 1.1110<sup>4932</sup>).
      * **Comp:** real representado con 8 bytes (valores del 2<sup>-63</sup>+1 al 2<sup>-63</sup>-1).
  * **Boolean:** ocupa 1 byte en memoria y puede tomar sÃ³lo valores lÃ³gicos: â€œtrueâ€ (verdadero) o â€œfalseâ€ (falso). Es un tipo de dato ordinal (donde False es antecesor de True).
  * **Char:** permite representar un carÃ¡cter de la tabla ASCII. Ocupa 1 byte en memoria. En Pascal, lLos caracteres se representan entre comillas simples. Es un tipo de dato ordinal.

#### Estructurados

  * **String:** representa una cadena de caracteres (con un mÃ¡ximo de 256). El tamaÃ±o ocupado en memoria varÃ­a entre 1 y 255 bytes. Si no se aclara el espacio a reservar, por defecto ocupa 255 bytes. Si se indica el espacio mÃ¡ximo que puede adoptar la variable, Ã©sta ocuparÃ¡ esa cantidad de bytes en memoria, se utilicen o no. Los strings, al igual que los caracteres, se representan entre comillas simples. El tipo string no se encontraba previsto en los compiladores originarios de Pascal, pero los modernos lo contemplan.

&nbsp;

### Tipos definidos por el usuario

#### Simples

  * **<a href="http://www.patriciaemiguel.com/pascal-tipos-subrango-y-enumerado/" target="_blank">Subrango</a>:** permite limitar el rango de valores que una variable puede adoptar. SÃ³lo puede establecerse un subrango de datos ordinales.
  * <a href="http://www.patriciaemiguel.com/pascal-tipos-subrango-y-enumerado/" target="_blank"><strong>Enumerado:</strong></a> permite especificar los valores que puede adoptar una variable.
  * **Pointer (puntero):** almacena una direcciÃ³n de memoria que apunta a un dato de tipo determinado.

#### Â Estructurados

  * **<a href="http://www.patriciaemiguel.com/conjuntos-en-pascal/" target="_blank">Conjunto</a>:** tal como los conjuntos en matemÃ¡tica, permiten agrupar elementos sin un orden (es un tipo no ordinal) y sin repeticiones. En Pascal, los conjuntos son heterogÃ©neos.
  * **<a href="http://www.patriciaemiguel.com/arreglos-en-pascal/" target="_blank">Arreglo</a>:** por &#8220;arreglo&#8221; se entiende lo que en matemÃ¡tica se representa mediante vectores (arreglos unidimensionales) y matrices (arreglos multidimensionales). Es un tipo de dato homogÃ©neo, donde todos sus elementos estÃ¡n ordenados mediante un Ã­ndice y pueden accederse de manera directa indicando el nombre de la variable y el Ã­ndice.
  * **<a href="http://www.patriciaemiguel.com/registros-en-pascal/" target="_blank">Registro</a>:** un registro permite agrupar datos de diferentes tipos (heterogÃ©neo). Por ejemplo, si deseÃ¡ramos agrupar datos personales de empleados de una empresa, podrÃ­amos crear registros que agrupen informaciÃ³n como nombre, apellido, fecha de nacimiento, lugar de residencia, etc. Los registros se potencian al combinarse con arreglos.
  * **Archivo:** permite la manipulaciÃ³n de archivos en memoria no volÃ¡til (disco). Mediante este tipo se pueden abrir, leer y escribir archivos.

&nbsp;

&nbsp;

> _La presente informaciÃ³n es en base al compilador Turbo Pascal._

&nbsp;
