---
layout: post
title: Desafío C++ número 7
date: 2021-01-15 12:00:00
categories: desafios c++
tags: arreglos entrevista
published: true
---
Esta consigna es común en entrevistas laborales de algunas empresas importantes, como Facebook o Microsoft. En este caso, el código está casi completo pero falta una pequeña parte. ¿Sabrías decir qué condición es la correcta?

<details><summary>Click aquí para desplegar la solución. 👈</summary>
<br />✅ La respuesta correcta es la d: numeros[i] != 0.
<br />
<br />✏️ Explicación: La variable "i" se utiliza para iterar por el índice del vector "numeros" y la variable "cero" se detiene cada vez que encuentra un 0 en el arreglo. Si el elemento del vector en la posición indicada por i es diferente de 0, debemos intercambiarlo con el último 0 que hemos encontrado, ubicado en la posición que indica la variable "cero".
<br />
<br />▶️ [Ver algoritmo explicado](https://youtu.be/nADemX9stHY?t=862){:target="_blank"}
<br />
<br /><div markdown="1">💻 [Código ejecutable](https://jdoodle.com/a/3pHN){:target="_blank"}

{% include codeEditor.html id="3pHN?stdin=0&arg=0&rw=1" %}
<br /> 
  </div>
<br />
<div markdown="1">![Solución al desafío]({{ site.url }}/assets/2021-01-14-desafio-cpp-7-solucion.png)
  </div></details>

<br />
<br />
**Desafío C++** 👇
<br />
![Desafío C++ número 7]({{ site.url }}/assets/2021-01-14-desafio-cpp-7.png)


{% include accesibilidad.html %}
La función moverCeros recibe un vector con números y debe retornarlo con todos los elementos que sean cero desplazados hacia la derecha. ¿Cuál es la condición correcta a evaluar en el if para lograr lo que pide la consigna?
a. cero==0
b. numeros[cero]!=0
c. i==0
d. numeros[i]!=0

Código:

```cpp
void moverCeros(vector<int>& numeros) {
	for (int i = 0, cero = 0; i < numeros.size(); i++) {
 		if (COMPLETAR EL CÓDIGO FALTANTE AQUÍ) {
			swap(numeros[cero++], numeros[i]);
		}
	}
}
```

</div></details>

