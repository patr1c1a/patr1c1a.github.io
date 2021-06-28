---
layout: post
title: Desafío Java número 5
date: 2021-06-27 12:00:00
categories: desafios java
tags: bloque
published: true
---
Analicemos cuidadosamente el código de este desafío... ¿Qué crees que sucede cuando se lo ejecuta? ¿Y por qué?

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la c: Se produce un error de compilación porque la variable x está declarada dentro de un bloque (formado por las llaves) y no es accesible fuera de él.
<br />
<br />✏️ Explicación: la variable x se encuentra declarada en un bloque definido por las llaves de las líneas 4 y 6 del código. Fuera de ese bloque, la variable no existe. Varias personas han preguntado si las llaves estaban incorrectamente colocadas, y no es así. Que el código no tiene sentido (además de dar un error) es verdad, pero el error está en intentar acceder a una variable donde no tiene alcance. En Java, las llaves crean un bloque de código con su propio ámbito y esto nos permite crear bloques donde queramos (incluso si no forma parte de un if, for, while, etc.): es decir que el bloque formado por las llaves que contienen a la declaración de x es válido.
<br />¿Y qué pasa con el for de la línea 7? ¿Por qué no tiene llaves? La respuesta a esto es válida para varios lenguajes, no solo Java: las llaves solo son necesarias cuando el bloque incluye más de una instrucción. Si ponemos llaves en un bloque que solo contiene una instrucción, esas llaves son opcionales. En este caso, el bloque for solo tiene una instrucción y no es obligatorio que tenga llaves.
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3puW){:target="_blank"}
  </div>
{% include codeEditor.html id="3puW?stdin=0&arg=0&rw=1" %} 
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2021-06-27-desafio-java-5-solucion.png)
  </div></details>

<br />
<br />
**Desafío Java** 👇
<br />
![Desafío Java número 5]({{ site.url }}/assets/2021-06-27-desafio-java-5.png)

{% include accesibilidad.html %}

¿Cuál es la salida del programa?

```java
class Desafio {
    public static void main (String[] args) {
        int i = 0;
        {
            int[] x = {0, 1, 2};
        }
        for (i = 0; i < x.length; i++)
            System.out.print(x[i]);
    }
}
```

Opciones:

a. 012.

b. 000.

c. Error en tiempo de ejecución.

d. Error de compilación.

</div></details>
