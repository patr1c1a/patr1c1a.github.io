---
layout: post
title: Tipos de datos - en detalle
date: 2025-06-26 09:00:00 -0300
categories: conceptos
tags: datos int boolean float char
published: true
---

Entender cómo se almacenan los datos nos ayuda a escribir código más eficiente (ahorrando memoria y CPU), debuggear errores raros (como overflows o accesos inválidos), trabajar con archivos binarios, redes o hardware (donde cada byte cuenta).

¿Cuándo vas a necesitar saber esto? Cuando trabajes con:

✓ Sistemas embebidos (memoria limitada),

✓ Procesamiento de archivos binarios (imágenes, sonido),

✓ Optimización crítica (juegos, algoritmos pesados),

✓ Bugs raros (como buffer overflows o corrupción de datos).


![Tipos de datos]({{ site.url }}/assets/2025-06-26-tipos-de-datos.png)


&nbsp;

{% include accesibilidad.html %}

Tipos de datos: en detalle

Un dato es una secuencia de bits (unos y ceros). Su tipo indica cómo interpretarlos. A nivel de hardware, todo son bits. 

El mismo patrón de bits (01000001) podría ser el número 65 (entero) o el carácter 'A' (ASCII). El tipo lo define.

El tipo de un dato nos dice:
- Qué valores puede tomar una variable (ejemplo: números, texto, verdadero/falso). 
- Qué operaciones se pueden hacer con él (ejemplo: sumar int, concatenar string).
- Cuánta memoria ocupa (ejemplo: un float usa más bytes que un boolean).

Cada tipo de dato ocupa una cierta cantidad de bytes en memoria:
- int: suelen ser 4 bytes (sistemas modernos), pero pueden ser 2 (ej: Arduino).
- float: 4 bytes (precisión simple) u 8 bytes (doble precisión, como el double en C).
- char: 1 byte (8 bits) en casi todos los sistemas modernos.
- bool: 1 byte (aunque alcanza con 1 bit, se usa 1 byte completo).
- punteros: 4 bytes (32-bit) u 8 bytes (64-bit), solo para almacenar una dirección.

Los arreglos se almacenan como bloques contiguos en memoria, donde cada elemento ocupa un tamaño fijo según su tipo. Ejemplo: un arreglo de 5 int (4 bytes c/u) ocupa 20 bytes contiguos. 


</div></details>
<br />&nbsp;
<hr />
