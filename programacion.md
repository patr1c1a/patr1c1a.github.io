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

    <div class="section-header">
        <h2>Curso gratuito de programación</h2>
    </div>

    <p>
        Los fundamentos de programación son la base de todo. Por eso te dejo mi curso gratuito de programación desde cero usando Python. Los conceptos que cubre son aplicables a la mayoría de lenguajes modernos, por eso el curso no se centra en Python sino en que aprendas las bases.
    </p>

    <a class="button-primary" href="https://www.youtube.com/playlist?list=PLb_E6BNMg5j7-MJ0ctjvKQlv2PU7qbMDb">
        Ver curso en Youtube
    </a>

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
