---
layout: post
title: Desafío C++ número 4
date: 2019-09-30 21:00:00
categories: desafios c++
tags: punteros
published: true
---

Desafío C++ número 4.

👉 Desafío de programación: punteros.

▶️ [Video: Punteros](https://www.youtube.com/watch?v=s8T7cPnYrz0){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />
<br />✏️ Explicación: el arreglo de la línea 6 tiene elementos de tipo char y se inicializa con 3 elementos: 'M', 'a', 'r', ubicados en las posiciones 0, 1 y 2. El arreglo de la línea 7 tiene elementos de tipo puntero a char (es decir: direcciones de memoria donde haya variables de tipo char). En la línea 8 se guarda en la primera posición de arregloPunterosChar la dirección de memoria del elemento que se encuentra en la posición 2 de arreglosChar (esa posición del arreglo contiene el carácter 'r'). En la línea 9 se imprime el puntero desreferenciado, es decir, se busca lo que hay en la dirección de memoria que indica, y en esa dirección de memoria se encuentra el carácter 'r'.
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-09-30-desafio-cpp-4-solucion.png)
  </div></details>
<br />
<br />
**Desafío C++** 👇

![Desafío]({{ site.url }}/assets/2019-09-30-desafio-cpp-4.png)
