---
layout: post
title: Desafío Python número 9
date: 2020-02-04 21:00:00
categories: desafios python
tags: strings diccionarios
published: true
---

¡Nuevo desafío Python! Esta vez, con diccionarios.

▶️ [Video: diccionarios en Python](https://youtu.be/ymaBXPjiaPY){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />  
<br />Respuesta: {'h':2, 'o':1, 'l':1, 'A':1, 'b':2, 'B':2, 'F':1, 'u':3}  
<br />
<br />✏️ Explicación: El algoritmo solicita al usuario 5 strings y, por cada carácter de cada string, si se trata de una letra, verifica si no se encuentra en el diccionario, en cuyo caso la agrega con el valor 1 y, si se encuentra, le suma 1.
<br />
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pW5){:target="_blank"}
  </div>
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2020-02-04-desafio-python-9-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇

![desafío Python número 9]({{ site.url }}/assets/2020-02-04-desafio-python-9.png)
{% include accesibilidad.html %}
```python
contadores={}
for i in range(5):
    cadena=input("Texto: ")
    for caracter in cadena:
        if caracter.isalpha():
            if caracter not in contadores:
                contadores[caracter]=1
            else:
                contadores[caracter]+=1
```

¿Qué contendrá el diccionario contadores al finalizar la ejecución de este fragmento de código si los strings procesados son estos?:

¡holA!

bBBb

123

@$1..0F

uuuh...
</div></details>
