---
layout: post
title: Ejercicio C++ resuelto - mapas
date: 2019-11-20 21:00:00
categories: c++ ejercicios
tags: mapas
published: true
---

Conversión de números romanos, en C++.

🤓 ¿Sabías que los romanos no siempre usaron las mismas reglas para escribir sus números y que éstas varían según la época? De acuerdo a las reglas modernas, esta expresión regular comprueba la validez de un número romano:
<pre><code>(^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$)</code></pre>

▶️ [Videos de C++](https://www.youtube.com/playlist?list=PLb_E6BNMg5j65aaxqcuz93MnGA06BYrhr){:target="_blank"}

![Ejercicio resuelto C++]({{ site.url }}/assets/2019-11-20-ejercicio-cpp-mapas.png)

{% include accesibilidad.html %}
Dado un número romano, convertirlo a su equivalente en números arábigos en base decimal. Equivalencias: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.

Reglas:

Número repetido hasta 3 veces: se suma.
- I delante de V o X significa restar 1.
- X delante de L o C significa restar 10.
- C delante de D o M significa restar 100.
- Precondiciones: el número romano a convertir estará en mayúsculas, será válido y su equivalente estará entre 1 y 3999.

Resolución:

```cpp
int romanoAInt(string romano) {
    map<char, int> equivalencias;
    equivalencias['M'] = 1000;
    equivalencias['D'] = 500;
    equivalencias['C'] = 100;
    equivalencias['L'] = 50;
    equivalencias['X'] = 10;
    equivalencias['V'] = 5;
    equivalencias['I'] = 1;
    int respuesta = 0;
    for (int i = 0; i < romano.length() - 1; ++i)
    {
        if (equivalencias[romano[i]] < equivalencias[romano[i+1]])
            respuesta -= equivalencias[romano[i]];
        else
            respuesta += equivalencias[romano[i]];
    }
    respuesta += equivalencias[romano[romano.length()-1]];
    return respuesta;
}
```
</div></details>

<hr />

💻 [Código ejecutable](https://jdoodle.com/a/3pLH){:target="_blank"}

{% include codeEditor.html id="3pLH?stdin=0&arg=0&rw=1" %}
