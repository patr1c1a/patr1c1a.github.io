---
layout: post
title: Desafío C++ número 5
date: 2020-01-15 21:00:00
categories: desafios c++
tags: challenge
published: true
---

Desafío C++

❓ ¿Qué hace esta función recursiva?

▶️ [Este video puede ayudarte a entender la recursividad](https://youtu.be/ymaBXPjiaPY){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✏️ La función recibe un string y lo retorna invertido. Si es vacío o tiene 1 solo carácter, retorna el mismo string, sin modificaciones.
<br />
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pLy){:target="_blank"}
  </div>
{% include codeEditor.html id="3pLy?stdin=0&arg=0&rw=1" %}
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2020-01-15-desafio-cpp-5-solucion.png)
</div></details>

<br />
<br />
**Desafío C++** 👇

![desafío C++ número 5]({{ site.url }}/assets/2020-01-15-desafio-cpp-5.png)

{% include accesibilidad.html %}

```cpp
string rev(string cadena) {
    int len=cadena.length();
    if (len==0 or len==1)
        return cadena;
    else
        if (len==2) {
            string res = "";
            return res+cadena[1]+cadena[0];
        }
        else {
            char primero=cadena[0];
            char ultimo=cadena[len-1];
            string interior=cadena.substr(1, len-2);
            return ultimo+rev(interior)+primero;
        }
}
```

¿Qué retorna esta función ante la siguiente invocación?

```cpp
rev("Este es un algoritmo recursivo!")
```
</div></details>
