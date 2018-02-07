---
layout: page
title: Categorías
permalink: /categorias/
published: true
---

{% if site.categories.size > 0 %}
                <span class="categories">
                  &raquo; 
                  {% for category in site.categories %}
                    <a href="{{ site.baseurl }}/category/{{ category }}">{{ category }}</a>
                    {% if forloop.last == false %}, {% endif %}
                  {% endfor %}
                </span>
{% endif %}
