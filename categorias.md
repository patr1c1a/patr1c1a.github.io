---
layout: page
title: Categorías
permalink: /categorias/
published: true
---

    <hr />
    {% for category in site.categories %}
        {% capture category_slug %}{{ category | first }}{% endcapture %}
        {% for c_slug in category_slug %}
            {% if c_slug == page.categories %}
                <button class="btn btn-sm btn-primary btn-raised">{{ c_slug }}</button>
            {% else %}
                <a href="{{ site.baseurl }}/category/{{ c_slug }}" class="btn btn-sm btn-default btn-raised">{{ c_slug }}</a>
            {% endif %}
        {% endfor %}
    {% endfor %}
    <hr />
