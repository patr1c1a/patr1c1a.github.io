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

        {% assign published_products = site.products | where: "published", true | sort: "catalog_order" %}

        {% for product in published_products %}

            {% assign card_image = product.catalog_image | default: product.image %}

            {% include premium_resource_card.html
                title=product.title
                subtitle=product.subtitle
                type=product.type
                description=product.description
                metadata=product.catalog_metadata
                image=card_image
                price=product.price_display.text
                url=product.url
            %}
        {% endfor %}

    </div>

</section>
