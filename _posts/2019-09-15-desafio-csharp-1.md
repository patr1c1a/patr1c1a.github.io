---
layout: post
title: Desafío C# número 1
date: 2019-09-15 21:00:00
categories: desafios csharp
tags: strings
published: true
---

Analizando la función dada, ¿qué características debe tener el argumento para que la función retorne true? 😎 

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />
<br />La función retorna true si la cadena es un palíndromo o vacía, considerando mayúsculas y minúsculas y también espacios, pero exceptuando acentos y signos gramaticales. Con cualquier palíndromo que cumpla estas condiciones retornará true.
<br />
<div markdown="1">💻 [Ejecutar el código](https://jdoodle.com/a/3pAs){:target="_blank"}
  </div>
{% include codeEditor.html id="3pAs?stdin=0&arg=0&rw=1" %}
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-09-15-desafio-csharp-1-solucion.png)
  </div></details>
<br />
<br />
**Desafío C#** 👇

![Desafío C# 1]({{ site.url }}/assets/2019-09-15-desafio-csharp-1.png)

<hr />
### Versión accesible (apta para lectores electrónicos):

Dada la siguiente función en C#:

~~~
public static bool f(string cadena) 
{
  cadena=cadena.Replace(" ", "").ToLower();
  int longitud=cadena.Length; 
  for (int i=0; i < longitud/2; i++) 
  { 
    if (cadena[i] != cadena[longitud-i-1]) 
    {
      return false;
    }
  }
  return true; 
} 
~~~
{: .language-csharp}

Dar un ejemplo de un string que podría usarse como argumento en la llamada a esta función si queremos que retorne true.

~~~
string cadena="aquí la cadena a usar";
Console.WriteLine(f(cadena));
~~~
{: .language-csharp}
