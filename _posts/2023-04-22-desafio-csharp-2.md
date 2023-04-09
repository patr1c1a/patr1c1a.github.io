---
layout: post
title: Desafío C# número 2
date: 2023-04-22 21:00:00
categories: desafios csharp
tags: propiedades
published: true
---
¿Qué crees que sucede cuando se ejecuta este código? ¿Qué corregirías?

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la c: "Nombre del empleado: Juan, Salario: 0".
<br />
<br />✏️ Explicación: El constructor de la clase Empleado hace incorrectamente la asignación de la propiedad Salario, debido a que se asigna la propiedad (cuyo identificador comienza en mayúscula) al parámetro (en minúsculas), cuando debería ser a la inversa. Esto no impide la compilación, pero sí ocasiona que el valor del parámetro salario nunca se asigne a la propiedad Salario, por lo que ésta toma el 0 como valor por defecto para un dato de tipo int.
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/66Qo){:target="_blank"}
  </div>
{% include codeEditor.html id="66Qo?stdin=0&arg=0&rw=1" %} 
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2023-04-22-desafio-csharp-2-solucion.png)
  </div></details>

<br />
<br />
**Desafío C#** 👇
<br />
![Desafío C# número 2]({{ site.url }}/assets/2023-04-22-desafio-csharp-2.png)

{% include accesibilidad.html %}

Desafío C#

¿Cuál es la salida de este programa?

```c#
class Empleado {
   public string Nombre;
   public int Salario;
   public Empleado(string nombre, int salario) {
      Nombre = nombre;
      salario = Salario;
   }
}

class Programa {
    static void Main() {
    Empleado emp = new Empleado("Juan", 2500);
    Console.WriteLine("Nombre del empleado: " + emp.Nombre + ", Salario: " + emp.Salario);
    }
}
```

Opciones:

a. <Error de compilación>

b. Nombre del empleado: Juan, Salario: 2500

c. Nombre del empleado: Juan, Salario: 0


</div></details>
