---
layout: post
title: Un caso con generadores en Python
date: 2024-04-27 21:00:00 -0300
categories: python
tags: yield generadores
published: true
---

Veamos un ejemplo con yield que podría generar confusión si no estamos acostumbrados a trabajar con generadores.

[Qué es yield]({% post_url 2023-05-06-python-yield %})

![Ejemplo con yield]({{ site.url }}/assets/2024-27-04-ejemplo-generadores-python.png)


&nbsp;

{% include accesibilidad.html %}

Un caso con generadores en Python

Llamando a esta función obtendremos un generador de números pares, desde el 0:

```python
def pares():
    i = 0
    while True:
        yield i
        i += 2
```

Mediante next(), el generador nos da el siguiente número:

```python
generador = pares()
for _ in range(10):
    print(next(generador))
```

¿Tal vez podríamos ahorrarnos una variable e invocar a la función directamente como argumento de next()?

```python
for _ in range(10):
    print(next(pares()))
```

Pero, si hacemos esto, veremos que siempre obtenemos 0…

Cada vez que se llama a pares() se obtiene un nuevo generador, que comenzará por el número 0. Eso es lo que sucede si llamamos a pares() en cada iteración. Es por esto que debemos obtener el generador una única vez y luego usarlo.


</div></details>
<br />&nbsp;

<hr />
