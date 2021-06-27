---
layout: post
title: Ejercicio de entrevista - Hallar el primer carácter no repetido en un string
date: 2021-03-19 12:00:00
categories: ejercicios java
tags: strings
published: true
---


Este ejercicio suele aparecer en entrevistas laborales de Amazon y de algunas otras empresas. Acá vemos algunas opciones de resolución, con Java. ¿Se te ocurre alguna otra?

💻 [Código ejecutable](https://jdoodle.com/a/3pNh){:target="_blank"}

▶️ [Si te interesa ver más ejercicios de entrevistas laborales y su resolución paso a paso, visita este video](https://www.youtube.com/watch?v=nADemX9stHY){:target="_blank"}


![Opción 1: fuerza bruta]({{ site.url }}/assets/2021-03-19-ejercicio-primer-caracter-unico-01.png)

{% include accesibilidad.html %}
Dado un string compuesto solo por letras minúsculas, hallar el primer carácter que no se repite. Si no existe, retornar "_".

Cuatro posibles soluciones en Java.

Opción 1: por "fuerza bruta". Complejidad algorítmica: O(N<sup>2</sup>)

```java
static char primerCaracterNoRepetido_fuerzaBruta(String cadena) {
	for (int i = 0; i < cadena.length(); i++) {
		boolean repetido = false;
		for (int j = 0; j < cadena.length(); j++) {
			if (cadena.charAt(i) == cadena.charAt(j) && (i != j)) {
				repetido = true;
			}
		}
		if (!repetido)
			return cadena.charAt(i);
	}
	return '_';
}
```
</div></details>
<br />&nbsp;

![Opción 2: métodos predefinidos]({{ site.url }}/assets/2021-03-19-ejercicio-primer-caracter-unico-02.png)

{% include accesibilidad.html %}

Opción 2: con métodos predefinidos. Complejidad algorítmica: O(N<sup>2</sup>)

```java
static char primerCaracterNoRepetido_metodosPredefinidos(String cadena) {
	for (int i = 0; i < cadena.length(); i++) {
		if (cadena.indexOf(cadena.charAt(i)) == cadena.lastIndexOf(cadena.charAt(i))) {
			return cadena.charAt(i);
		}
	}
	return '_';
}
```

</div></details>
<br />&nbsp;

![Opción 3: hashmap]({{ site.url }}/assets/2021-03-19-ejercicio-primer-caracter-unico-03.png)

{% include accesibilidad.html %}

Opción 3: con hashmap. Complejidad algorítmica: O(N)

```java
static char primerCaracterNoRepetido_hashMap(String cadena) {
	HashMap<Character, Integer> ocurrencias = new HashMap();
	for (int i = 0; i < cadena.length(); i++) {
		char c = cadena.charAt(i);
		if (ocurrencias.containsKey(c)) {
			ocurrencias.put(c, ocurrencias.get(c) + 1);
		} else {
			ocurrencias.put(c, 1);
		}
	}

	for (int i = 0; i < cadena.length(); i++) {
		char c = cadena.charAt(i);
		if (ocurrencias.get(c) == 1)
			return c;
	}
	return '_';
}
```

</div></details>
<br />&nbsp;

![Opción 4: arreglo asociado]({{ site.url }}/assets/2021-03-19-ejercicio-primer-caracter-unico-04.png)

{% include accesibilidad.html %}

Opción 4: con un arreglo asociado. Complejidad algorítmica: O(N)

```java
static char primerCaracterNoRepetido_arregloAsociado(String cadena) {
	int[] ocurrencias = new int[26];
	for (char c : cadena.toCharArray()) {
		ocurrencias[c - 'a']++;
	}
	for (char c : cadena.toCharArray()) {
		if (ocurrencias[c - 'a'] == 1)
			return c;
	}
	return '_';
}
```

</div></details>
<hr />

{% include codeEditor.html id="3pNh?stdin=0&arg=0&rw=1" %}

