---
layout: post
title: Algoritmo de Euclides para hallar el mcd
date: 2019-10-04 21:00:00
categories: pseudocodigo
tags: matematica algoritmo
published: true
---

Una implementación sencilla del algoritmo de Euclides para hallar el máximo común divisor entre dos números.

Recordemos que la operación `mod` (o "módulo") retorna el resto de la división. Por ejemplo: `5 mod 2` retornará 1, ya que es el resto de dividir 5 / 2.

![Algoritmo de euclides]({{ site.url }}/assets/2019-10-04-algoritmo-euclides.png)
{% include accesibilidad.html %}

Algoritmo de Euclides: máximo común divisor.

Pseudocódigo:

```
while n ≠ 0:
  r ← m mod n
  m ← n
  n ← r
return m
```
</div></details>


<br />
<hr />
<br />
💻 [Implementación en Python](https://jdoodle.com/a/3pWe){:target="_blank"}

{% include codeEditor.html id="3pWe?stdin=0&arg=0&rw=1" %}
