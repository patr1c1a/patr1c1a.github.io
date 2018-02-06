---
layout: post
title: Tipos de datos
date: 2015-06-18 11:00:00
categories: conceptos
published: true
---

La información representada en un programa constituye los "datos" que este programa manipula.

Algunos lenguajes de programación son **fuertemente tipados**, lo que significa que siempre debe indicársele con qué clase de datos está tratando, por ejemplo: números, letras, valores lógicos, etc. Para la computadora todo está representado en forma de unos y ceros, por lo que los tipos de datos asocian esos unos y ceros con determinada representación. Esto significa que un mismo grupo de unos y ceros, dispuestos de determinada manera, podría representar un número, una letra, una dirección de memoria o cualquier otro dato, según la interpretación que se le de. Entonces, en un lenguaje fuertemente tipado, es necesario indicar qué es lo que los unos y ceros representan y, una vez definido, el dato no puede utilizarse como de otro tipo a menos que se realice una conversión.

Es importante conocer el **tipo de un dato** para que el compilador pueda determinar cuáles son los **valores posibles** para ese dato y, además, qué **operaciones** se pueden realizar con ellos.

Diferentes lenguajes de programación pueden tener la capacidad de representar diferentes tipos de datos. Existen algunos tipos de datos que, de una manera u otra, suelen encontrarse en todo lenguaje:

  * **Entero ("integer" o "int"):** representa números enteros, positivos o negativos. Es un tipo de dato ordinal, es decir que para cada valor existe un antecesor y un sucesor (el 2 es sucesor del 1 y antecesor del 3).
  * **Real:** para números reales (con decimales), positivos o negativos. La parte entera de un número se separa de la parte decimeal por medio de un punto (por ejemplo, 247.50). Es un tipo de dato no ordinal, ya que al poder adoptar infinitos valores debido a los decimales, no se puede decir cuál es el antecesor y cuál el sucesor.
  * **Booleano ("boolean" o "bool"):** puede tomar sólo valores lógicos. Es decir, el dato contiene "true" (verdadero) o "false" (falso). Es un tipo de dato ordinal (False equivale a 0 y True equivale a 1, por lo tanto, False es antecesor de True).
  * **Carácter ("char"):** permite representar un caracter de la tabla ascii (tanto letras, como números, símbolos y caracteres no legibles). Por ejemplo: 'm'. Es un tipo de dato ordinal, ya que cada carácter tiene un valor numérico asociado en la tabla ascii.
  * **Cadena de caracteres ("string"):** representa una sucesión ordenada de caracteres. Por ejemplo: 'cadena de caracteres'. Es ordinal, ya que las palabras pueden ordenarse de la misma manera en que se las ordena en un diccionario.

En algunos lenguajes (como Java), estos tipos de datos suelen denominarse "primitivos" (en el caso de Java, el String es una excepción).

Aparte de estos datos básicos, suelen existir tipos de datos creados por el usuario, como los enumerados o los rangos, en el que el usuario indica los valores posibles que puede obtener, creando un subconjunto de un dato existente.

En la programación orientada a objetos, con la creación de clases es posible definir innumerables objetos con características y "operaciones" propias.
