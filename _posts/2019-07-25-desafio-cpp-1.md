---
layout: post
title: Desafío C++ número 1
date: 2019-07-25 21:00:00
categories: desafios c++
tags: arreglos
published: true
---

¿Podrás detectar el error en este programa C++? 🔎

▶️ [Este video sobre arreglos en C++ puede ayudarte a resolver el problema](https://www.youtube.com/watch?v=1UycYfCSil8){:target="_blank"}

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✏️ El error está en la carga del arreglo, ya que la dimensión lógica nunca se incrementa al ir agregando elementos, entonces cada valor ingresado se guarda en la posición 0, pisando al anterior.
<br />
<br />Algunos detalles más:
<br />🔹 ¿Hay un bucle infinito? No. El bucle while corta si se ingresa valor==0 y for nunca se ejecuta porque i==0 y dimension==0.
<br />🔹 ¿Podría hacerse con do-while en vez de while? Eso cambiaría el algoritmo. Tal como está, se ejecuta 0 o más veces. Con do-while (a menos que haya un break anticipado) se ejecutaría 1 o más veces.
<br />🔹 ¿Qué se almacena en el arreglo? Con la versión errónea, solo se almacena el último valor leido (a menos que sea el 0), y siempre se lo guarda en la primera posición del arreglo con la instrucción numeros[dimension]=valor
<br />🔹 Los elementos son indefinidos cuando se declara el arreglo, pero eso no causará errores si se maneja apropiadamente la dimensión lógica. El tamaño físico del arreglo es 10, pero podría haber menos elementos "útiles" (tamaño lógico) ocupados.
<br />
<div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pI5){:target="_blank"}
  
{% include codeEditor.html id="3pI5?stdin=1&arg=0&rw=1" %}
  </div>
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2019-07-25-desafio-cpp-1-solucion.png)
  </div></details>

<br />
<br />
**Desafío C++** 👇
![Desafío C++ número 1]({{ site.url }}/assets/2019-07-25-desafio-cpp-1.png)

{% include accesibilidad.html %}

Detectar el error en este programa C++. Este programa debe permitir almacenar hasta 10 números en un arreglo, para después imprimirlo. ¿Qué error tiene? 

```cpp
#include <iostream>
using namespace std;
int main() {
    float numeros[10]; //arreglo con espacio para 10 elementos
    int dimension = 0; //tamaño lógico del arreglo
    float valor;
    
    //Cargar en el arreglo los números ingresados por el usuario
    cout << "Valor a almacenar (finalizar con '0'): ";
    cin >> valor;
    while (valor != 0 && dimension < 10) {
        numeros[dimension] = valor;
        cout << "Valor a almacenar (finalizar con '0'): ";
        cin >> valor;
    }

    //Imprimir el arreglo
    for (int i = 0; i < dimension; ++i) {
        cout << numeros[i] << endl;
    }
}
```

</div></details>
