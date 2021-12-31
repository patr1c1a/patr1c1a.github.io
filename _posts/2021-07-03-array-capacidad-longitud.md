---
layout: post
title: La capacidad y longitud de un arreglo, o su dimensión física y lógica
date: 2021-07-04 12:00:00
categories: conceptos
tags: arreglo array
published: true
---


Los arrays son estructuras básicas, a partir de las cuales en varios lenguajes se implementan otras con diversas operaciones. Normalmente, en un array podemos distinguir su capacidad física de la cantidad de elementos que almacena, y también la cantidad de espacio ocupado en la memoria de la computadora.

Podemos ampliar este tema leyendo el capítulo "7.4.1 Capacidad vs. longitud de un array" del libro "Algoritmos a fondo con implementaciones en C y Java" (primera edición), del Ing. Pablo Sznajdleder.

![Capacidad y Longitud de un array]({{ site.url }}/assets/2021-07-03-array-capacidad-longitud.png)


{% include accesibilidad.html %}
"Capacidad" y "longitud" de un array (o "dimensión física" y "lógica")

Capacidad: tope físico a la cantidad de elementos que puede contener un array. Es fija.

Longitud: cuántos elementos almacena el array. Cambia a medida que se almacenan o eliminan elementos.

Si se define un array con 100 elementos de 2 bytes cada uno, el array ocupará 200 bytes en memoria, aunque aún no hayamos almacenado nada en él.

Ejemplo: Si tenemos un array de tipo string[100], su capacidad es 100. Su longitud inicial es 0. Si se agregan 5 elementos, la capacidad será 100 y la longitud será 5. Si luego se elimina un elemento, la capacidad será 100 y, la longitud, 4. Usualmente, los elementos se almacenan consecutivamente desde el 0.

La longitud como concepto lógico no tiene sentido para la máquina. Ella solo sabe que el array tiene 100 elementos. Es el programador quien determina cuántos de ellos son "válidos".
</div></details>
<hr />
