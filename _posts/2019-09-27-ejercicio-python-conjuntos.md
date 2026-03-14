---
layout: post
title: Ejercicio resuelto - conjuntos en Python
date: 2019-09-27 21:00:00
categories: python ejercicios
tags: conjuntos
published: true
---

Un ejercicio simple que puede resolverse usando operaciones básicas de conjuntos en Python.

▶️ [Video: desarrollo del ejercicio](https://youtu.be/Zo6TzXy7cxM){:target="_blank"}

![Ejercicio con conjuntos - Python]({{ site.url }}/assets/2019-09-27-ejercicio-python-conjuntos.png)

{% include accesibilidad.html %}
Ejercicio con conjuntos en Python

Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de alumnos de nivel secundario, finalizando al ingresar “x”.

- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
- Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

Solución:

```python
def cargarNombres(alumnos):
    nombre=input("Nombre: ")
    while nombre!="x":
        alumnos.add(nombre)
        nombre=input("Nombre: ")
    return alumnos
primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
cargarNombres(secundaria)
print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria | secundaria: # operación usada: unión
    print(nombre)
print("NOMBRES COMUNES:")
for nombre in primaria & secundaria: # operación usada: intersección
    print(nombre)
print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria - secundaria: # operación usada: diferencia
    print(nombre)
```

</div></details>
