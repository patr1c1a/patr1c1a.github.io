---
layout: post
title: Desafío C++ número 6
date: 2020-07-23 12:00:00
categories: desafios c++
tags: referencias funciones
published: true
---

Siguiendo con los desafíos de programación: uno con C++.⭐️✨⚡️

Si bien podríamos modificar tanto la función como la invocación para evitar el error, en este caso tenemos 4 variantes de la función, pero solo una de ellas corrige el error. Cuál es

Aclaración: el programa que se muestra es solo para "jugar" a descifrar el error. No tiene ningún sentido ni "hace" nada en especial.


<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la B.
<br />
<br />✏️ Explicación:
<br />
<br /> El código original ocasiona un error debido a que la función recibe el primer parámetro por referencia, pero en la invocación se está pasando como argumento la expresión a+b. Esta operación genera un valor temporal (con el resultado de a+b) que se descarta tan pronto la expresión es usada, por lo que no es posible crear una referencia a él.
<br />
<br />❌ A. Además de que no soluciona el error antedicho, no corresponde poner una instrucción return debido a que la función es de tipo void.
<br />✔️ B. Esta es la opción correcta. Aunque el argumento a+b sigue estando almacenado de manera temporal, const extiende su tiempo de vida, permitiendo leer ese valor (mas no modificarlo) dentro de la función.
<br />❌ C. En esta opción se indica que todos los parámetros sean pasados por referencia, lo cual altera el resultado final sin corregir el error.
<br />❌ D. Cambiar el tipo de la función y hacer que retorne un valor entero no soluciona el problema.
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


