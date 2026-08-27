from pathlib import Path
import json
import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
FUNCTIONS_DIR = SCRIPT_DIR.parent
PROJECT_ROOT = FUNCTIONS_DIR.parent

PRODUCTS_DIR = PROJECT_ROOT / "_products"
OUTPUT_FILE = FUNCTIONS_DIR / "product_catalog.json"


def read_front_matter(path):
    text = path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        raise ValueError(f"Missing front matter: {path}")

    parts = text.split("---", 2)

    if len(parts) < 3:
        raise ValueError(f"Invalid front matter: {path}")

    return yaml.safe_load(parts[1]) or {}


def main():
    catalog = {}

    for path in sorted(PRODUCTS_DIR.glob("*.md")):
        front_matter = read_front_matter(path)

        slug = front_matter.get("slug")

        if not slug:
            raise ValueError(f"Missing slug: {path}")

        if slug in catalog:
            raise ValueError(f"Duplicate slug: {slug}")

        catalog[slug] = {
            "slug": slug,
            "title": front_matter.get("title"),
            "status": front_matter.get("status"),
            "published": front_matter.get("published", False),
            "purchase_options": front_matter.get("purchase_options", []),
            "variants": front_matter.get("variants", []),
        }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Exported {len(catalog)} products to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()