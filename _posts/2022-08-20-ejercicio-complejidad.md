---
layout: post
title: Ejercicio de complejidad algorítmica (resuelto)
date: 2022-08-20 12:00:00
categories: ejercicios
tags: python complejidad
published: true
---


Sabemos que, para un mismo problema, pueden existir varias soluciones. ¡Pero hay soluciones más eficientes que otras! Acá vemos un ejemplo (escrito en lenguaje Python, pero el ejemplo es válido para otros lenguajes). Más abajo puede verse el código ejecutable en Python y también en C++, con medición del tiempo de ejecución de ambas versiones del algoritmo.



[Click acá para ver info sobre complejidad algorítmica](https://rebrand.ly/complejidad_algoritmica)


![Ejercicio de complejidad algorítmica, resuelto]({{ site.url }}/assets/2022-08-20-ejercicio-complejidad.png)


{% include accesibilidad.html %}
Ejercicio: complejidad algorítmica

Dada una lista de números, este algoritmo retorna dos elementos que, sumados, den un cierto resultado (o bien 0, 0 en caso de no hallarlos):

```python
def sumandos(numeros, suma):
  for a in numeros:
    diferencia = suma - a
    for b in numeros:
      if (b != a) and (b == diferencia):
        return (a, b)
  return (0, 0)
```

Su complejidad es O(n<sup>2</sup>) porque tiene bucles anidados. ¿Puede mejorarse la complejidad a O(n)?

Resolución:

```python
def sumandos(numeros, suma):
  conjunto = set()
  for a in numeros:
    diferencia = suma - a
    if diferencia in conjunto:
      return (a, diferencia)
    else:
      conjunto.add(a)
  return (0, 0)
```

Su complejidad es O(n). El bucle que itera por los n elementos de la lista nos da una complejidad de O(n). El operador "in" de Python tiene complejidad O(1), por lo que no influye en este resultado.

</div></details>



<hr />
