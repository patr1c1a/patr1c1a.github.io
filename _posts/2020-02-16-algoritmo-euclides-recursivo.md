---
layout: post
title: Algoritmo de euclides recursivo
date: 2020-02-16 21:00:00
categories: pseudocodigo
tags: algoritmos euclides matematica
published: true
---

El algoritmo de Euclides nos permite hallar el máximo común divisor entre dos números y su definición es, por naturaleza, recursiva. Veamos un ejemplo en pseudocódigo.

Recordemos que la operación `mod` (o "módulo") retorna el resto de la división. Por ejemplo: `5 mod 2` retornará 1, ya que es el resto de dividir 5 / 2.

▶️ [Video: recursividad](https://youtu.be/0NBPd81uhJE){:target="_blank"}

![Algoritmo de euclides en pseudocódigo]({{ site.url }}/assets/2020-02-16-algoritmo-euclides-recursivo.png)

{% include accesibilidad.html %}

Algoritmo de Euclides: máximo común divisor (recursivo)

La fórmula de máximo común divisor ("mcd") se define como:

x si y=0;

mcd(y, resto(x,y)) si y>0.

Algoritmo en pseudocódigo:

```
Función mcd(x: entero, y: entero)
  si y == 0:
    retornar x
  si no:
    retornar mcd(y, (x mod y))
fin mcd
```

Entrada: dos números enteros: x, y. Donde x>0, y>=0.

Salida: el máximo común divisor de ambos.
</div></details>
<br />
<hr />
<br />

💻 [Código ejecutable (implementación en Python)](https://jdoodle.com/a/3pWc){:target="_blank"}

{% include codeEditor.html id="3pWc?stdin=0&arg=0&rw=1" %}
