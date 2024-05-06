---
layout: post
title: ¡Cuidado con la concatenación implícita!
date: 2024-05-06 09:00:00 -0300
categories: python
tags: strings
published: true
---

Varios lenguajes soportan la concatenación implícita de literales string. Algunos ejemplos son C, C++, Python, Ruby, Swift... Esto podría causar problemas difíciles de detectar a simple vista, como el ejemplo que se muestra donde, al existir un valor por defecto para el segundo parámetro, si se omite la coma en la lista de argumentos, ambos strings se pasan al primer parámetro, concatenados como uno solo.


![Concatenación implícita]({{ site.url }}/assets/2024-05-06-concatenacion-implicita.png)


&nbsp;

{% include accesibilidad.html %}

¡Cuidado con la concatenación implícita!

¿Qué problema tiene esta lista en C?

```c
char *lista[] = {
        "nombre"
        "apellido",
        "e-mail",
        "domicilio"
    };
```

Veamos su contenido: nombreapellido, e-mail, domicilio

Sin una coma entre los dos primeros elementos, no se produce un error sino una concatenación.

Algunos lenguajes concatenan los strings literales adyacentes.

Este ejemplo en C++ muestra que podría darse un error poco evidente si la intención fuera pasar "apellido" como segundo argumento:

```c++
std::string funcion(std::string a, std::string b = "") {
    return a;
}

int main() {
    std::cout << funcion("nombre" "apellido");
    return 0;
}
```

</div></details>
<br />&nbsp;

<hr />
