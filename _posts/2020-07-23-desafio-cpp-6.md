---
layout: post
title: Desafío C++ número 6
date: 2020-07-23 12:00:00
categories: desafios c++
tags: referencias funciones
published: false
---

Siguiendo con los desafíos de programación: uno con C++.⭐️✨⚡️

Si bien podríamos modificar tanto la función como la invocación para evitar el error, en este caso tenemos 4 variantes de la función, pero solo una de ellas corrige el error. Cuál es

Aclaración: el programa que se muestra es solo para "jugar" a descifrar el error. No tiene ningún sentido ni "hace" nada en especial.


<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la B.
<br />
<br />✏️ Explicación:
<br />
<br /> El código original ocasiona un error debido a que la función recibe el primer parámetro por referencia (es decir, espera una dirección de memoria), pero en la invocación se está pasando el argumento a+b. Esta operación (a+b) genera un valor temporal (el resultado de la suma).
<br />
<br />❌ A. 
<br />✔️ B. 
<br />❌ C. 
<br />❌ C. 
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://repl.it/@programacionde1/C-Desafio-6){:target="_blank"}
  </div>
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2020-07-23-desafio-cpp-6-solucion.png)
  </div></details>

<br />
<br />
**Desafío C++** 👇
<br />
![Desafío C++ número 6]({{ site.url }}/assets/2020-07-23-desafio-cpp-6.png)


