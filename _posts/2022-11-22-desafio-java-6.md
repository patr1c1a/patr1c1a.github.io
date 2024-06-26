---
layout: post
title: Desafío Java número 6
date: 2022-11-22 22:00:00 -0300
categories: desafios java
tags: strings
published: true
---
Como varias personas me pidieron otro desafío Java, acá va uno, en este caso con strings 😎.

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la c: muestra el texto "veremos".
<br />
<br />✏️ Explicación: 
<br />Este método permite truncar una cadena de caracteres a la longitud máxima pasada por parámetro. De esta forma, cualquiera sea el string dado en el primer parámetro, si su longitud es mayor que la longitud máxima dada en el segundo parámetro, retornará desde el carácter en la posición 0 hasta el de la posición dada por ese máximo.
<br />La condición del "if" prevee el caso en que la longitud máxima dada sea mayor que la de la cadena (por ejemplo, si los argumentos fueran la cadena "hola" y la longitud 12), para evitar una excepción de tipo StringIndexOutOfBoundsException.
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/5wLc){:target="_blank"}
  </div>
{% include codeEditor.html id="5wLc?stdin=0&arg=0&rw=1" %} 
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2022-11-22-desafio-java-6-solucion.png)
  </div></details>

<br />
<br />
**Desafío Java** 👇
<br />
![Desafío Java número 6]({{ site.url }}/assets/2022-11-22-desafio-java-6.png)

{% include accesibilidad.html %}

¿Cuál es la salida del programa?

```java
public class DesafioJava {
    static String desafio(String cadena, int longitud) {
        if (cadena.length() <= longitud) {
            return cadena;
        } else {
            return cadena.substring(0, longitud);
        }
    }
    public static void main(String args[]) {
      System.out.println(desafio("veremos qué imprime", 7));
    }
}
```

Opciones:

a. "imprime"

b. "veremos qué"

c. "veremos"

d. "veremos qué imprime"

</div></details>
