---
layout: post
title: Pregunta de entrevista laboral (Python)
date: 2023-05-20 22:00:00 -0300
categories: python ejercicios
tags: entrevistas listas
published: true
---

Veamos algo que suele preguntarse en algunas entrevistas, para determinar qué tanto conocemos a Python. Y es que este es un error común cuando somos principiantes, especialmente porque nuestro programa no mostrará ninguna advertencia, pero probablemente el resultado no sea el que esperamos.


![Pregunta de entrevista laboral]({{ site.url }}/assets/2023-05-21-python-parametro-por-defecto-mutable.png)


&nbsp;

{% include accesibilidad.html %}
Pregunta de entrevista laboral (Python)

¿Cuál es la salida de este programa?

```python
def prueba(lista=[]):
	lista.append(5)
	return lista
	
print(prueba())
print(prueba())
```
Respuesta:
```
[5]
[5, 5]
```
El parámetro lista tiene un valor por defecto (una lista vacía) que se usa si no se pasa un argumento en la llamada.

¿Por qué no retorna lo mismo en ambas llamadas? Respuesta: en Python los parámetros se evalúan una única vez, cuando la función se define. Luego se usa ese valor en cada llamada.

Para solucionarlo:

```python
def prueba (lista=None):
	if lista == None:
		lista = []
	lista.append(5)
	return lista
```

Salida:
```
[5]
[5]
```


</div></details>



<hr />
