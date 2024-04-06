---
layout: post
title: Desafío C# número 3
date: 2024-04-05 20:00:00 -0300
categories: desafios csharp
tags: atributos herencia poo
published: true
---
Lo importante en este desafío es aplicar una de las características de la programación orientada a objetos. ¿Sabrías decir cuál, y entonces descubrir la solución correcta?

Si quisiéramos ejecutar el código del ejemplo, deberíamos instanciar el objeto desde dentro de algún método en una clase. Además, para acceder a los campos de ese objeto, deberíamos agregar "getters" y "setters" (o bien hacer que los campos tengan el modificador de acceso "public" en lugar de "private").

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la c: "r, g, b, tonalidad, saturacion, luminosidad".
<br />
<br />✏️ Explicación: La clase `ColorExtendido` hereda de `Color` y, por ende, todos sus atributos.
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/66Qm){:target="_blank"}
  </div>
{% include codeEditor.html id="66Qm?stdin=0&arg=0&rw=1" %} 
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2024-04-06-desafio-csharp-3-solucion.png)
  </div></details>

<br />
<br />
**Desafío C#** 👇
<br />
![Desafío C# número 3]({{ site.url }}/assets/2024-04-06-desafio-csharp-3.png)

{% include accesibilidad.html %}

Desafío C#

¿Qué atributos contendrá el objeto 'ce' instanciado?

```c#
class Color
{
    private int r, g, b;
} 

class ColorExtendido : Color
{
    private int tonalidad, saturacion, luminosidad;
}

// Instanciar objeto:
ColorExtendido ce = new ColorExtendido();
```

Opciones:

a) tonalidad, saturacion, luminosidad

b) r, g, b

c) r, g, b, tonalidad, saturacion, luminosidad

d) r, g, b si el objeto se crea en memoria stack; tonalidad, saturacion, luminosidad si se crea en memoria heap.


</div></details>
