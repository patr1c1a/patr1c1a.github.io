---
layout: page
title: Categorías
permalink: /categorias/
published: true
---

<div>
<h2> CATEGORÍAS:</h2>
{% for category in site.categories %}
  <div>
    {% capture category_name %}{{ category | first }}{% endcapture %}
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

---

<div>
<h2> TAGS:</h2>
        {% for tag in site.tags %}
            {% capture tag_name %}{{ tag | first }}{% endcapture %}
            <a name="{{ tag_name}}">{{ tag_name}}</a>
            "{{ tag | first }}"{% unless forloop.last %},{% endunless %}
        {% endfor %}
</div>
