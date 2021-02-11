---
layout: post
title: Desafío UML número 2
date: 2021-02-11 12:00:00
categories: desafios uml
tags: clases poo herencia
published: false
---
☕ Este desafío es válido para Java pero también podría serlo en otros lenguajes orientados a objetos...

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La clase Libro no debería heredar de Biblioteca, ya que la herencia define una relación de generalidad y un Libro no es una Biblioteca.
<br />Puede corregirse el error haciendo que Biblioteca contenga una colección de objetos Libro.
<br />
<pre><code>Clase Biblioteca {
    Lista<Socio> socios;
    Lista<Libro> libros;
}
<br />&nbsp;
Clase Socio {
    int numero;
    string nombre;
}
<br />&nbsp;
Clase Libro {
    int codigo;
    string titulo;
    string autor;
}</code></pre>
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2021-02-11-desafio-uml-2-solucion.png)
  </div></details>

<br />
<br />
**Desafío UML** 👇
<br />
![Desafío UML número 2]({{ site.url }}/assets/2021-02-11-desafio-uml-2.png)


