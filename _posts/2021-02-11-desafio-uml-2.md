---
layout: post
title: Desafío UML número 2
date: 2021-02-11 12:00:00
categories: desafios poo
tags: clases poo herencia
published: true
---
¿Probamos con un desafío de UML?
<br />Es un diseño simplificado para gestionar una biblioteca, pero contiene un error de concepto. ¿Lo detectaste? 🔎
<br />¿Qué sugerirías para solucionarlo?

<br />
**Desafío UML** 👇
<br />
![Desafío UML número 2]({{ site.url }}/assets/2021-02-11-desafio-uml-2.png)
<br />&nbsp;

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La clase Libro no debería heredar de Biblioteca, ya que la herencia define una relación de generalidad y un Libro no es una Biblioteca. Esto es así porque la herencia permite que las clases puedan descomponerse en otras más específicas, “heredando” las características comunes pero luego manteniendo para sí mismas las que no comparten. Si Libro hereda de Biblioteca, entonces cada Libro tendría también una colección de Socio, lo cual no tiene sentido.
<br />Entonces, puede corregirse el error haciendo que Biblioteca contenga una colección de objetos Libro.
<br /><code>Clase Biblioteca {
    Lista<Socio> socios;
    Lista<Libro> libros;
}
Clase Socio {
    int numero;
    string nombre;
}
Clase Libro {
    int codigo;
    string titulo;
    string autor;
}
</code>
<br />&nbsp;
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2021-02-11-desafio-uml-2-solucion.png)
    </div></details>



