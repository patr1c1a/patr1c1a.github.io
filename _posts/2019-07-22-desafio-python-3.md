---
layout: post
title: Desafío Python número 3
date: 2019-07-22 21:00:00
categories: desafios python
tags: diccionarios listas arreglos
published: true
---

¿Vamos con un nuevo desafío en Python? 😎

🎥 Para aprender sobre diccionarios y listas, no dejes de ver estos videos:

▶️ [Video: Listas y tuplas](https:://www.youtube.com/watch?v=TEHBEGj1MSU){:target="_blank"}

▶️ [Video: Diccionarios](https://www.youtube.com/watch?v=ymaBXPjiaPY){:target="_blank"}


<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✏️ Explicación: este algoritmo guarda datos en un diccionario donde las claves son nombres de plantas (tipo string) y los valores son listas que contienen propiedades de cada planta (elementos de las listas: de tipo string). Para evitar sobreescribir una lista si se ingresa una planta ya existente en el diccionario, se verifica previamente que la clave no exista en él, con el operador in.
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pVL){:target="_blank"}
  </div>
{% include codeEditor.html id="3pVL?stdin=0&arg=0&rw=1" %}  
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-07-22-desafio-python-3-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇
![Desafío Python número 3]({{ site.url }}/assets/2019-07-22-desafio-python-3.png)
{% include accesibilidad.html %}

```python
recetasNaturistas = {}
planta = input("Nombre de una planta: ")
while planta != "x":
    if planta not in recetasNaturistas:
        recetasNaturistas[planta] = []
    propiedad = input("Ingrese una propiedad de la planta: ")
    while propiedad != "x":
        recetasNaturistas[planta].append(propiedad)
        propiedad = input("Ingrese una propiedad de la planta: ")
    planta = input("Nombre de una planta: ")

print(recetasNaturistas)
```

¿Qué imprime este programa si, al ejecutarlo, se ingresa lo siguiente, en el orden indicado?

menta

concentración

memoria

antiinflamatorio

x

lima

circulación

x

lavanda

cicatrizante

antiestrés

x

x
</div></details>
