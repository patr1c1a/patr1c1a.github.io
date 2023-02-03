---
layout: post
title: Ejercicio y resolución en 4 lenguajes
date: 2023-02-02 20:00:00 -0300
categories: ejercicios
tags: algoritmos
published: false
---

Un ejercicio que puede parecer complejo pero no lo es tanto. Veamos su resolución en distintos lenguajes.


![Enunciado]({{ site.url }}/assets/2023-02-02-ejercicio-resoluciones-4-lenguajes-01.png)
![Resolución - Algoritmo]({{ site.url }}/assets/2023-02-02-ejercicio-resoluciones-4-lenguajes-02.png)
![Implementación - Python y Javascript]({{ site.url }}/assets/2023-02-02-ejercicio-resoluciones-4-lenguajes-03.png)
![Implementación - Java y C++]({{ site.url }}/assets/2023-02-02-ejercicio-resoluciones-4-lenguajes-04.png)



&nbsp;

{% include accesibilidad.html %}

Ejercicio de programación

Dado un arreglo con cinco enteros positivos, hallar los valores mínimo y máximo que pueden calcularse sumando exactamente cuatro de los cinco números. Retornar un nuevo arreglo donde el primer elemento sea el valor mínimo y el segundo sea el valor máximo.

Ejemplo:

entrada: [3,6,1,5,0]

mínimo: 0+1+3+5

máximo: 1+3+5+6

salida: [9,15]



Resolución (descripción del algoritmo):

Paso 1: Ordenar el arreglo en forma ascendente.
Paso 2: Calcular la mínima suma, sumando los primeros cuatro elementos.
Paso 3: Calcular la máxima suma, sumando los últimos cuatro elementos.
Paso 4: Retornar los resultados en un nuevo arreglo, compuesto por la mínima suma y la máxima suma.

Implementación en Python:

```python
def suma_min_max(arreglo):
    minimo = sorted(arreglo)[0:4]
    maximo = sorted(arreglo)[-4:]
    return [sum(minimo), sum(maximo)]
```

Implementación en Javascript:

```javascript
function suma_min_max(arreglo) {
  let ordenado = Array.from(arreglo)
  ordenado.sort((a, b) => a - b);
  let minimo = ordenado.slice(0, 4).reduce((a, b) => a + b, 0);
  let maximo = ordenado.slice(-4).reduce((a, b) => a + b, 0);
  return [minimo, maximo];
}
```

Implementación en Java:

```java
import java.util.Arrays;

public class SumaMinMax {
    public static int[] suma_min_max(int[] arreglo) {
        int[] ordenado = arreglo.clone();
        Arrays.sort(ordenado);
        int minimo = ordenado[0] + ordenado[1] 
                  + ordenado[2] + ordenado[3];
        int maximo = ordenado[1] + ordenado[2] 
                  + ordenado[3] + ordenado[4];
        return new int[] { minimo, maximo };
    }
}
```

Implementación en C++:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

vector<int> suma_min_max(vector<int> arreglo) {
    sort(arreglo.begin(), arreglo.end());
    int minimo = accumulate(arreglo.begin(), arreglo.begin()+4, 0);
    int maximo = accumulate(arreglo.rbegin(), arreglo.rbegin()+4, 0);
    return {minimo, maximo};
}
```


</div></details>


<br />&nbsp;

### [Código Python para ejecutar](https://jdoodle.com/a/5OBB){:target="_blank"}

{% include codeEditor.html id="5OBB?stdin=0&arg=0&rw=1" %}

<br />&nbsp;


### [Código Javascript para ejecutar](https://jdoodle.com/a/5OBE){:target="_blank"}

{% include codeEditor.html id="5OBE?stdin=0&arg=0&rw=1" %}

<br />&nbsp;


### [Código Java para ejecutar](https://jdoodle.com/a/5OBv){:target="_blank"}

{% include codeEditor.html id="5OBv?stdin=0&arg=0&rw=1" %}

<br />&nbsp;


### [Código C++ para ejecutar](https://jdoodle.com/a/5OBp){:target="_blank"}

{% include codeEditor.html id="5OBp?stdin=0&arg=0&rw=1" %}

<br />&nbsp;




<hr />
