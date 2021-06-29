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
<br />✅ La respuesta correcta es la d: Se produce un error de compilación porque la variable x está declarada dentro de un bloque (formado por las llaves) y no es accesible fuera de él.
<br />
<br />✏️ Explicación: la variable x se encuentra declarada en un bloque definido por las llaves de las líneas 4 y 6 del código. Fuera de ese bloque, la variable no existe.
<br />Varias personas han preguntado si las llaves estaban incorrectamente colocadas, y no es así. El error se produce por un problema de alcance de la variable cuando se intenta acceder a ella desde un ámbito mayor al bloque que la contiene. Aunque este es un fragmento de código de ejemplo y es verdad que ese bloque no tiene sentido ahí, de todas formas el bloque formado por las llaves es válido.
<br />En Java, las llaves crean un bloque de código con su propio ámbito y no es necesario que ese bloque forme parte de un if, for, while, etc. 
<br />🤔 ¿Y qué pasa con el for de la línea 7? ¿Por qué no tiene llaves? La respuesta a esto es válida para varios lenguajes, no solo Java: las llaves solo son necesarias cuando el bloque incluye más de una instrucción. Si ponemos llaves en un bloque que solo contiene una instrucción, esas llaves son opcionales. En este caso, el bloque de código dentro del for tiene solo una instrucción y entonces no es obligatorio que tenga llaves.
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
