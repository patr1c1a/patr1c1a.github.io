---
layout: post
title: Datos binarios vs. texto
date: 2023-03-12 20:00:00 -0300
categories: otros
tags: binario ascii unicode
published: true
---

Cuando un programa crea o manipula archivos, será importante definir en qué forma deben almacenarse e interpretarse los datos.

![DATOS BINARIOS VS. TEXTO]({{ site.url }}/assets/2023-03-12-binario-texto.png)


&nbsp;

{% include accesibilidad.html %}

Datos binarios vs. texto

Representación de datos en la computadora: Las computadoras entienden unos y ceros –sistema binario– y de esta forma representan todos los datos (números, letras, etc.).

Ejemplo: el carácter "A" en codificación ASCII se representa con el número binario 01000001 (que equivale al número 65 en sistema decimal).

Cada carácter en ASCII estándar usa 8 bits (1 byte) mientras que, en UNICODE-32, ocupa 32 bits (4 bytes).

Si escribimos el número 4000000000 como texto ASCII, estaríamos ocupando 10 bytes, ya que el número tiene 10 dígitos (10 caracteres). Si, en cambio, lo almacenamos como número binario, alcanzaría con solo 4 bytes –o  32 bits–, pues con eso podemos representar 232 valores (lo que equivale a 4294967296 y es suficiente para almacenar el número 4000000000).

Almacenando los datos en formato binario, se ahorra espacio y se evita la conversión entre texto y binario. Pero, si necesitamos almacenar algo entendible para los humanos, los datos binarios no serán comprensibles y será mejor almacenarlos como texto.

</div></details>



<hr />
