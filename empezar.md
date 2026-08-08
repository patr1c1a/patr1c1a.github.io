---
layout: landing
title: Empezar
hero_title: ¿Qué te interesa aprender?
hero_text: Te ayudo a encontrar el recorrido que mejor se adapta a tus objetivos.
permalink: /empezar/
published: true
---

<section class="learning-path-selector">

{% include learning_path_card.html
title="Programación"
description="Construir una base sólida para desenvolverte en el mundo del desarrollo de software."
button_text="Comenzar recorrido"
url="#programacion"
%}

{% include learning_path_card.html
title="Inteligencia Artificial"
description="Aprender a aprovechar la IA para trabajar mejor, crear más y resolver tareas."
button_text="Comenzar recorrido"
url="#ia"
%}

</section>

<section id="programacion">

<h2>Guía para empezar en Desarrollo de Software</h2>

{% include table_of_contents.html
items=site.data.start_landing.programming.toc
%}

<p>(Contenido pendiente)</p>

</section>

<section id="ia">

<h2>Guía para empezar con Inteligencia Artificial</h2>

{% include table_of_contents.html
items=site.data.start_landing.ai.toc
%}

<p>(Contenido pendiente)</p>

</section>