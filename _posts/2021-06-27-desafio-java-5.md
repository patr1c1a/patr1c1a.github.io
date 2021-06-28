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
<br />✅ La respuesta correcta es la c: Se produce un error de compilación porque la variable x está declarada dentro del bloque que la engloba y no es accesible fuera de él.
<br />
<br />✏️ Explicación: la variable x se encuentra declarada en un bloque definido por las llaves de las líneas 4 y 6 del código. Fuera de ese bloque, la variable no existe (recordemos que, en Java, las llaves crean un bloque de código con su propio ámbito). El hecho de que la variable sea un array no hace ninguna diferencia a este respecto. Podría tratarse de una variable de cualquier otro tipo y el comportamiento sería el mismo: al intentar acceder a ella desde un ámbito mayor a donde está declarada, se produciría un error en la compilación.
<br />Si, en este código, las líneas 7 y 8 (del bucle for que imprime el arreglo) se movieran hacia dentro del bloque donde está declarada x, entonces se podría compilar y ejecutar el código sin problemas, obteniendo la salida 012. También, si dentro del bloque que contiene a x creáramos otro "sub-bloque", podríamos acceder a x, ya que este último estaría incluido dentro del ámbito del bloque que lo contiene. 
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3puW){:target="_blank"}
  </div>
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

a. 012

b. 000

c. Error en tiempo de ejecución

d. Error de compilación

</div></details>
