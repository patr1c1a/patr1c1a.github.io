---
layout: post
title: Buenas prácticas para nuestros condicionales
date: 2019-09-22 21:00:00
categories: otros conceptos
tags: buenas_practicas condicionales
published: true
---

👉 Que compile no significa que haga lo que se pide. Pero que compile y que haga lo que se necesita, tampoco significa que la implementación sea correcta.

Estos son algunos ejemplos para mejorar nuestros condicionales.

Porque las buenas prácticas distinguen a los buenos desarrolladores.

![Condicionales]({{ site.url }}/assets/2019-09-22-buenas-practicas-condicionales.png)

{% include accesibilidad.html %}

"if" redundantes: cómo simplificar tu código

Caso 1:

```java
if (cliente != null)
    return cliente;
else
    return null;
```

El if es redundante. Con return cliente, si cliente es un objeto, se devolverá ese objeto, y si cliente es null se devolverá null.

Caso 2:

```java
if (existe(articulo) == true)
    return true;
else
    return false;
```

Basta con retornar existe(articulo), ya que esta función retorna el valor true o false buscado.

Caso 3:

```java
if (edad < 18)
    precio -= precio*0.1;
    pasajeros++;
else
    pasajeros++;
```

No toda la estructura es innecesaria, pero puede reescribirse como:

```java
if (edad < 18)
    precio -= precio*0.1;
pasajeros++;
```

Caso 4:

```java
if (tipoAnimal == "perro")
    animal.Ladrar();
else if (tipoAnimal == "gato")
    animal.Maullar();
```

Si el comportamiento depende del tipo del objeto, puede haber un problema de diseño. En ese caso sería mejor usar polimorfismo para que cada clase implemente su propio comportamiento:

```java
Animal animal;
animal.emitirSonido();
```

</div></details>
