---
layout: post
title: Usar recursividad no siempre es más elegante
date: 2025-07-11 13:00:00 -0300
categories: conceptos otros
tags: recursividad
published: true
---

A veces pensamos que usar recursividad hará que el código se vea "más elegante" o "más avanzado". Pero, ¿sabías que puede ser menos eficiente y hasta peligroso si no se usa bien? Muchas veces, la iteración es preferible.

No se trata de ver cuál es "más elegante", sino de elegir la herramienta correcta para cada problema.


![Usar recursividad no siempre es más elegante]({{ site.url }}/assets/2025-07-11-recursividad-iteracion.png)


&nbsp;

{% include accesibilidad.html %}
Usar recursividad no siempre es más elegante

La recursividad divide un problema en subproblemas más pequeños, pero con costos:

- Cada llamada consume memoria al agregar un frame al stack.
- Recursiones profundas pueden causar stack overflow (excede el límite de stack).
- Overhead en cada llamada (paso de argumentos, creación de contexto y retorno).

Esta función se llama a sí misma muchas veces. Con n=1000, necesita millones de llamadas porque repite cálculos, y eso llena la memoria (stack) hasta dar error:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
fibonacci(1000)
```

Usa iteración cuando:

- El problema se resuelve recorriendo datos secuencialmente, sin dividir en subproblemas.
- La recursión sería muy profunda (ej. factoriales grandes, secuencias largas).
- Se busca eficiencia en consumo de memoria y tiempo.

Usa recursividad cuando:

- El problema se define naturalmente de forma recursiva (árboles, grafos, backtracking, división y conquista).
- La profundidad de llamadas es controlada y no crece proporcional al tamaño de entrada.



</div></details>
<br />&nbsp;
<hr />
