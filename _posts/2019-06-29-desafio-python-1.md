---
layout: post
title: Desafío Python número 1
date: 2019-06-29 21:00:00
categories: desafios python
tags: strings
published: true
---

En la imagen se ven dos líneas con instrucciones. La primera asigna un string a una variable. ¿Qué hace la segunda? (no olvides que el símbolo *>>>* implica el uso del intérprete interactivo de Python, por lo que la ejecución de una operación mostrará inmediatamente su resultado).

▶️ [Para ver cómo hacer estas y otras operaciones con strings en Python, visitá este video](https://www.youtube.com/watch?v=xAigyL6Lz2s){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />La opción correcta es la b).
<br />
<br />✏️ Explicación:
<br />✅ Opción b): la operación c[:13:2] obtiene una rebanada del string c, desde el inicio y hasta el carácter en la posición 13 (o, lo que es igual, hasta la 12 inclusive), salteando caracteres de 2 en 2. Eso nos deja con el string "et su t", a lo cual se le concatena un carácter: el de la posición 16 de c, ya que len(c) es 17, al restar 1 obtenemos el 16, y la posición 16 del string c es el carácter "g".
<br />
<br />🚫 Opciones incorrectas:
<br />▪️ El string de la opción a) se obtendría si se hiciese la operación c[13:2:-1] que obtiene una rebanada desde el carácter en la posición 13 (la "r" de la palabra "string") hasta el carácter en la posición 2 (o, lo que es igua, la posición 3 inclusive), que es la última "e" de la palabra "este". Va en sentido inverso porque se indicó un "step" o "paso" de -1.
<br />▪️ La opción c) plantea un error, pero ese no es el caso. Dos cosas podían prestarse a confusión: que la rebanada c[:13:2] no tuviera una posición de inicio, pero al dejarla en blanco se toma por defecto desde el principio del string; o que len(c) da el número 17 mientras que el índice del string va del 0 al 16, pero al restarle 1 entonces obtenemos el 16 que señala el último carácter.
<br />
<br />
<div markdown="1">💻 [Código ejecutable](https://repl.it/@programacionde1/Python-Desafio-1){:target="_blank"}
  </div>
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-06-29-desafio-python-1-solucion.png)
  </div></details>

<br />
<br />
**Desafío Python** 👇
![desafío Python número 1]({{ site.url }}/assets/2019-06-29-desafio-python-1.png)
