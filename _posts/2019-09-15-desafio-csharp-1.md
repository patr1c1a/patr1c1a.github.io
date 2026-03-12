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
<br />La función retorna true si la cadena es un palíndromo o vacía, ignorando mayúsculas y minúsculas y también espacios (pero no los símbolos, letras acentuadas o signos gramaticales). Con cualquier palíndromo que cumpla estas condiciones retornará true.
<br />
<div markdown="1">💻 [Ejecutar el código](https://paiza.io/projects/fBJV3dwtgfhpjc3iefe9ZA){:target="_blank"}
  </div>
{% include codeEditor_paiza.html id="fBJV3dwtgfhpjc3iefe9ZA" %}
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-09-15-desafio-csharp-1-solucion.png)
  </div></details>
<br />
<br />
**Desafío C#** 👇

![Desafío C# 1]({{ site.url }}/assets/2019-09-15-desafio-csharp-1.png)

{% include accesibilidad.html %}

Dada la siguiente función en C#:

```csharp
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
```

Dar un ejemplo de un string que podría usarse como argumento en la llamada a esta función si queremos que retorne true.

```csharp
string cadena="aquí la cadena a usar";
Console.WriteLine(f(cadena));
```

</div></details>
---
