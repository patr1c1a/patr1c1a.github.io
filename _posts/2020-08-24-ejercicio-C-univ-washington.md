---
layout: post
title: Ejercicio de examen, resuelto - Analizar código C
date: 2020-08-24 12:00:00
categories: ejercicios
tags: analizar
published: true
---


Veamos un ejercicio de examen de la Universidad de Washington, con su resolución. En esta oportunidad se busca analizar el código de un programa escrito en C.


![Ejercicio resuelto de programación en C]({{ site.url }}/assets/2020-08-24-ejercicio-C-univ-washington.png)
{% include accesibilidad.html %}

Ejercicio de examen (resuelto) de la Universidad de Washington (CSE 374 Programming Concepts and Tools, 3/15/12). "Conceptos y herramientas de programación".

¿Qué salida se obtiene al ejecutar el siguiente programa en C?

```c
#include <stdio.h>
#define FOO(x,y) x + y
#define BAR(x,y) y * x

int main() {
    int a = 2;
    int b = 3;
    int c = 5;
    printf("%d\n", FOO(a+b,c));
    printf("%d\n", BAR(a+b,c));
    printf("%d\n", BAR(FOO(a,c),BAR(b,b)));
    return 0;
}
```

Respuesta:

10

13

23
</div></details>
<hr />


✏️ Explicación del código:
<br />Las instrucciones `#define` se utilizan para crear macros. Una macro es un fragmento de código al que se le da un nombre y, cuando se usa ese nombre, se reemplaza textualmente por el código de la macro.
<br />Las macros de este ejercicio tienen parámetros pero no son exactamente iguales a una función, ya que siempre se hace un reemplazo textual del código.
<br />📍 Es decir que, donde dice `FOO(a+b,c)`, debido a que **FOO** está definida como `FOO(x,y) x + y`, entonces **x** toma el valor de `a+b` mientras que **y** toma el valor de `c`. Haciendo un reemplazo textual nos queda `a+b+c`. Si `a=2, b=3, c=5` finalmente nos queda `2+3+5`.
<br />📍 En el caso de `BAR(a+b,c)`, al estar definida como `BAR(x,y) y * x`, entonces se reemplaza **y** por `5`, mientras que **x** se reemplaza por `2+3`, lo que nos deja con `5*2+3`. Teniendo en cuenta la precedencia de los operadores, calculamos `(5*2)+3` y nos da 13.
<br />📍 En la última operación, `BAR(FOO(a,c),BAR(b,b))`, el reemplazo hace que quede `BAR(2+5,3*3)` que se expande luego a `3*3*2+5`, lo cual nos da como resultado 23 (porque se ejecuta primero `3*3*2` y luego a eso se le suman `5`).

<br />En [esta herramienta](https://godbolt.org/z/qcnh6KsbW){:target="_blank"} es posible ver las macros expandidas por el preprocesador (si compiláramos nuestro programa manualmente, usaríamos una instrucción como esta: `gcc -E programa.c`). Para la función main, el preprocesador obtendrá un resultado como el siguiente:

```c
int main() {
    int a = 2;
    int b = 3;
    int c = 5;
    printf("%d\n", a+b + c);
    printf("%d\n", c * a+b);
    printf("%d\n", b * b * a + c);
    return 0;
}
```

💻 [Ver el código en ejecución](https://jdoodle.com/a/3pG4){:target="_blank"}
{% include codeEditor.html id="3pG4?stdin=0&arg=0&rw=1" %}

<br />&nbsp;
