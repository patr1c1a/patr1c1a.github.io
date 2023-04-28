---
layout: post
title: Qué es yield en Python
date: 2023-05-06 21:00:00 -0300
categories: python conceptos
tags: yield
published: true
---

Esta es una de esas herramientas que aprendemos cuando queremos dar un pasito más allá y mejorar nuestro código Python. ¿Conocías "yield"? ¿Lo has usado?


![¿Qué es yield en Python?]({{ site.url }}/assets/2023-05-06-python-yield.png)


&nbsp;

{% include accesibilidad.html %}
Python: ¿qué es "yield"?

yield: palabra clave para crear un generador.

generador: función que retorna un iterador.

iterador: objeto que puede iterarse, llamando a next() para que retorne el siguiente elemento de la secuencia.

yield funciona suspendiendo la ejecución de la función para retornar un valor. La siguiente vez que se llama a la misma función, la ejecución continúa desde donde se había dejado.

EJEMPLOS:

Sin yield:

```python
def fibonacci(cantidad):
    a, b = 0, 1
    for i in range(cantidad):
        print(a)
        a, b = b, a + b

fibonacci(10)
```

Con yield:

```python
def fibonacci(cantidad):
    a, b = 0, 1
    for i in range(cantidad):
        yield a
        a, b = b, a + b

for i in fibonacci(10):
    print(i)
```

yield es útil para evitar cargar en memoria grandes cantidades de datos que se deban iterar.

```python
def leer_archivo(nombre):
    with open(nombre, 'r') as a:
        for line in a:
            yield line

for linea in leer_archivo('datos.txt'):
    print(linea)
```


</div></details>



<hr />
