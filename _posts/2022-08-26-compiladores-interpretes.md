---
layout: post
title: Compiladores e intérpretes
date: 2022-08-23 12:00:00
categories: conceptos
tags: compiladores intérpretes
published: true
---

La diferencia entre lenguajes "compilados" e "interpretados" suele influir en sus prestaciones, su velocidad de ejecución y su flexibilidad. Mientras que un compilador traduce el código para que pueda ejecutarlo el procesador, un intérprete lo ejecuta directamente.

De todas formas, muchos lenguajes tienen partes compiladas y partes interpretadas (como Java, que debe compilarse a "byte-code" para que luego una máquina virtual -la JVM- lo interprete).

Otras publicaciones relacionadas:

[Cómo funciona un compilador]({% post_url 2019-11-13-funcionamiento-compilador %})

[Cómo optimiza código un compilador]({% post_url 2019-11-27-optimizaciones-compilador %})


![Compiladores e intérpretes]({{ site.url }}/assets/2022-08-26-compiladores-interpretes.png)


{% include accesibilidad.html %}
Compiladores  e  intérpretes

Compilador: Traduce el código escrito en un lenguaje de programación a instrucciones en "código de máquina" que el procesador pueda entender.

Normalmente, tras la compilación se genera un archivo ejecutable que puede usarse para correr el programa las veces que sea.

Intérprete: Lee el código escrito en un lenguaje de programación y lo "interpreta", instrucción por instrucción, cada vez que el programa se ejecuta.

El código vuelve a interpretarse con cada ejecución, lo que suele hacer a los lenguajes interpretados más lentos que los compilados.

</div></details>





<hr />
