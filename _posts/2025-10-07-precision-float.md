---
layout: post
title: ¿Por qué 0.1 + 0.2 no da 0.3?
date: 2025-10-07 15:00:00 -0300
categories: conceptos
tags: float double precision punto_flotante ieee754
published: true
---

Este es un problema que ocurre en prácticamente todos los lenguajes modernos. Para evitarlo, debemos usar tipos decimales especiales (decimal, BigDecimal, Decimal de Python) o librerías de aritmética de precisión arbitraria.

No existe un lenguaje moderno popular que use decimales exactos como tipo numérico por defecto.

![Por qué 0.1 + 0.2 no da 0.3]({{ site.url }}/assets/2025-10-07-precision-float.png)


&nbsp;

{% include accesibilidad.html %}

¿Por qué 0.1 + 0.2 no da 0.3?

Los números decimales que usamos (base 10) no siempre pueden representarse exactamente en binario (base 2), que es como la computadora guarda los números.

Por ejemplo, 0.1 en decimal es una fracción infinita en binario, igual que 1/3 es infinito en decimal (0.333…).

Ejemplos:

```javascript
console.log(0.1 + 0.2);
```

```python
print(0.1 + 0.2)
```

```ruby
puts 0.1 + 0.2
```

El resultado, en todos ellos, es 0.30000000000000004.

¿Por qué pasa esto?

0.1 y 0.2 no se pueden representar de forma exacta en binario.
La computadora guarda un valor muy cercano, pero no exacto, y al sumarlos ese error de precisión se nota.

Sucede en todos los lenguajes que usan el estándar IEEE 754 de punto flotante (casi todos los lenguajes modernos). Para evitarlo, muchos lenguajes tienen tipos decimales especiales (como BigDecimal en Java).

</div></details>
<br />&nbsp;
<hr />
