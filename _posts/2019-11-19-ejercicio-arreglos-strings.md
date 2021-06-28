---
layout: post
title: Ejercicio resuelto, con strings y arreglos
date: 2019-11-19 21:00:00
categories: python java ejercicios
tags: arreglos strings
published: true
---

Veamos un problema con strings + una posible solución. ¿Se te ocurre algún algoritmo diferente? 🧠 (pista: los hay).

Fuente: [leetcode.com](https://leetcode.com/){:target="_blank"}

![Enunciado]({{ site.url }}/assets/2019-11-19-ejercicio-arreglos-strings-01.png)

{% include accesibilidad.html %}
Dada una cadena S y un carácter C, retornar un arreglo de enteros representando la distancia más corta desde cada carácter en la cadena hasta una ocurrencia del carácter C.


Ejemplo 1:

Entrada: "algoritmo", 'o'

Salida: [3, 2, 1, 0, 1, 2, 2, 1, 0]


Ejemplo 2:

Entrada: "abcdefga", 'a'

Salida: [0, 1, 2, 3, 3, 2, 1, 0]


Precondiciones:

La longitud de S está en [1, 1000].

C es un único carácter.

C se encuentra en S.

Todas las letras en S y C son minúsculas.
</div></details>



![Algoritmo]({{ site.url }}/assets/2019-11-19-ejercicio-arreglos-strings-02.png)
{% include accesibilidad.html %}
Solución intuitiva:

Por cada índice S[i], se intenta encontrar la distancia al siguiente carácter C yendo hacia la iziquierda y yendo hacia la derecha. La respuesta será el menor de esos dos valores.


Algoritmo:

Yendo de izquierda a derecha, guardar el índice prev del último carácter C encontrado. Así, la respuesta será i - prev.

Yendo de derecha a izquierda, guardar el índice prev del último carácter C encontrado. Así, la respuesta será prev - i.

Tomar el menor de estos dos valores para obtener el resultado final.


Complejidad:

De tiempo: O(N), donde N es la longitud de S. Se pasa dos veces por toda la cadena.

De espacio: O(N), el tamaño de la respuesta.
</div></details>

![Código]({{ site.url }}/assets/2019-11-19-ejercicio-arreglos-strings-03.png)

{% include accesibilidad.html %}

Solución en Python:


Solución en Java:

```java
public int[] distanciaMasCorta(String S, char C) {
	int N = S.length();
	int[] ans = new int[N];
	int prev = -(S.length()+1);

	for (int i = 0; i < N; ++i) {
		if (S.charAt(i) == C)
			prev = i;
		ans[i] = i - prev;
	}

	prev = S.length()+1;
	for (int i = N-1; i >= 0; --i) {
		if (S.charAt(i) == C)
			prev = i;
		ans[i] = Math.min(ans[i], prev - i);
	}

	return ans;
}
```

</div></details>

<hr />

💻 [Versión Python ejecutable](https://jdoodle.com/a/3pND){:target="_blank"}

{% include codeEditor.html id="3pND?stdin=0&arg=0&rw=1" %}
<br />



💻 [Versión Java ejecutable](https://jdoodle.com/a/3pNC){:target="_blank"}

{% include codeEditor.html id="3pNC?stdin=0&arg=0&rw=1" %}


