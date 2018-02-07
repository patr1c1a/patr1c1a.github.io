---
layout: post
title: Lenguajes de bajo y alto nivel
date: 2016-03-29 19:00:00
categories: conceptos
tags: lenguajes
published: true
---

En el mundo de los lenguajes de programación suele categorizarse a los lenguajes mediante diferentes criterios: estáticos o dinámicos, fuertemente o débilemente tipados, interpretados o compilados, etc. Y uno de los criterios es el que los divide en lenguajes de bajo o de alto nivel, también mencionados como lenguajes de primera a cuarta generación.

Cuando se habla de "bajo nivel" se está, en realidad, haciendo referencia a lenguajes más cercanos al código entendible por una computadora, pero más lejanos a lo entendible por los humanos. Los lenguajes de alto nivel son más entendibles por un humano, pero contienen abstracciones de las instrucciones que la computadora "sabe" interpretar.

Asimismo, los lenguajes de primera generación son los de más bajo nivel, es decir, los que están más cerca del lenguaje que entiende una computadora. Los lenguajes de cuarta generación son los de más alto nivel.

## Lenguajes de 1º generación

Son códigos de máquina que dependen de cada procesador y arquitectura. Por ejemplo, para sumarle 1 a un número, se podría utilizar una instrucción como _1001101010000001_. Obviamente, es imposible programar de esta manera, recordando cada instrucción.

## Lenguajes de 2º generación

Son palabras asociadas a cada instrucción de código de máquina. Cada una de estas palabras equivale a una instrucción de los lenguajes de primera generación (por esto se dice que la equivalencia es 1 a 1). Por ejemplo, para sumarle 1 a un número, podría utilizarse una instrucción como _ADD x, 1_. Programar en este tipo de lenguajes (normalmente llamados "ensamblador", y dependientes de cada arquitectura de procesador) suele ser trabajoso pero a la vez provee un control total sobre el código, permitiendo una gran eficiencia. Suele utilizarse este tipo de lenguajes para construir piezas de software que requieren interactuar directamente con el hardware (como los controladores) o con el sistema operativo (como un compilador).

## Lenguajes de 3º generación

Aquí comienzan los lenguajes de alto nivel, y se los llama así porque una instrucción de alto nivel, normalmente, representa a varias de bajo nivel. Están más cerca del lenguaje humano y abstraen el código de un procesador o arquitectura concreto para que sea independiente y pueda usarse en varias arquitecturas diferentes. Con una sola instrucción de alto nivel basta para efectuar tareas que, a bajo nivel, requerirían de varias instrucciones más. Este código ya no resulta tan eficiente como el código escrito en lenguajes de primera o segunda generación, pero en la generalidad de los casos las diferencias son despreciables. Para convertir el código de estos lenguajes a código de máquina (deshaciendo el nivel de abstracción) es necesario un compilador o un intérprete. En esta categoría encontramos a la mayoría de los lenguajes de mayor utilización en la actualidad, como Java, C#, C++, Python, etc.

## Lenguajes de 4º generación

Tienen el mayor nivel de abstracción y suelen tener propósitos muy específicos y limitados a un objetivo concreto. Son lenguajes no procedurales. Entre ellos puede incluirse CSS y SQL.

También suele nombrarse una **quinta generación**, en la que se incluyen los lenguajes visuales, que se programan mediante una interfaz visual y requiriendo del programador menos conocimientos de programación.
