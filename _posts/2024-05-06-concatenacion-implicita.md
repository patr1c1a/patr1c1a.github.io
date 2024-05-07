---
layout: post
title: ¡Cuidado con la concatenación implícita!
date: 2024-05-06 09:00:00 -0300
categories: python c++
tags: strings
published: true
---

Algunos lenguajes soportan la concatenación implícita de literales string. Es algo a tener en cuenta, porque podría causar problemas difíciles de detectar a simple vista. En el ejemplo que se muestra, al existir un valor por defecto para el segundo parámetro de la función, si se omite la coma en la lista de argumentos, ambos strings se pasan al primer parámetro, concatenados como uno solo.


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

C, Python y C++ concatenan los strings literales adyacentes.

Este ejemplo muestra que podría darse un error poco evidente si la intención fuera pasar "apellido" como segundo argumento.

C++:
```cpp
string funcion(string a, string b = "") {
    return a;
}

int main() {
    cout << funcion("nombre" "apellido");
    return 0;
}
```

Python:
```python
def funcion(a, b=""):
    return a
print(funcion("nombre" "apellido"))
```

</div></details>
<br />&nbsp;

<hr />
