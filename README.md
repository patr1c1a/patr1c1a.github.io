# Sitio web

## Tecnologías

- Jekyll con Ruby.
- Host en plan gratuito de Cloudflare Pages
- Firebase Cloud Functions para generar links de pago
- APIs de mercadopago y paypal
- Firebase Firestore como base de datos (para inscripciones y operaciones de pago).
- Lazyforms para formularios

## Arquitectura general

- default.html: documento HTML.
- head_redesign.html: metadatos comunes del nuevo sitio.
- home.html: estructura de la Home.
- landing.html: estructura común de las landings.
- product.html: estructura común de los productos.
- _layouts/ contiene esqueletos de páginas completas.
- _includes/ contiene fragmentos reutilizables que un layout puede ensamblar.
- Las páginas (home.md, empezar.md, programacion.md, etc.) solamente proporcionan contenido.
- _products es una collection de Jekyll.
- _includes/icon.html: responsable de renderizar cualquier ícono del sitio.
- functions: carpeta correspondiente a Firebase.
- Los productos de la tienda, internamente son "productos" (product, products, related_products, product.html, etc.) pero de cara al usuario son "recursos premium" cuando hablamos de esos productos en la interfaz.

## Header

Contiene la foto y nombre, además del menú.

Fuente: `_data/navigation.yml`

## Home

**¿Qué querés hacer hoy?**: contiene 4 cards. Las primeras 3 conducen a las landing pages "empezar", "programación", "IA" y la cuarta es el buscador.

**Empezar**: Intenta orientar. Su objetivo es resolver el problema: "No sé por dónde empezar". 

**Programación**: Contiene posts del blog seleccionados, link al curso gratuito en youtube y a la herramienta de práctica de programación, productos de la tienda orientados a programación.

**IA**: Contiene posts del blog seleccionados, playlist de videos en youtube, link a la herramienta de IA, productos de la tienda orientados a IA.

**Lo nuevo**: productos nuevos de la tienda. Las fuentes son `_data/home_highlighted_products.yml` y colección `_products`.

**¿No sabés por dónde empezar?**: Dirige a la misma página que "Empezar".

**Recursos destacados**: del blog. La fuente es `_data/home_featured_posts.yml`

**Recursos premium**: productos destacados de la tienda. La fuente es `_data/home_featured_products.yml`

**Herramientas gratuitas**: La fuente es `_data/tools.yml`

**Newsletter**: usa emailoctopus. Solo para avisos de novedades de la tienda.

## Tienda

Fuente: `_products/`

Cada producto es un Markdown.

Los productos tienen una audiencia: "programacion" o "ia". Permite filtrar para mostrar en la landing page correspondiente.

La colección _products genera sus URLs públicas bajo /recursos/:name/.

Cada documento de _products/ debe declarar explícitamente layout: product.

El nombre del archivo de cada producto debe coincidir con su slug.

La URL pública de cada producto seguirá la estructura `/recursos/<slug>/`. Para lograr que el campo slug del front matter sea la fuente de verdad de la URL, en config.yml la colección _products tiene configurado `permalink: /recursos/:name/` lo cual termina produciendo: `/recursos/<nombre del archivo>/` (como slug es igual a nombre del archivo, se logra que coincidan).

En la tienda, cada producto tiene su imagen de catálogo, que no necesariamente es la misma que la imagen promocional que existe principalmente para representar el recurso en contextos como Home/Landings. Si no existe, se hace fallback a la imagen promocional. Entonces, cada producto puede tener:

- image → representación general del recurso, necesaria para otros componentes (home, landings, etc.). Relación de aspecto 3:2.
- catalog_image → imagen específicamente compuesta para la tarjeta de /tienda/. Relación de aspecto 3:2.
- product_image → imagen principal de la página individual del producto.
- variants[].image → imagen específica de cada variante, para la página del producto.

El orden de las cards en la tienda se define mediante el campo "catalog_order" en el front matter de cada producto (cada archivo .md dentro de "_products").

En el front matter, "status: closed" hará que el producto se siga mostrando pero sin botón de compra. Aparece un formulario para avisar cuándo está nuevamente disponible.

En un producto habrá product_variants o product_purchase pero no ambas.

purchase_options maneja opciones de compra de una variante de un producto que tiene variantes. El proveedor (payhip, mercadopago, paypal, udemy, etc.) determina posteriormente cómo se genera el mecanismo concreto de compra.

### Páginas de productos

Cada producto de la tienda tendrá una página dedicada donde se mostrará toda la información y la forma de adquirirlo.

Cada producto tiene sus particularidades y formas de adquirirlo.

Solo algunos productos (talleres, experiencias guiadas, clases online, etc.), en las opciones de compra tendrán un formulario de inscripción para capturar los datos del comprador y unir eso con el link de pago (generado por MercadoPago o Paypal).

Los productos que son de compra directa no requieren ningún dato del comprador (más que completar la transacción y pago).

En el front matter, purchase options representa cómo puede adquirirse un producto (Mercado Pago, PayPal, transferencia, etc.)

Un producto puede tener variantes. Las variantes no son productos independientes.

El precio puede pertenecer a una variante. En el front matter, variants contiene las opciones de compra de un producto con variantes o ediciones.

El proveedor/método de adquisición puede pertenecer a una variante.

Para pagos con mercadopago o paypal se generará un link específico para esa transacción, lo cual permitirá relacionar los datos del formulario con los del pago. Para este backend se usará Firebase Cloud Functions.

## Functions

El código de Cloud Functions se encuentra en: `functions/`

Entorno virtual local: `functions/venv/`.

Para instalar localmente las dependencias:

```bash
cd functions
venv\Scripts\activate
python -m pip install -r requirements.txt
```

Para desplegar las Functions (desde la raíz del proyecto): `firebase deploy --only functions`

Para consultar los logs: `firebase functions:log`

## Listado de productos

Los productos se definen exclusivamente mediante el front matter de `_products/*.md`. Pero las Cloud Functions no leen directamente los archivos *.md.

El script `functions/scripts/export_product_catalog.py` lee esos archivos y genera automáticamente `functions/product_catalog.json`.

El archivo se genera usando el siguiente comando (desde la raíz): `functions\venv\Scripts\python functions\scripts\export_product_catalog.py`.

`functions/product_catalog.json` no debe editarse manualmente. Contiene el listado de productos con los datos necesarios por la Cloud Function para validar las opciones de compra: slug, opción, precio, moneda y proveedor.

## Deployment

Las Functions utilizan Cloud Functions 2nd generation.

Firebase utiliza Artifact Registry para almacenar las imágenes de los deployments. Se configuró una política de limpieza para evitar la acumulación indefinida de imágenes antiguas.

Las imágenes antiguas se conservan durante 1 día.

Cada vez que se modifique el front matter de un producto que afecte al checkout se debe regenerar el catálogo antes de desplegar Functions (`functions\venv\Scripts\python functions\scripts\export_product_catalog.py`) y deploy Functions (`firebase deploy --only functions`).

## Levantar localmente el sitio

1. Regenerar el catálogo de productos: `functions\venv\Scripts\python functions\scripts\export_product_catalog.py`

2. Deploy Functions: `firebase deploy --only functions`

3. Levantar Jekykll: `bundle exec jekyll serve --livereload --force_polling`