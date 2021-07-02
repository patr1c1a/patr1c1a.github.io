---
layout: post
title: Ejercicio resuelto - Código Morse en Python
date: 2019-10-10 21:00:00
categories: python
tags: diccionario string
published: true
---

En este ejercicio resuelto con Python, convertimos texto a código Morse 😎


![Ejercicio resuelto]({{ site.url }}/assets/2019-10-10-ejercicio-python-codigo-morse.png)

{% include accesibilidad.html %}

Ejercicio con diccionario en Python

Escribir un programa que permita convertir un texto a código Morse.

Precondición: el texto solo estará compuesto por letras y/o espacios.

En esta resolución comenzamos por inicializar un diccionario con las letras (mayúsculas) y su equivalente en Morse:

```python
MORSE = {' ': '_', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', }

def convertirAMorse(frase):
    frase = frase.upper()
    fraseCodificada = ""
    for caracter in frase:
        fraseCodificada += MORSE[caracter] + " "
    return fraseCodificada

frase = input("Frase a convertir: ")
fraseCodificada = convertirAMorse(frase)
print(fraseCodificada)
```

En la instrucción `fraseCodificada += MORSE[caracter] + " "` se accede a la clave del diccionario dada por la variable `caracter`.

</div></details>


💻 [Código del programa](https://jdoodle.com/a/3qpF){:target="_blank"}

{% include codeEditor.html id="3qpF?stdin=0&arg=0&rw=1" %}


▶️ [Video: diccionarios](https://www.youtu.be/ymaBXPjiaPY){:target="_blank"}

▶️ [Video: Ejercicios con diccionarios](https://www.youtu.be/uOpW1tKKO8M){:target="_blank"}
