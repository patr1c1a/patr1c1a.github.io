---
layout: post
title: Desafío Java número 3
date: 2020-07-15 12:00:00
categories: desafios java
tags: strings null
published: true
---
☕ Hace tiempo que no hacemos un desafío, así que vamos con uno de Java. ¿Cuál es la respuesta correcta? 🤔

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la C: la línea 6 genera un error.
<br />
<br />✏️ Explicación: el método recibe un arreglo de String y retorna el String más largo contenido en el arreglo. Para esto, itera por todos los elementos, quedándose con el primero que tenga la mayor longitud.
<br />
<br />❌ A. Las líneas 3 y 4 declaran dos variables (objetos) de tipo String cuyos valores son null. Esto es totalmente válido, por lo que no habrá error en tiempo de compilación ni en tiempo de ejecución. Solo será cuestión de tener cuidado de no utilizar objetos nulos (que es lo que sucede en la línea 6) para evitar errores.
<br />❌ B. El operador == usado con objetos de tipo String compara las referencias (direcciones de memoria), independientemente del valor que tengan esos strings. Entonces, es válido comparar para saber si dos referencias son iguales.
<br />✔️ C. El error se provoca durante la ejecución, por ser null el objeto cadena1, entonces se arroja una NullPointerException. Lo interesante es que el hecho de que cadena2 sea nulo no genera ningún error. Podríamos probar esto cambiando la línea 3 para asignar cualquier string válido a cadena1, por ejemplo: <code>String cadena1="hola";</code> y entonces el código no daría errores, aunque cadena2 continúe siendo null. Esto se debe a que no es posible usar el operador "." (punto) sobre un objeto nulo: null.equals() es una operación inválida. 
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pNt){:target="_blank"}
  </div>
  
{% include codeEditor.html id="3pNt?stdin=0&arg=0&rw=1" %}
  
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2020-07-15-desafio-java-3-solucion.png)
  </div></details>

<br />
<br />
**Desafío Java** 👇
<br />
![Desafío Java número 3]({{ site.url }}/assets/2020-07-15-desafio-java-3.png)

{% include accesibilidad.html %}

```java
public class Main {
   public static void main(String[] args) {
      String cadena1 = null;
      String cadena2 = null;
      System.out.println(cadena1 == cadena2);
      System.out.println(cadena1.equals(cadena2));
   }
}
```

¿Cuál o cuáles de las líneas del código anterior causan un error?

A. La tercera y la cuarta.

B. La quinta.

C. La sexta.
</div></details>
