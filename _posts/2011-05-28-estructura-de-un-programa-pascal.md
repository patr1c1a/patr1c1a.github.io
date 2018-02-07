---
layout: post
title: Estructura de un programa en Pascal
date: 2011-05-28 19:12:00
categories: pascal
tags: paradigma_imperativo
published: true
---

Pascal es un lenguaje que no es sensible a mayúsculas y minúsculas, por lo que las palabras reservadas y los identificadores pueden ser escritos mezclando mayúsculas y minúsculas: &#8220;miVariable&#8221; es lo mismo que &#8220;mivariable&#8221;.

Es importante tener en cuenta que las instrucciones, en Pascal, finalizan con punto y coma (;) a excepción de la instrucción que finaliza el programa, que se escribe seguida de un punto.

Un programa en Pascal está compuesto por diversos bloques de código, algunos de ellos opcionales y otros de existencia obligatoria:

- **Cabecera:** indica el nombre del programa sólo a modo de título o información. El nombre del archivo que contiene el programa puede no ser el mismo. El nombre del programa debe comenzar con una letra o un guión bajo, anteponiéndose la palabra reservada “program” y finalizando la línea con un punto y coma.

- **Declaración de unidades:** para el caso en que el programa requiera de la utilización de unidades externas, con el fin de adicionar funciones a las predefinidas de turbo pascal. La palabra reservada es “uses”, seguida del nombre del archivo que refiere a la unidad.

- **Declaración de constantes:** la palabra reservada para declarar una constante es “const”, seguida por el identificador de dicha constante, el cual debe comenzar con una letra o un guión bajo, un signo de igualdad (=) y el valor de la constante.

- **Declaración de tipos:** sector en el cual se definen nuevos tipos de datos. La palabra reservada es “type”, seguida del nombre del tipo, un signo de igualdad (=) y la definición.

- **Declaración de variables globales:** afectan a todo el programa.

- **Declaración de módulos:** también llamados “subprogramas” o “subrutinas”. Todos los módulos y funciones deben implementarse antes de ser utilizados. Es decir, si un módulo invoca a otro, el código de este último deberá estar situado en una posición anterior a la invocación. Esto es debido a que el compilador de Pascal interpreta el código en orden, comenzando por la primera línea. Un módulo puede contener declaración de variables locales (sólo existen dentro de él). Comienzan con la palabra “begin” y finalizan con “end;” (el punto y coma indica que el programa continúa).

- **Declaración de variables locales al programa principal:** Pascal requiere que las variables estén declaradas (indicando su tipo) antes de ser utilizadas. Justo antes de comenzar el cuerpo del programa principal, deben definirse las variables que se van a utilizar en él. Se indican con la palabra “var” seguida del nombre de la variable y el tipo de dato que representa.

- **Cuerpo del programa:** el programa principal debe estar encerrado entre las etiquetas “begin” y “end.” (el “end” final va seguido de un punto).

&nbsp;

Puede encontrarse documentación detallada sobre los diferentes estándares de Pascal en <a href="http://pascal-central.com/standards.html" target="_blank">http://pascal-central.com/standards.html</a>.

&nbsp;
