---
layout: post
title: Desafío Java número 1
date: 2019-11-29 21:00:00
categories: desafios java
tags: referencias
published: true
---

¿Te animas a un desafío con Java? 😀

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />la respuesta correcta es la c.
<br />✏️ Explicación: Los arreglos en Java son alocados dinámicamente (son objetos). Por ende, cuando asignamos un arreglo a otro no se está realizando una copia sino que ambas variables referencian al mismo objeto. Al modificar un elemento de la variable m1, se altera la única instancia del arreglo que existe, la cual puede referenciarse como m1 o m2 indistintamente.
<br />
<br />📗 Documentación oficial: https://docs.oracle.com/javase/specs/jls/se13/html/jls-10.html
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-11-29-desafio-java-1-solucion.png)
  </div></details>

<br />
<br />
**Desafío Java** 👇

![desafío Java número 1]({{ site.url }}/assets/2019-11-29-desafio-java-1.png)
