---
layout: post
title: El error en C++ que puede causar problemas inesperados
date: 2025-07-18 13:00:00 -0300
categories: c++
tags: punteros dangling
published: true
---

Este ejemplo muestra un potencial problema cuando guardamos una dirección de memoria en una variable, pero luego esa dirección se "libera" para ser reutilizada. Esto es lo que se llama "dangling pointer" y genera que no podamos predecir qué sucederá en cada ejecución del programa.

Puede provocar:
- Acceso a basura en memoria (valores inesperados)
- Crash del programa ("segfault")
- Corrupción silenciosa de datos si el puntero se usa para escritura

En un fragmento de código tan chico como el del ejemplo, es difícil que cause problemas. Pero en un programa grande, que puede tener muchos flujos de ejecución diferentes y que puede estar ejecutándose por mucho tiempo, estos bugs podrían aparecer.

💻 [Código ejecutable](https://paiza.io/projects/zZkaayNC8eDsDKn5sDTGvQ){:target="_blank"}



![El error en C++ que puede causar problemas inesperados]({{ site.url }}/assets/2025-07-18-dangling-pointer.png)


&nbsp;

{% include accesibilidad.html %}
El error en C++ que puede causar problemas inesperados

```cpp
#include <iostream>
 
int* funcion() {
    int x = 10;
    return &x;
}
 
int main() {
    int* p = funcion();
    std::cout << *p << std::endl;
}
```

Esta función genera un "dangling pointer": es un puntero que queda apuntando a una dirección inválida.

Cuando se ejecuta la función, en memoria se reserva un espacio para sus datos (la variable x). Todavía no sabemos qué retornará, así que no tenemos valor para p.

Cuando la función terminó, la memoria ocupada por x se liberó (porque era local a la función). Pero el puntero retornado queda guardando su dirección de memoria, que ahora está disponible para cualquier otro dato.

Es posible que el espacio de memoria 0xCDF2 se use para otro dato. A medida que transcurre el programa, ya no podremos asegurar que siga guardando el valor 10.

</div></details>
<br />&nbsp;
<hr />
