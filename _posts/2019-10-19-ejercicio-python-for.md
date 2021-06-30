---
layout: post
title: Ejercicio con bucles for en Python
date: 2019-10-19 21:00:00
categories: ejercicios python
tags: bucles
published: true
---

Veamos un ejercicio simple en Python, usando bucles for.

▶️ [Video: bucles for](https://youtu.be/TPXPoUkUNqg){:target="_blank"}

▶️ [Video: explicación del ejercicio](https://youtu.be/7fBMgfbD570){:target="_blank"}

![Ejercicio Python]({{ site.url }}/assets/2019-10-19-ejercicio-python-for.png)

{% include accesibilidad.html %}

Encriptar un mensaje usando el método de "la cifra del César", que consiste en correr cada letra -considerando la posición que ocupa en el alfabeto- una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra "hola" se transforma en "jqnc".

Si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la latra 'a'.

```python
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("Corrimiento: "))
mensaje = input("Mensaje a encriptar: ")
encriptado = ""
for caracter in mensaje:
    if caracter.lower() in alfabeto:
        indice = alfabeto.find(caracter.lower())
        indice = (indice+corrimiento) % 27
        encriptado += alfabeto[indice]
    else:
        encriptado += caracter
print("Mensaje encriptado: ", encriptado)
```

Se efectúa una operación módulo para obtener el resto de dividir por 27 porque son 27 las letras en el alfabeto español.

</div></details>

<hr />
<br />

💻 [Código ejecutable](https://jdoodle.com/a/3q9i){:target="_blank"}

{% include codeEditor.html id="3q9i?stdin=0&arg=0&rw=1" %}
