---
layout: post
title: Desafío Java número 8
date: 2025-05-24 08:00:00 -0300
categories: desafios java
tags: variables referencia
published: true
---

¡Veamos un desafío con Java! Este es un tema que suele generar errores comunes al trabajar con colecciones (List, Map), APIs, o cualquier objeto mutable. Entenderlo evita bugs del tipo "¿Por qué mi objeto cambió... o no cambió?".

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la a: "Hola mundo".
<br />
<br />✏️ Explicación: la variable `saludo` es mutable: cuando se llama a `modificar(saludo)`, Java pasa una copia de la referencia (dirección de memoria) al objeto original. 

`texto.append("mundo")` modifica el objeto original (porque `texto` apunta al mismo StringBuilder que `saludo`).

`texto = new StringBuilder("Adiós")` no afecta al original: esta línea hace que `texto` pase a apuntar a un nuevo objeto ("Adios"), pero la referencia original (`saludo`) sigue apuntando a la posición de memoria que contiene "Hola mundo". Reasignar `texto` solo cambia la referencia local dentro del método `modificar()`. El saludo en `main()` nunca se entera del nuevo objeto.
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://paiza.io/projects/k7xwfpdhajPwG17-OI1RCw){:target="_blank"}
  </div>
{% include codeEditor_paiza.html id="k7xwfpdhajPwG17-OI1RCw" %} 
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2025-05-24-desafio-java-8-solucion.png)
  </div></details>

<br />
<br />
**Desafío Java** 👇
<br />
![Desafío Java número 8]({{ site.url }}/assets/2025-05-24-desafio-java-8.png)

{% include accesibilidad.html %}

Desafío Java

¿Qué imprime?

```java
public class Main {
    public static void main(String[] args) {
        StringBuilder saludo = new StringBuilder("Hola ");
        modificar(saludo);
        System.out.println(saludo);
    }

    static void modificar(StringBuilder texto) {
        texto.append("mundo");
        texto = new StringBuilder("Adios");
    }
}
```

Opciones:

a) Hola mundo

b) Hola

c) Adios

d) Hola mundo Adios


</div></details>
