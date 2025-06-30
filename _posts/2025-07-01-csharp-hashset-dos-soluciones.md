---
layout: post
title: Dos soluciones en C# para detectar duplicados
date: 2025-06-01 12:00:00 -0300
categories: csharp
tags: algoritmos hashset duplicados
published: true
---

A veces buscamos escribir código más compacto porque a simple vista parece "más elegante", pero no siempre el algoritmo más breve es el más eficiente.

Como programadores, es clave entender cómo funciona cada enfoque antes de elegir. Al elegir un algoritmo o implementación, considerá:

Complejidad algorítmica (Big O).
- Tiempo: ¿cuántas veces recorrerá la estructura de datos?
- Espacio: ¿cuánta memoria extra necesita?

Caso promedio y peor caso.
- ¿Puede detenerse antes si encuentra la respuesta rápido?
- ¿Siempre procesa toda la entrada?

Legibilidad y mantenibilidad.
- ¿El código es fácil de entender y mantener para otros programadores?

💻 [Código ejecutable](https://paiza.io/projects/HQCKSl4qkAk97lpzMnGi-g){:target="_blank"}



![Dos soluciones para detectar duplicados]({{ site.url }}/assets/2025-07-01-csharp-hashset-dos-soluciones.png)


{% include codeEditor_paiza.html id="HQCKSl4qkAk97lpzMnGi-g" %} 


&nbsp;

{% include accesibilidad.html %}
Dos soluciones en C# para detectar duplicados.

Dado un array de enteros, devolver true si algún valor se repite, o false en caso contrario.

Solución "clásica":

```csharp
public static bool ContieneDuplicados_clasica(int[] nums)
{
    HashSet<int> visto = new HashSet<int>();
    foreach (int n in nums)
    {
        if (visto.Contains(n))
            return true;
        visto.Add(n);
    }
    return false;
}
```

Esta opción evita recorrer todo el array si encuentra un duplicado temprano (mejor rendimiento en el caso promedio).

Solución "compacta":

```csharp

public static bool ContieneDuplicados_compacta(int[] nums)
{
    return new HashSet<int>(nums).Count < nums.Length;
}
```

Esta opción siempre recorre todo el array y crea un HashSet completo (peor en memoria si el array es grande y tiene duplicados al inicio).

Ambas soluciones recorren el array completo en el peor caso, por lo tanto su complejidad algorítmica es O(n).

- La solución clásica agrega cada elemento y chequea si ya estaba antes.
- La solución compacta crea directamente un HashSet con todos los elementos y compara su tamaño con el array original.

</div></details>
<br />&nbsp;
<hr />
