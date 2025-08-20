---
layout: post
title: ¿Cómo sabe la computadora dónde está cada elemento de un array?
date: 2025-08-20 13:00:00 -0300
categories: conceptos
tags: arrays offset memoria
published: true
---

¿Por qué importa entender cómo se almacenan los arrays en memoria? Porque muchas estructuras y algoritmos dependen de este modelo, almacenando elementos en bloques contiguos de memoria y accediendo por índice (por ejemplo, hashmaps).

En algunos lenguajes, como Python o Java, las estructuras similares a arrays suelen almacenar referencias a los datos, lo que implica un comportamiento diferente aunque visualmente parezca igual.

![Cómo sabe la computadora dónde está cada elemento de un array]({{ site.url }}/assets/2025-08-20-arrays-en-memoria.png)


&nbsp;

{% include accesibilidad.html %}
¿Cómo sabe la computadora dónde está cada elemento de un array?

El espacio ocupado en memoria por un array es: cantidad de elementos * tamaño de cada elemento. Por ejemplo, si cada entero ocupa 4 bytes, un array de 10 enteros usará 40 bytes. 
Esto aplica a arrays que almacenan directamente los valores (no referencias), como en C y C++.

Las celdas de memoria RAM son de 1 byte.

Como los elementos se almacenan consecutivos, pueden buscarse fácilmente por posición (“i”), desplazándonos desde el principio (“base”) del arreglo: dirección base + (i * tamaño de cada elemento)

Ejemplo: un array de caracteres: ['H', 'O', 'L', 'A'] con índice de 0 a 3. En memoria: supongamos que empieza en la dirección 1320.

Para acceder al elemento en la posición 2 (carácter 'L') se empieza desde la dirección base, en este caso la 1320, avanzando 2 veces el tamaño de cada elemento. Si el tamaño de un carácter es de 1 byte y nos desplazamos 2 posiciones desde la 1320, tenemos: 1320 + (2*1) = 1322.

</div></details>
<br />&nbsp;
<hr />
