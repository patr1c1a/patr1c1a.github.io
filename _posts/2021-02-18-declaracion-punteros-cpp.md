---
layout: post
title: Declaración y definición de punteros en C++
date: 2021-02-18 12:00:00
categories: c++
tags: punteros stack heap
published: true
---

Declarar un puntero en C++ puede parecer una tarea trivial, pero hay detalles importantes a tener en cuenta.

![Declaración y definición de punteros en C++]({{ site.url }}/assets/2021-02-18-declaracion-punteros-cpp.png)

<br />&nbsp;

💻 [Código con ejemplos](https://jdoodle.com/a/3pCy){:target="_blank"}

{% include codeEditor.html id="3pCy?stdin=0&arg=0&rw=1" %}

<br />&nbsp;
<hr />
### Versión accesible (apta para lectores electrónicos):
Declaración y definición de punteros "crudos" en C++

Un puntero es una variable que contiene una dirección de memoria

Un puntero declarado sin un valor inicial tiene contenido indefinido.

```cpp
string saludo;
string * ptr;
```

La primera es una variable string. La segunda es un puntero a string.

nullptr indica que no tiene valor:

```cpp
ptr = nullptr;
```

Un puntero puede apuntar a una posición de memoria stack o heap.

```cpp
ptr = &saludo;
ptr = new string();
```

El primero apunta a stack. El segundo apunta a heap.

En una declaración múltiple, el * se asocia al identificador, no al tipo:

```cpp
int* x, y;
```

x es puntero a int. y es int.
