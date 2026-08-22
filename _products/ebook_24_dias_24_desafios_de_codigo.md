---
layout: product
title: "24 días, 24 desafíos de código"
subtitle: "Desde “mi código funciona” hasta la solución profesional"
slug: "ebook-24-dias-24-desafios-de-codigo"
description: "Libro digital con 24 ejercicios de programación explicados y optimizados en detalle. Disponible en 4 ediciones."
image: "/static/img/products/ebook_24_desafios/thumbnail_ebook_24_dias_24_desafios_de_codigo.png"
product_image: "/static/img/products/ebook_24_desafios/portada_multilenguaje.png"
catalog_image: "/static/img/products/ebook_24_desafios/catalogo.png"
catalog_order: 3
type: "Ebook"
status: evergreen
audience: programacion
registration_required: false
catalog_metadata:
  - icon: "book"
    text: "PDF de 290+ páginas"
  - icon: "file"
    text: "Incluye repositorio"
  - icon: "code"
    text: "Ejercicios detallados"

product_details:
  - icon: "book"
    text: "PDF descargable (más de 290 páginas en las ediciones individuales o más de 380 páginas en la edición multilenguaje)."
  - icon: "code"
    text: "Repositorio de código ejecutable con todas las soluciones eficientes."
  - icon: "comment"
    text: "Instrucciones para ejecutar cada desafío."
  - icon: "lock"
    text: "Acceso inmediato y permanente."
  - icon: "tag"
    text: "Marca de agua personalizada (que no cubre el texto del libro)."

topics:
  - programacion
  - ejercicios
  - algoritmos
cta: "Comprar ahora"
published: true
price_display:
  text: "Desde USD 17"

variants_title: "Seleccionar edición"
variants_description: "Todos los desafíos y explicaciones son idénticos. Lo que cambia entre las ediciones es el lenguaje utilizado en las implementaciones finales."
variants:
  - id: python
    title: "Edición Python"
    description: "24 desafíos de programación resueltos con Python."
    image: "/static/img/products/ebook_24_desafios/portada_python.png"

    purchase_options:
      - id: usd
        title: "Dólares estadounidenses"
        price: 17
        currency: USD
        payment_provider: payhip
        payment_data:
          product: "WSi0z"
          variant: "1763755283979"

  - id: java
    title: "Edición Java"
    description: "24 desafíos de programación resueltos con Java."
    image: "/static/img/products/ebook_24_desafios/portada_java.png"

    purchase_options:
      - id: usd
        title: "Dólares estadounidenses"
        price: 17
        currency: USD
        payment_provider: payhip
        payment_data:
          product: "WSi0z"
          variant: "1763762998340"

  - id: csharp
    title: "Edición C#"
    description: "24 desafíos de programación resueltos con C#."
    image: "/static/img/products/ebook_24_desafios/portada_cs.png"

    purchase_options:
      - id: usd
        title: "Dólares estadounidenses"
        price: 17
        currency: USD
        payment_provider: payhip
        payment_data:
          product: "WSi0z"
          variant: "1763763166781"

  - id: multilenguaje
    title: "Edición multilenguaje"
    description: "Los 24 desafíos de programación resueltos con Python, Java y C#."
    image: "/static/img/products/ebook_24_desafios/portada_multilenguaje.png"

    purchase_options:
      - id: usd
        title: "Dólares estadounidenses"
        price: 29.99
        currency: USD
        payment_provider: payhip
        payment_data:
          product: "WSi0z"
          variant: "1763763190695"
---

<section class="product-section product-value">

    <h2>Que el código funcione no hace a un buen programador...</h2>

    <p>
        La IA puede generar código que funciona. Pero un buen desarrollador debe ser capaz de analizarlo, detectar problemas y tomar mejores decisiones.
    </p>

    <p>
        Este libro digital propone 24 desafíos de programación para practicar justamente esas habilidades.
    </p>

    <ul>
        <li>Aprenderás a detectar cuándo un algoritmo que "funciona" es en realidad ineficiente.</li>
        <li>Descubrirás cómo optimizar una solución inicial para convertirla en una más profesional.</li>
        <li>Encontrarás estrategias para reutilizar al enfrentarte a otros problemas.</li>
        <li>Analizarás casos de prueba y eficiencia paso a paso.</li>
    </ul>

</section>

<section class="product-section product-resources">

    <h2>Muestra gratis: para probar antes de comprar</h2>

    <p>
        La muestra gratuita contiene la introducción, el primer capítulo completo y parte del segundo capítulo.
    </p>

    <p>
        También está disponible en Youtube una lista de videos donde analizo los 24 desafíos y explico las ideas detrás de sus soluciones.
    </p>

    <div class="product-resource-links">

        <a
            href="https://forms.gle/Ek6ZjaTX43YaPftc8"
            target="_blank"
            rel="noopener noreferrer"
            class="product-secondary-action"
        >
            Descargar muestra gratuita
        </a>

        <a
            href="https://www.youtube.com/playlist?list=PLb_E6BNMg5j5i5lJocZSidKcGXWeHWkRo"
            target="_blank"
            rel="noopener noreferrer"
            class="product-secondary-action"
        >
            Ver videos de los 24 desafíos
        </a>

    </div>

</section>

<section class="product-section">

    <h2>¿Qué incluye tu compra?</h2>

    <ul class="product-metadata">
        {% for item in page.product_details %}
            <li>
                {% include metadata_item.html
                    icon=item.icon
                    text=item.text
                %}
            </li>
        {% endfor %}
    </ul>

    {% if page.cta %}
        <a href="#comprar" class="product-primary-action">
            {{ page.cta }}
        </a>
    {% endif %}
</section>

<section class="product-section product-faq">

    <h2>Preguntas frecuentes</h2>

    <details>
        <summary>¿Qué nivel necesito?</summary>
        <p>
            Los conocimientos de un curso básico de programación son suficientes:
            bucles, funciones y estructuras básicas como arreglos, conjuntos y diccionarios.
            Mi curso de programación desde cero es un buen punto de partida.
        </p>
    </details>

    <details>
        <summary>¿En qué formato viene?</summary>
        <p>
            PDF descargable y repositorio de código ejecutable.
            Las ediciones individuales tienen más de 270 páginas y la edición multilenguaje,
            más de 380.
        </p>
    </details>

    <details>
        <summary>¿Qué lenguajes incluye?</summary>
        <p>
            Hay cuatro ediciones disponibles: Python, Java, C# y Multilenguaje,
            que incluye los tres lenguajes. Los desafíos y explicaciones son idénticos;
            solo cambian las implementaciones finales.
        </p>
    </details>

    <details>
        <summary>¿Puedo imprimirlo?</summary>
        <p>
            Sí. Una vez comprado, podés imprimirlo para uso personal.
        </p>
    </details>

    <details>
        <summary>¿Por qué creaste este libro?</summary>
        <p>
            Muchas personas saben lo básico de programación pero no saben cómo avanzar.
            En lugar de seguir acumulando lenguajes, frameworks y tecnologías, este libro
            propone trabajar sobre habilidades que siguen siendo útiles aunque cambien
            las herramientas: razonamiento, algoritmos, eficiencia y capacidad para
            evaluar una solución.
        </p>
    </details>

    <details>
        <summary>¿Cuál es la política de devoluciones?</summary>
        <p>
            No se aceptan devoluciones una vez descargado el producto, excepto por un
            defecto técnico grave, como un archivo corrupto o contenido diferente al
            descripto. Si tenés un problema, contactame dentro de las 48 horas posteriores
            a la compra escribiendo a
            programaciondesdecero@patriciaemiguel.com.
        </p>
    </details>

</section>
