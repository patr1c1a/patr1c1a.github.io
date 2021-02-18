---
layout: post
title: Desafío Python número 10
date: 2021-03-03 12:00:00
categories: desafios python
tags: tuplas iteraciones
published: false
---
¡Nuevo desafío Python!

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ EL PROBLEMA ESTÁ EN LA LÍNEA 1: la segunda tupla solo tiene 2 elementos, por lo que se arroja el siguiente error al intentar "desempaquetar" durante la iteración:
_ValueError: not enough values to unpack (expected 3, got 2)_. La iteración falla pues se intenta desempaquetar usando tres variables -nombre, edad, pais- y la segunda tupla tupla no tiene suficientes elementos.
<br />
<br />✏️ Para solucionarlo, deberíamos agregar un valor a la segunda tupla. Para que sea semánticamente correcto, debería agregarse un número en la posición 1 de la segunda tupla.
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://repl.it/@programacionde1/Python-Desafio-10){:target="_blank"}
  </div>
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2021-03-03-desafio-python-10-solucion.png)
  </div></details>

<br />
<br />
**Desafío Java** 👇
<br />
![Desafío Python número 10]({{ site.url }}/assets/2021-03-03-desafio-python-10.png)

