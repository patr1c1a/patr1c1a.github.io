---
layout: landing
title: Recursos premium
hero_title: Recursos premium
hero_text: Cursos, talleres, libros y experiencias para seguir aprendiendo y desarrollar tus habilidades.
permalink: /tienda/
published: true
---

<section class="catalog-section">

    <div class="catalog-grid">

        {% assign published_products = site.products | where: "published", true %}

        {% for product in published_products %}

            {% include premium_resource_card.html
                title=product.title
                subtitle=product.subtitle
                type=product.type
                description=product.description
                image=product.catalog_image
                fallback_image=product.image
                price=product.price_display.text
                url=product.url
            %}
        {% endfor %}

    </div>

</section>
