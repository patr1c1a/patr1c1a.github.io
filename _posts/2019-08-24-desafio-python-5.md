---
layout: post
title: Desafío Python número 5
date: 2019-08-24 21:00:00
categories: desafios python
tags: funciones bucles
published: true
---

Si necesitas repasar algunos conceptos para resolverlo, estos videos pueden serte útiles:

▶️ [Video: funciones](https://youtu.be/IF34NgjldXs){:target="_blank"}

▶️ [Video: bucles while](https://youtu.be/Ll8Q48_yPIM){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />La opción correcta es la a).
<br />
<br />✏️ Explicación: esta función determina si el número n contiene al dígito d. Para esto, se recorre el número, obteniendo cada dígito desde el final (usando el operador módulo) y comparándolos con d. Si el dígito coincide con d, la función retorna True. Si finaliza la iteración sin encontrarlo, retorna False.
<br />
<br />
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pTx){:target="_blank"}
  </div>
<br />
{% include codeEditor.html id="3pTx?stdin=0&arg=0&rw=1" %}
<br />

<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-08-24-desafio-python-5-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇
![desafío Python número 5]({{ site.url }}/assets/2019-08-24-desafio-python-5.png)

{% include accesibilidad.html %}
¿Cuál o cuáles de las siguientes llamadas a función retornan False?


a. `funcion(543210, 6)`

b. `funcion(100000000, 0)`

c. `funcion(100000000, 1)`

```python
def funcion(n, d):
    while n != 0:
        if n%10 == d:
            return True
        n //= 10
    return False
```

</div></details>



