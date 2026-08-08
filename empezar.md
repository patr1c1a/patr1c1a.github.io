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

{% include landing/learning_guides/programming.html %}

</section>

<section id="ia">

{% include landing/learning_guides/ai.html %}

</section>