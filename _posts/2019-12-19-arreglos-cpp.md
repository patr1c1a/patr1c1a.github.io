---
layout: post
title: Ejercicio con arreglos en C++
date: 2019-12-19 21:00:00
categories: c++ ejercicios
tags: arreglos
published: true
---


Los arreglos son una de las estructuras de datos más básicas que podemos utilizar para implementar algoritmos y contenedores.

![Ejercicio con arreglos C++]({{ site.url }}/assets/2019-12-19-arreglos-cpp.png)
{% include accesibilidad.html %}
	
Dado un arreglo de enteros y su dimensión lógica (cantidad de elementos), imprimir todos los sub-arreglos de elementos que sumen 0.
Ejemplo: para {2, 4, -5, 3, 1, -3, 2, 7, -2, -7} se deben imprimir los subarreglos:

[1..5]

[1..9]

[4..6]

[6..9]  
  

Resolución:

```cpp
void imprimirSubArreglos(int arreglo[], int n) {
    for (int i = 0; i < n; i++) {
        int suma = 0;
        for (int j = i; j < n; j++) {
            suma += arreglo[j];
            if (suma == 0) {
                cout << "[" << i << ".." << j << "]\n";
            }
        }
    }
}
```
</div></details>

<hr />

💻 [Probar y ejecutar el código](https://jdoodle.com/a/3pLF){:target="_blank"}

{% include codeEditor.html id="3pLF?stdin=0&arg=0&rw=1" %}


