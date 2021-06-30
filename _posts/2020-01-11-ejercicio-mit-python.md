---
layout: post
title: Ejercicio de examen de MIT, resuelto - Listas en Python
date: 2020-01-11 21:00:00
categories: ejercicios python
tags: mit listas arreglos
published: true
---

En este ejercicio de examen del MIT se pide realizar operaciones sobre una lista para obtener la mediana de una serie de números, utilizando Python. La resolución dada por la universidad utiliza una excepción para el caso de que la lista esté vacía.

▶️ [Video: listas y tuplas en Python](https://www.youtube.com/watch?v=TEHBEGj1MSU){:target="_blank"}

![Ejercicio de MIT resuelto]({{ site.url }}/assets/2020-01-11-ejercicio-mit-python.png)

{% include accesibilidad.html %}

Ejercicio de examen resuelto (programación en Python).

Este ejercicio de examen es de M.I.T. de Estados Unidos ("6.00 Introduction to computer science and programming").

Consigna:

Dada la función hallarMediana(L), escribir el código que implemente una función de acuerdo a la especificación dada a continuación:

Halla la mediana de L.

L: una lista no vacía de floats.

Retorno: Si L tiene una cantidad impar de elementos, retorna el valor mediano de L. Ejemplo: si L es la lista [15.0, 5.3, 18.2], retorna 15.0.

Si L tiene una cantidad par de elementos, retorna el promedio de los dos elementos medianos.

Ejemplo: si L es la lista [1.0, 2.0, 3.0, 4.0], retorna 2.5.

Si la lista está vacía, arroja una excepción ValueError.

Efectos colaterales: ninguno


Resolución:

```python
def hallarMediana(L):
    if len(L) == 0:
        raise ValueError("Lista vacía")
    copy = L[:]
    copy.sort()
    if len(copy)%2 == 1:
        return copy[len(copy)//2]
    else:
        return (copy[len(copy)//2] + copy[len(copy)//2 -1]) / 2
```

</div></details>
<hr />
<br />
[Código ejecutable](https://jdoodle.com/a/3pWv){:target="_blank"}

{% include codeEditor.html id="3pWv?stdin=0&arg=0&rw=1" %}
