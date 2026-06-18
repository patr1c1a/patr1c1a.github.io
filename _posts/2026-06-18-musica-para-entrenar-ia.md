---
layout: post
title: Música para entrenar a la IA
date: 2026-06-18 16:00:00
categories: ia
tags: datasets música suno udio
published: true
---

![Música para entrenar a la IA]({{ site.url }}/assets/2026-06-18-musica-para-entrenar-ia.png){: width="40%" }

Desde 2024 algunas empresas como Warner, Universal y Sony comenzaron a demandar a las creadoras de herramientas de generación musical mediante IA. También algunos artistas independientes se unieron para reclamar por el uso indebido de sus obras.

## El problema

Muchas veces, las obras de estos artistas fueron usadas sin su permiso para entrenar a los modelos de IA que luego serían puestos a disposición del público como parte de herramientas generadoras de música.

Recientemente, la revista estadounidense ["The Atlantic" creó un buscador](https://www.theatlantic.com/category/ai-watchdog/){:target="_blank"} en el que pueden encontrarse los 21 millones de canciones usadas por este tipo de empresas para el entrenamiento de sus productos.

## Cómo The Atlantic llegó a esa información

En [el artículo publicado](https://www.theatlantic.com/technology/2026/06/ai-music-generators-suno-google-udio/687485/){:target="_blank"}, The Atlantic menciona el caso de unos patinadores artísticos que, durante una competencia, usaron una canción generada por IA. La letra se asemejaba demasiado a la de ["You Get What You Give" de New Radicals](https://www.youtube.com/watch?v=DL7-CKirWZE){:target="_blank"} pero el estilo musical era diferente, lo cual develaba que la canción de New Radicals había sido usada en algún dataset de entrenamiento. Particularmente, en el usado por algún modelo de generación musical.

Los escritores de la revista revisaron papers de desarrolladores e información disponible en plataformas de machine learning donde quedaba a la vista que varias empresas habían usado grandes cantidades de datos sobre música perteneciente a numerosos artistas. Dos de estas empresas son [Google](https://arxiv.org/abs/2301.11325){:target="_blank"} y [Stability](https://arxiv.org/html/2407.14358){:target="_blank"}.

## Qué son los datasets de música

En internet hay numerosos "datasets" de temas variados. Es decir, datos recolectados y ordenados, que se publican para un uso que habitualmente es educativo o de investigación. Por ejemplo, cualquier desarrollador podría acceder a [alguno de los datasets que ofrece la plataforma Kaggle](https://www.kaggle.com/datasets){:target="_blank"} para aprender sobre análisis y manipulación de datos.

Entre la gran cantidad de datos disponibles, hay algunos datasets que se enfocan específicamente en música. Algunos no proveen los archivos musicales sino los metadatos: la información que describe a esa música, sus artistas y los álbumes que han lanzado. Otros sí contienen los archivos de sonido y permiten su descarga.

Entre los datasets especializados en música y sonidos se encuentran [Laion-disco-12M](https://laion.ai/blog/laion-disco-12m/){:target="_blank"}, [Free Music Archive](https://freemusicarchive.org/){:target="_blank"} y [Freesound](https://freesound.org/){:target="_blank"}. Sus términos y condiciones ponen límites claros a su uso.

## El uso indebido

Las empresas de IA suelen escudarse en que los datasets son públicos. Pero cuando se trata de usar la información para entrenar un producto comercial, los límites comienzan a desdibujarse.

En algunos casos se sospecha que obtuvieron la música de plataformas como Spotify o Youtube, usando herramientas automatizadas de "scraping" (una técnica para obtener toda la información disponible en una página web), lo cual suele estar prohibido por esas plataformas.

Las demandas de grandes empresas no se hicieron esperar, pero también hay estudios de abogados que están representando a músicos, productores y compositores independientes, como ["Top Music Attorney"](https://www.topmusicattorney.com/indieailawsuit){:target="_blank"} o [Loevy](https://www.loevy.com/class-actions/artificial-intelligence/music-ai-class-action/){:target="_blank"} (que litigan específicamente en Estados Unidos).
