---
layout: post
title: Video - Tu código puede tener un bug invisible
date: 2025-10-14 16:00:00
categories: conceptos
tags: variables memoria overflow integer enteros
published: true
---

En programación, no todo lo que "cuenta"… "cuenta" bien. Aunque suene paradójico, uno de los errores más antiguos —y aún vigentes— tiene que ver con cómo las computadoras representan los números. Específicamente, con los límites de los tipos de datos enteros.

El "integer overflow" ocurre cuando un cálculo produce un valor que excede la capacidad máxima del tipo de dato utilizado. Muchos lenguajes no arrojan un error cuando esto sucede, por lo que puede pasar desapercibido durante pruebas, pero en producción puede causar fallos silenciosos, corrupción de datos o incluso vulnerabilidades de seguridad.

[Este ejemplo en C++](https://paiza.io/projects/27Wd58xurVr1X0sQHQP3kg){:target="_blank"} muestra un ejemplo de overflow:
```cpp
int max = 2147483647; // Máximo valor para int32 (2^31 - 1)
std::cout << "Antes del overflow: " << max << std::endl;
max = max + 1; // Provoca overflow
std::cout << "Después del overflow: " << max << std::endl;
```

Este tipo de problema no es solo teórico: en 2015 se descubrió que los sistemas de los aviones Boeing 787 podían fallar tras estar encendidos más de 248 días seguidos debido a un contador de tiempo de 32 bits que se desbordaba. Y en 2014, YouTube tuvo que migrar su contador de vistas de un entero con signo de 32 bits a uno de 64 bits cuando Gangnam Style superó los 2.100 millones de reproducciones (el límite práctico de ese tipo de dato).

Lo interesante del overflow es que muchas veces ocurre en contextos donde "nunca pasaría": contadores de usuarios, cálculos financieros, tiempos de ejecución… Hasta que pasa.

▶️ En este video breve, te cuento más detalles sobre el tema.

Después de verlo, tal vez podríamos pensar en qué sucedería si sumamos dos números grandes y el resultado se desborda, pero luego restamos uno de ellos. ¿Volvería al valor original, o el daño ya está hecho?

{% include youtubePlayer.html id="xwxz9fNyvJo" %}

