---
layout: post
title: Álgebra de Boole
date: 2022-11-13 13:00:00 -0300
categories: conceptos
tags: boole circuitos
published: true
---

Aunque parezca un tema más apropiado para expertos en matemática o electrónica, el álgebra de Boole nos permite analizar los circuitos lógicos digitales. En palabras no muy técnicas, un circuito es algo que permite dejar pasar electricidad, y puede estar abierto (la deja pasar) o cerrado (no la deja). Esto puede representarse en dos estados: 0 y 1, lo cual permite aplicar un sistema binario. Ahora ya nos suena un poco más relacionado a las computadoras, ¿no? 😉


![Microservicios vs. "monolito"]({{ site.url }}/assets/2022-11-13-algebra-boole.png)


{% include accesibilidad.html %}

Álgebra de Boole

Creada por George Boole en 1854, sirve para representar circuitos lógicos digitales.

Reconoce solo dos estados en un circuito lógico (por ejemplo: verdadero ó falso; 0 ó 1; alto ó bajo; sí ó no; abierto ó cerrado…).

Tiene dos elementos: 0 y 1, y tres operadores: and (·), or (+), not (‘), que se definen así:

Operador and:

Si A=0 y B=0, entonces A and B da 0

Si A=0 y B=1, entonces A and B da 0

Si A=1 y B=0, entonces A and B da 0

Si A=1 y B=1, entonces A and B da 1


Operador or:

Si A=0, B=0, entonces A or B da 0

Si A=0, B=1, entonces A or B da 1

Si A=1, B=0, entonces A or B da 1

Si A=1, B=1, entonces A or B da 1


Operador not:

Si A=0, entonces not A da 1

Si A=1, entonces not A da 0


</div></details>




<hr />
