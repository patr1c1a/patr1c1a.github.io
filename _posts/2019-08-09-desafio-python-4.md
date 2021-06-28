---
layout: post
title: Desafío Python número 4
date: 2019-08-09 21:00:00
categories: desafios python
tags: strings
published: true
---

Desafío de Python número 4 🐍

Si necesitas repasar cómo funcionan if, for y while, estos videos pueden serte útiles:

▶️ [Video: if-elif-else](https://youtu.be/kIkAhld32O8){:target="_blank"}

▶️ [Video: bucles for](https://youtu.be/TPXPoUkUNqg){:target="_blank"}

▶️ [Video: bucles while](https://youtu.be/Ll8Q48_yPIM){:target="_blank"}


<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />La opción correcta es la B.
<br />
<br />✏️ Explicación:
<br />🔹 La opción A no resuelve el problema porque no es necesaria una iteración (ya estamos dentro de la iteración for, y ahora sólo hay que ver si el carácter evaluado es una vocal). Además, no existe ninguna variable o expresión llamada vocales dentro de la función, lo cual daría un error antes de comenzar la ejecución.
<br />🔹 La opción C no da ningún error pero no hace lo esperado: c siempre va a ser un único carácter (porque se está recorriendo la cadena) y jamás podría ser igual a "aeiou".
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pW3){:target="_blank"}
  </div>
{% include codeEditor.html id="3pW3?stdin=0&arg=0&rw=1" %}
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-08-09-desafio-python-4-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇
![Desafío Python número 4]({{ site.url }}/assets/2019-08-09-desafio-python-4.png)

{% include accesibilidad.html %}
```python
def cantidadVocales(cadena):
    cadena = cadena.lower()
    cantidad = 0
    for c in cadena:
        
            cantidad += 1
    return cantidad
```

¿Qué instrucción falta en la línea 5? (inmediatamente después de `for c in cadena:`)?

a. while c in vocales:

b. if c in "aeiou":

c. if c=="aeiou":
</div></details>
