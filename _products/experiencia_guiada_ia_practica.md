---
layout: product
title: "Experiencia guiada de IA"
subtitle: "Grupo de práctica por WhatsApp, a tu ritmo"
slug: "experiencia-guiada-ia-practica"
description: "Experiencia grupal para practicar el uso de inteligencia artificial mediante actividades guiadas y acompañamiento."
image: "/static/img/products/experiencia_guiada_ia_practica/thumbnail_experiencia_guiada_ia_practica.png"
catalog_order: 2
type: "Experiencia guiada"
status: scheduled
audience: ia
registration_required: true
registration_fields:
  - name
  - email
  - whatsapp
catalog_metadata:
  - icon: "whatsapp"
    text: "Grupo de práctica"
  - icon: "calendar"
    text: "Comienza el 7 de septiembre"
  - icon: "clock"
    text: "4 semanas"

product_details:
  - icon: "whatsapp"
    text: "Grupo de práctica por WhatsApp."
  - icon: "calendar"
    text: "Inicio: 7 de septiembre de 2026."
  - icon: "clock"
    text: "Duración: 4 semanas."
  - icon: "target"
    text: "No se necesitan conocimientos previos de inteligencia artificial."

topics:
  - ia
  - inteligencia-artificial
  - productividad

cta: "Inscribirme"
published: true

start_date: "2026-09-07"
length: "4 semanas"

price_display:
  text: "ARS 15.000 / USD 10"

purchase_title: "¿Cómo inscribirse?"
purchase_description: "Ingresa tus datos en el formulario y completa el pago con el medio que prefieras."

purchase_options:
  - id: ars
    title: "Pesos argentinos"
    price: 15000
    currency: ARS
    payment_provider: mercadopago
    payment_data: {}

  - id: usd
    title: "Dólares estadounidenses"
    price: 10
    currency: USD
    payment_provider: paypal
    payment_data: {}
---

<section class="product-section product-value">

    <h2>¿Cómo funciona?</h2>

    <p>
        Durante 4 semanas practicaremos distintos usos de inteligencia artificial
        mediante un grupo de WhatsApp.
    </p>

    <p>
        Una vez por semana voy a proponer una actividad para probar una herramienta
        o una forma diferente de utilizar la IA. Cada integrante podrá realizarla
        a su propio ritmo.
    </p>

    <p>
        Después, quienes quieran podrán compartir con el resto del grupo qué hicieron
        y cuál fue el resultado.
    </p>

    <p>
        Conocer cómo otras personas utilizan estas herramientas es una excelente
        manera de descubrir nuevas posibilidades y aprender de la experiencia. Y yo voy a estar guiando el proceso durante todo el recorrido.
    </p>

</section>

<section class="product-section">

    <h2>¿Qué esperar de esta experiencia?</h2>

    <ul>
        <li>Una propuesta práctica diferente cada semana.</li>
        <li>La posibilidad de experimentar con IA a tu propio ritmo.</li>
        <li>Ideas y ejemplos aportados por otras personas del grupo.</li>
        <li>Acompañamiento durante las 4 semanas.</li>
        <li>Un espacio para probar, equivocarte y descubrir nuevas formas de utilizar la IA.</li>
    </ul>

</section>

<section class="product-section">

    <h2>Detalles de esta propuesta</h2>
      
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

</section>
