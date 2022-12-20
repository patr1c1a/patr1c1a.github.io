---
layout: post
title: Ejercicio con Python, aplicando buenas prácticas
date: 2022-12-20 10:00:00 -0300
categories: ejercicios
tags: python buenas_practicas
published: true
---

Un ejercicio simple nos demuestra cómo la solución puede escribirse de diferentes maneras. En la segunda nuestro código es más legible y aprovecha las características del tipo bool.


![Mejorando nuestro código]({{ site.url }}/assets/2022-12-10-unix-vs-linux.png)



&nbsp;

{% include accesibilidad.html %}

EJERCICIO DE PROGRAMACIÓN

Leer un string y mostrar "True" si la cantidad de caracteres es un número par, o "False" si es impar.

Solución 1:

texto = input()
longitud = len(texto)
if longitud % 2 == 0:
    print("True")


Pero… ¿Podríamos simplificarlo?

Solución 2

texto = input()
print(len(texto) % 2 == 0)

</div></details>




<hr />
