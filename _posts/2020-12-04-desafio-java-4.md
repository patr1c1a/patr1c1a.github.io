---
layout: post
title: Desafío Java número 4
date: 2020-12-04 12:00:00
categories: desafios java
tags: clases poo atributos
published: true
---
☕ Este desafío es válido para Java pero también podría serlo en otros lenguajes orientados a objetos...

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la A: Se produce un error porque el atributo n es privado.
<br />
<br />✏️ Explicación: la clase Desafio tiene un atributo llamado "n" cuyo modificador de acceso es "private", lo cual hace que solo pueda accederse desde dentro de la misma clase. Al intentar leer el valor de ese atributo desde un método de la clase Main, arroja el error "n has private access in Desafio"
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pNj){:target="_blank"}
  </div>
  
{% include codeEditor.html id="3pNj?stdin=0&arg=0&rw=1" %}
  
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2020-12-04-desafio-java-4-solucion.png)
  </div></details>

<br />
<br />
**Desafío Java** 👇
<br />
![Desafío Java número 4]({{ site.url }}/assets/2020-12-04-desafio-java-4.png)

{% include accesibilidad.html %}
	
¿Qué sucede al ejecutar el programa?

a. Error: n es privado

b. Error en tiempo de ejecución

c. Se imprime el valor por defecto para los int

d. Se imprime un valor residual de memoria

```java
class Desafio {
    private int n;
} 

public class Main {
    public static void main(String args[]) { 
        Desafio d_java = new Desafio(); 
        System.out.println(d_java.n); 
    }  
}
```

</div></details>
