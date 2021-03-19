---
layout: post
title: La variable __name__ en Python
date: 2021-03-15 12:00:00
categories: python
tags: name
published: true
---

En Python suele usarse <pre><code>if __name__ == "__main__"</code></pre> cuando hay más de un módulo en el programa, para ejecutar o evitar que se ejecuten ciertas instrucciones.

Cuando se importa un módulo, el código que está dentro de las funciones no se ejecuta automáticamente, pero sí el que está fuera. Es por eso que en el ejemplo de la imagen cambia el resultado según cuál archivo se ejecute.


![Variable __name__ en Python]({{ site.url }}/assets/2021-03-15-variable-name-python.png)

