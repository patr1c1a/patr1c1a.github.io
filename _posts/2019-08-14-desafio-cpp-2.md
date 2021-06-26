---
layout: post
title: Desafío C++ número 2
date: 2019-08-14 21:00:00
categories: desafios c++
tags: preincremento
published: true
---

Para saber cuál es la salida de este programa, no solo debe analizarse la función invocada, sino también la invocación.

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />La respuesta es "impar".
<br />
<br />✏️ Esto es así debido al preincremento de la variable, ya que el operador ++ colocado delante de la variable hace que primero se ejecute el incremento y luego se resuelva la expresión, que en este caso es una llamada a función. Entonces, a la función se le envía el valor 11, el cual es impar (por eso, al dividirlo por 2 y quedarse con el resto, da 1 y es distinto de 0, lo que hace que la función retorne false).
  
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pI8){:target="_blank"}
  
{% include codeEditor.html id="3pI8?stdin=0&arg=0&rw=1" %}

  </div>
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-08-14-desafio-cpp-2-solucion.png)
  </div></details>

<br />
<br />
**Desafío C++** 👇
![Desafío C++ número 2]({{ site.url }}/assets/2019-08-14-desafio-cpp-2.png)

{% include accesibilidad.html %}

¿Qué imprime y por qué?

```cpp
#include <iostream>

bool paridad(int a) {
    return a%2 == 0;
}

int main() {
  int a = 10;
  if (paridad(++a))
    std::cout << "par";
  else
    std::cout << "impar";
}
```

</div></details>
