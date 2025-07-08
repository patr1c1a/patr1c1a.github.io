---
layout: post
title: Usar recursividad no siempre es más elegante
date: 2025-07-11 13:00:00 -0300
categories: otros conceptos
tags: recursividad
published: true
---

A veces pensamos que usar recursividad hará que el código se vea "más elegante" o "más avanzado". Pero, ¿sabías que puede ser menos eficiente y hasta peligroso si no se usa bien? Muchas veces, la iteración es preferible.

No se trata de ver cuál es "más elegante", sino de elegir la herramienta correcta para cada problema.


![Usar recursividad no siempre es más elegante]({{ site.url }}/assets/2025-07-11-recursividad-iteracion.png)


&nbsp;

{% include accesibilidad.html %}
Usar recursividad no siempre es "más elegante"

La recursividad divide un problema en subproblemas idénticos más pequeños, pero tiene costos importantes:
- Cada llamada recursiva agrega un nuevo marco (frame) en el stack de llamadas, consumiendo memoria.
- Si la recursividad es muy profunda, puede provocar un stack overflow (error cuando el stack supera su límite).
- Las llamadas recursivas tienen overhead (paso de argumentos, creación de contexto, retorno).

Por eso, no siempre es la mejor opción.

Usa iteración cuando:
- La solución requiere recorrer secuencialmente un conjunto de datos sin descomposición natural en subproblemas.
- La recursividad sería demasiado profunda (por ejemplo, calcular factoriales grandes o secuencias largas).
- Se busca eficiencia en consumo de memoria y tiempo.

Usa recursividad cuando:
- El problema tiene definición recursiva clara (como recorrer árboles o grafos, algoritmos de backtracking o división y conquista).
- La profundidad de la recursividad es controlada y no crece linealmente con el tamaño de entrada.


</div></details>
<br />&nbsp;
<hr />
