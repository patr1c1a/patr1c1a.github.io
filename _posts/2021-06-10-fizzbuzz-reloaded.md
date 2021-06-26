---
layout: post
title: Ejercicio con C++ - "Fizz buzz recargado"
date: 2021-06-10 12:00:00
categories: c++
tags: c++ entrevista
published: true
---

En algunas entrevistas laborales suele aparecer la prueba "fizz buzz": un ejercicio simple para evaluar si dominamos las bases de la programación ([la consigna puede verse en esta publicación](https://cafecito.app/programaciondesde0/post/la-prueba-fizz-buzz-en-entrevistas-laborales-4LY78HxCV){:target="_blank"}.

Esta es una versión un poco más compleja 🤓.

[Código para ejecutar](https://jdoodle.com/a/3pAW){:target="_blank"}

{% include codeEditor.html id="3pAW?stdin=0&arg=0&rw=1" %}

<br />


![Fizz Buzz recargado]({{ site.url }}/assets/2021-06-10-fizzbuzz-reloaded.png)


{% include accesibilidad.html %}

Dado un entero n (mayor que 1), retornar un arreglo de strings -indizado desde 1- donde:

arreglo[i] == "FizzBuzz" si i es divisible por 3 y por 5.

arreglo[i] == "Fizz" si i es divisible por 3.

arreglo[i] == "Buzz" si i es divisible por 5.

arreglo[i] == i si ninguna de las condiciones anteriores es verdadera.

Resolución:

```cpp
vector<string> fizzBuzz(int n) {
    vector<string> arreglo;
    for (int i = 1; i <= n; ++i) {
        string s = "";
        if ((i % 3 != 0) and (i % 5 != 0))
            s += to_string(i);
        else
            if (i % 3 == 0)
                s += "Fizz";
            if (i % 5 == 0)
                s += "Buzz";
        arreglo.push_back(s);
    }
    return arreglo;
}
```

Explicación:

`for (int i = 1; i <= n; ++i)`: Nos piden que el índice comience en 1 (aunque el arreglo se llenará desde el principio, en la posición 0).

`s += to_string(i)`: El número i debe convertirse a string porque el arreglo es de strings.

`arreglo.push_back(s)`: Usamos el método para insertar en un vector (a continuación del último elemento o en la posición 0 si aún no hay elementos).</pre>

</div></details>
<hr />
