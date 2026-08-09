---
layout: landing
title: Programación
description: Aprender programación desde cero.
hero_title: Programación
hero_text: Recursos y herramientas para construir una base sólida y seguir avanzando.
permalink: /programacion/
published: true
---

<section class="landing-section programming-course">

    {% include free_course_card.html
        url="https://www.youtube.com/playlist?list=PLb_E6BNMg5j7-MJ0ctjvKQlv2PU7qbMDb"
    %}

</section>

<section class="landing-section programming-posts">

    {% include section_header.html
        title="Posts recomendados"
        url="/blog/"
    %}

    <div class="cards-grid">
        {% for post in site.data.programming_landing.posts %}

            {% include featured_resource_card.html
                title=post.title
                url=post.url
                image=post.image
            %}

        {% endfor %}
    </div>

</section>

<section class="landing-section programming-practice">

    {% include section_header.html
        title="Practicar ejercicios con Python"
    %}

    {% for tool in site.data.tools.items %}
        {% if tool.title == "Plataforma de práctica" %}
            {% include tool_card.html
                title=tool.title
                description=tool.description
                button=tool.button
                url=tool.url
                image=tool.image
            %}
        {% endif %}
    {% endfor %}

</section>

{% include landing/related_products.html
    audience="programacion"
%}
