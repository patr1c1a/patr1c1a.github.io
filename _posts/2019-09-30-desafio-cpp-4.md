---
layout: post
title: Desafío C++ número 4
date: 2019-09-30 21:00:00
categories: desafios c++
tags: punteros
published: true
---

👉 Para saber qué imprime este programa deberemos analizar de qué tipo son las variables declaradas y los punteros que se crean, y descubrir de qué forma se utilizan y acceden esos datos.


▶️ [Video: Punteros](https://www.youtube.com/watch?v=s8T7cPnYrz0){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />
<br />La respuesta es: r.
<br />
<br />✏️ Explicación: el arreglo de la línea 6 tiene elementos de tipo char y se inicializa con 3 elementos: 'M', 'a', 'r', ubicados en las posiciones 0, 1 y 2. El arreglo de la línea 7 tiene elementos de tipo puntero a char (es decir: direcciones de memoria donde haya variables de tipo char). En la línea 8 se guarda en la primera posición de arregloPunterosChar la dirección de memoria del elemento que se encuentra en la posición 2 de arreglosChar (esa posición del arreglo contiene el carácter 'r'). En la línea 9 se imprime el puntero desreferenciado, es decir, se busca lo que hay en la dirección de memoria que indica, y en esa dirección de memoria se encuentra el carácter 'r'.
<br />&nbsp;
  
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pBg){:target="_blank"}
  </div>
  {% include codeEditor.html id="3pwV?stdin=0&arg=0&rw=1" %}
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-09-30-desafio-cpp-4-solucion.png)
  </div></details>
<br />
<br />
**Desafío C++** 👇

![Desafío C++ 4]({{ site.url }}/assets/2019-09-30-desafio-cpp-4.png)
