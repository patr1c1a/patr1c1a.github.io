---
layout: post
title: Ejercicio con arreglos en C++
date: 2020-01-06 21:00:00
categories: ejercicios c++
tags: arreglos bucles
published: true
---

Un ejercicio utilizando arreglos y una posible resolución. ¿Se te ocurre alguna otra? Si es así, compartila en la sección de comentarios 😃.


![Ejercicio C++]({{ site.url }}/assets/2020-01-06-ejercicio-cpp-arreglos.png)

{% include accesibilidad.html %}

Dado un arreglo conteniendo solo unos y ceros, y su dimensión, ordenar los elementos en tiempo lineal.

Ejemplo:

Entrada: { 1, 0, 1, 0, 1, 0, 0, 1 }

Salida: { 0, 0, 0, 0, 1, 1, 1, 1 }

```cpp
void ordenar(int A[], int n) {
    int k = 0;
    for (int i = 0; i < n; i++) {
        if (A[i] == 0) {
            A[k++] = 0;
        }
    }
    for (int i = k; i < n; i++) {
        A[k++] = 1;
    }
}
```

</div></details>

<hr />

💻 [Para probar y ejecutar el código](http://jdoodle.com/a/3pLG){:target="_blank"}

{% include codeEditor.html id="3pLG?stdin=0&arg=0&rw=1" %}
