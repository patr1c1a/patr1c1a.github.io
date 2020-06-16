---
layout: post
title: Algoritmo para hallar el mayor y el menor número
date: 2019-08-31 21:00:00
categories: pseudocodigo
tags: bucles while
published: true
---

Este algoritmo permite obtener el mayor y el menor de una cantidad indeterminada de números leidos.

▶️ [Video explicativo](https://youtu.be/Ll8Q48_yPIM){:target="_blank"}

🔗 [Implementación en Python (para ejecutar paso a paso)](http://pythontutor.com/visualize.html#code=numero%20%3D%20int%28input%28%22Escriba%20un%20n%C3%BAmero%3A%20%22%29%29%0Amayor%20%3D%20numero%0Amenor%20%3D%20numero%0Awhile%20numero%20!%3D%200%3A%0A%20%20%20%20if%20numero%20%3E%20mayor%3A%0A%20%20%20%20%20%20%20%20mayor%20%3D%20numero%0A%20%20%20%20elif%20numero%20%3C%20menor%3A%0A%20%20%20%20%20%20%20%20menor%20%3D%20numero%0A%20%20%20%20numero%20%3D%20int%28input%28%22Escriba%20un%20n%C3%BAmero%3A%20%22%29%29&cumulative=false&curInstr=13&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%229%22,%228%22,%220%22%5D&textReferences=false){:target="_blank"}

✏️ También es posible inicializar las variables "mayor" y "menor" con valores límite para el tipo de dato (dependiente del lenguaje y la implementación, como por ejemplo INT_MAX ó INT_MIN para C y C++).

![Algoritmo para hallar el menor y el mayor número de una serie]({{ site.url }}/assets/2019-08-31-algoritmo-mayor-menor.png)
