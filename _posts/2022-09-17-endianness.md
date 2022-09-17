---
layout: post
title: Arquitecturas "little-endian" y "big-endian"
date: 2022-09-17 21:00:00 -0300
categories: conceptos
tags: big-endian little-endian
published: true
---

No todas las computadoras tienen la misma arquitectura (aunque algunas son más populares y otras se han dejado de usar). Una de las diferencias está en el orden de los bytes cuando se almacena un dato, y a esto se lo llama, en inglés, "endianness". En el caso de datos que solo usen 1 byte no habrá diferencia pero, cuando se usan 2 o más, debe distinguirse en qué orden se almacenarán.

Los nombres "big endian" y "little endian" se basan en el libro "Los viajes de Gulliver", en el cual dos facciones de liliputienses se distinguen porque unos rompen los huevos cocidos por el extremo más pequeño mientras que los otros lo hacen por el extremo más grande.


![Arquitecturas little endian y big endian]({{ site.url }}/assets/2022-09-17-endianness.png)


{% include accesibilidad.html %}
Arquitecturas "little-endian" y "big-endian"

Cuando un dato ocupa varias posiciones de memoria, es necesario saber en qué orden se almacenan sus bytes.

El número decimal 8607518, como hexadecimal:

- Big-endian: 1E 57 83 00

- Little-endian: 00 83 57 1E

"Big-endian": desde el "extremo mayor" ("big end")  hacia el menor. El byte más significativo se ubica en la dirección de memoria más pequeña.

"Little-endian": desde el "extremo menor" ("little end")  hacia el mayor. El byte más significativo se ubica en la dirección de memoria más grande.

</div></details>





<hr />
