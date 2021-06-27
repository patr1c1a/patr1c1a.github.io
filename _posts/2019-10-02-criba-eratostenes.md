---
layout: post
title: La criba de Eratóstenes
date: 2019-10-02 21:00:00
categories: otros
tags: c matematica algoritmo
published: true
---

👉 Un algoritmo para encontrar los números primos entre el 2 y un número dado: "la criba de Eratóstenes". 

💻 [Programa ejecutable](https://jdoodle.com/a/3pNd){:target="_blank"}

📌 Referencias:

- [Wikipedia](https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes){:target="_blank"}
- ["Algorithms in C" (Sedgewick)](https://books.google.com.ar/books/about/Algorithms_in_C.html?id=Bf7XAAAAMAAJ){:target="_blank"}

![Criba de Eratóstenes]({{ site.url }}/assets/2019-10-02-criba-eratostenes.png)

{% include accesibilidad.html %}

La criba de Eratóstenes es un algoritmo que permite hallar todos los números primos menores que un número natural dado N. Se forma una tabla con todos los números naturales comprendidos entre 2 y N, y se van tachando los números que no son primos.

PROGRAMA EN C:

El objetivo de este programa es colocar a[i] en 1 si i es primo, ó en 0 si no lo es. Primero, coloca todos los elementos del arreglo en 1, indicando que se desconoce qué números no son primos. Luego coloca en 0 los elementos del arreglo correspondientes a índices múltiplos de números que son primos (se sabe que ellos no son primos). Si a[i] es 1 luego de que todos los múltiplos de primos menores han sido puestos en 0, entonces sabemos que i es primo.

```c
#define N 10000
int main() 
{
    int i, j, a[N];
    for (i = 2; i < N; i++)
        a[i] = 1;
    for (i = 2; i < N; i++) 
        if (a[i])
            for (j = i; i*j < N; j++)
                a[i*j] = 0;
    for (i = 2; i < N; i++)
        if (a[i])
            printf("%8d", i);
} 
```

</div></details>

<hr />

{% include codeEditor.html id="3pNd?stdin=0&arg=0&rw=1" %}
<br />
