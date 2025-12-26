---
layout: post
title: Desafío Java número 7
date: 2023-07-16 22:00:00 -0300
categories: desafios java
tags: ambito scope alcance
published: true
---
Sin ejecutar el código, ¿podrías decir qué instrucciones darían error y por qué?.

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es: líneas 6 y 10.
<br />
<br />✏️ Explicación:
<br />La línea 6 arroja el error "variable x is already defined in method funcion()". Esto sucede porque existe una variable llamada x (con el valor 1) dentro del ámbito de la función y luego, dentro de un bloque comprendido en esa misma función, se intenta reusar el mismo nombre de variable.
<br />La línea 10 arroja el error "cannot find symbol" debido a que la variable y (con el valor 3) solo existe dentro del bloque comprendido por las llaves de las líneas 5 y 8, lo que hace que no pueda accederse a ella desde fuera del ámbito de ese bloque.
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/6onl){:target="_blank"}
  </div>
{% include codeEditor.html id="6onl?stdin=0&arg=0&rw=1" %}
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2023-07-16-desafio-java-7-solucion.png)
  </div></details>

<br />
<br />
**Desafío Java** 👇
<br />
![Desafío Java número 7]({{ site.url }}/assets/2023-07-16-desafio-java-7.png)

{% include accesibilidad.html %}

Al ejecutar este código, ¿en cuál o cuáles líneas se produce algún error?

{% highlight java linenos %}
public class Ejemplo {
    
    public static void funcion() {
        int x = 1;
        {
            int x = 2;
            int y = 3;
        }
        System.out.println(x);
        System.out.println(y);
    }
    
    public static void main(String args[]) {
        funcion();
    }
}
{% endhighlight %}


</div></details>
