---
layout: post
title: Pseudocódigo
date: 2015-06-27 19:00:00
categories: conceptos
tags: algoritmos resolución_problemas
published: true
---

El pseudocódigo es una manera informal de escribir código sin utilizar la sintaxis estricta de algún lenguaje de programación. No es código entendible por una máquina (no es ejecutable) sino por humanos, por esto se utiliza con mucha frecuencia para enseñar a programar, para diseñar la estructura de un programa o para documentar algoritmos.

A pesar de que es una manera informal de escribir algoritmos y de ser independiente de un entorno de programación concreto, esto no significa que se pueda escribir pseudocódigo sin saber nada de programación, ya que deben aplicarse las estructuras de control y los conceptos básicos.

En general, el pseudocódigo puede pasarse luego a un lenguaje de programación concreto. Aunque, al ser una herramienta general, el lenguaje de programación elegido será luego el que brinde las estructuras concretas a utilizar. Así, el pseudocódigo no tiene ninguna sintaxis en particular ni reglas estrictas para su escritura, sino que debe permitir expresar algoritmos de manera sencilla y sin confusiones.

Como no existe una sintaxis específica, entonces podemos escribir el pseudocódigo en el idioma en que nos resulte más cómodo, en lugar de utilizar el inglés (que utilizan la mayoría de lenguajes).

Podría decirse que el pseudocódigo está en un punto intermedio entre el lenguaje natural que usamos los humanos y un lenguaje de programación entendido por la computadora. Por ejemplo, si quisiéramos determinar si una persona es mayor de edad (tomando la mayoría a los 18 años):

En lenguaje natural:

<pre>Preguntar qué edad tiene la persona. Si la respuesta es un número mayor o igual a 18, la persona es mayor de edad.</pre>

En pseudocódigo:

<pre><code>LEER edad
SI edad >= 18 ENTONCES
    MOSTRAR MENSAJE "La persona es mayor de edad"
SI NO
    MOSTRAR MENSAJE "La persona es menor de edad"</code></pre>

En un lenguaje de programación como C++:

<pre><code>int edad;
cout << "Ingresar edad de la persona: ";
cin >> edad;
if (edad >= 18)
    cout << "\nLa persona es mayor de edad: ";
else
    cout << "\nLa persona es menor de edad: ";</code></pre>
