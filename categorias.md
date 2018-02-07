---
layout: page
title: Categorías
permalink: /categorias/
published: true
---

{% for category in site.categories %}
    <li><a href="{{category.url}}"><strong>{{category|first}}</strong></a></li>
{% endfor %}
