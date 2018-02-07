---
layout: page
title: Categorías
permalink: /categorias/
published: true
---

{% for category in site.categories %}
    <li><a href="{{ site.baseurl }}/category/{{ category }}"><strong>{{category|first}}</strong></a></li>
{% endfor %}
