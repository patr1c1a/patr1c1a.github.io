---
layout: post
title: Desafío Python número 7
date: 2019-11-06 21:00:00
categories: desafios python
tags: strings
published: true
---


Si necesitas repasar algunos conceptos para resolverlo, estos videos pueden serte útiles:

▶️ [Video: manejo de strings en Python](https://youtu.be/xAigyL6Lz2s){:target="_blank"}

▶️ [Video: bucles for](https://www.youtube.com/watch?v=TPXPoUkUNqg){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />La respuesta correcta es la d.
<br />
<br />✏️ Explicación: la función convierte la letra inicial de cada palabra a mayúscula, tomando como separador de palabras a los caracteres no alfabéticos. No convierte a minúsculas las demás letras, por lo que no es equivalente al método title() de Python.
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3q97){:target="_blank"}
  </div>
  
{% include codeEditor.html id="3q97?stdin=0&arg=0&rw=1" %}
  
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-11-06-desafio-python-7-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇

![desafío Python número 7]({{ site.url }}/assets/2019-11-06-desafio-python-7.png)

{% include accesibilidad.html %}

```python
def convertir(cadena):
    nueva = ""
    siguiente = True
    for caracter in cadena:
        if siguiente:
            caracter = caracter.upper()
        nueva += caracter
        siguiente = not caracter.isalpha()
    return nueva
```

¿Qué retorna la función ante la siguiente invocación?

`convertir("**el desafío Python número: ¡7!**")`

Opciones:

a. `"**El desafío python número: ¡7!**"`

b. `"**EL DESAFÍO PYTHON NÚMERO: ¡7!**"`

c. `"El Desafío Python Número 7"`

d. `"**El Desafío Python Número: ¡7!**"`

</div></details>

