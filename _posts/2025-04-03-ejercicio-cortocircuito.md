---
layout: post
title: Resolvamos un ejercicio con arreglos
date: 2025-04-03 09:00:00 -0300
categories: ejercicios csharp
tags: arreglos bucles cortocircuito
published: true
---

Vemos un ejercicio con arreglos y una posible solución que tiene un error... Aunque la resolución, en general, está bien encarada y su complejidad algorítmica con respecto al tiempo es de O(N), hay un error evidente: las condiciones de los bucles `while` acceden a elementos del arreglo mediante su índice sin antes validar que el índice esté en el rango correcto.

La corrección a hacer es simple: usamos una "evaluación de cortocircuito" invirtiendo las partes de la condición para verificar que el índice sea válido antes de usarlo. El operador `and` hace que, al ser falsa la primera parte de la condición, la segunda no se evalúe (evitando así el error).


![Evaluación de cortocircuito]({{ site.url }}/assets/2025-04-03-ejercicio-cortocircuito.png)


&nbsp;

{% include accesibilidad.html %}

Dado un arreglo de números, ordenado en forma ascendente, retornar el máximo entre la cantidad de números positivos y negativos (el 0 no se considera positivo ni negativo).

Ejemplo 1:

Arreglo: [-8,-5,-3,0,9,13]

Salida esperada: 3.

Ejemplo 2:

Arreglo: [0,0,10,20,30,40]

Salida esperada: 4.

Esta resolución en C# tiene un error:

```csharp
public class Solucion 
{
  public int Maximos(int[] n) 
  {
    int i = 0;
    int neg = 0;
    int pos = 0;
    while (n[i] < 0 && i < n.Length)
    {
      neg++;
      i++;
    }
    while (n[i] == 0 && i < n.Length)
      i++;
    if (i < n.Length)
      pos = n.Length - i;
    return Math.Max(neg, pos);
  }
}
```

Los "while" intentan acceder a un elemento por su índice antes de verificar si está en el rango válido. Cuando la variable i sea mayor que el último índice válido, habrá un error.

Lo corregimos con una "evaluación de cortocircuito", invirtiendo el orden en las condiciones:

```csharp
while (i < n.Length && n[i] < 0)
{
  neg++;
  i++;
}
while (i < n.Length && n[i] == 0)
  i++;
```

Operación AND: si la primera parte da falso, toda la expresión da falso. La segunda parte no se evalúa cuando ya se sabe que la expresión entera será falsa.

</div></details>
<br />&nbsp;
<hr />
