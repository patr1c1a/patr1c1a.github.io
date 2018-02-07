---
layout: page
title: Categorías
permalink: /categorias/
published: true
---

<div>
{% for category in site.categories %}
  <div>
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <div id="#{{ category_name | slugize }}"></div>
    <p></p>
    
    <h3 class="category-head">{{ category_name }}</h3>
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories[category_name] %}
    <article class="archive-item">
      <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>


<div>
TAGS:
        {% for tag in site.tags %}
        "{{ tag | first }}"{% unless forloop.last %},{% endunless %}
        {% endfor %}
</div>
