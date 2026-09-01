import json
import mercadopago
from firebase_functions.params import SecretParam
from pathlib import Path
from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from firebase_admin import initialize_app, firestore


set_global_options(
    region="southamerica-east1",
    max_instances=1,
)

initialize_app()


CATALOG_PATH = Path(__file__).parent / "product_catalog.json"
MERCADOPAGO_ACCESS_TOKEN = SecretParam("MERCADOPAGO_ACCESS_TOKEN")


def load_catalog():
    with CATALOG_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def find_purchase_option(product, purchase_option_id):
    for option in product.get("purchase_options", []):
        if option.get("id") == purchase_option_id:
            return option

    return None


@https_fn.on_request(
    secrets=[MERCADOPAGO_ACCESS_TOKEN]
)
def createRegistration(req: https_fn.Request) -> https_fn.Response:

    if req.method != "POST":
        return https_fn.Response(
            "Method Not Allowed",
            status=405,
        )

    data = req.get_json(silent=True)

    if not data:
        return https_fn.Response(
            "Invalid JSON",
            status=400,
        )

    product_slug = data.get("product_slug")
    purchase_option = data.get("purchase_option")

    if not product_slug or not purchase_option:
        return https_fn.Response(
            "Missing product_slug or purchase_option",
            status=400,
        )

    catalog = load_catalog()

    product = catalog.get(product_slug)

    if not product:
        return https_fn.Response(
            "Product not found",
            status=404,
        )

    if not product.get("published"):
        return https_fn.Response(
            "Product is not available",
            status=400,
        )

    if product.get("status") == "closed":
        return https_fn.Response(
            "Product is closed",
            status=400,
        )

    option = find_purchase_option(
        product,
        purchase_option,
    )

    if not option:
        return https_fn.Response(
            "Purchase option not found",
            status=400,
        )

    if not option.get("price") or not option.get("currency"):
        return https_fn.Response(
            "Invalid purchase option configuration",
            status=500,
        )

    if not option.get("payment_provider"):
        return https_fn.Response(
            "Missing payment provider configuration",
            status=500,
        )

    db = firestore.client()

    registration = {
        "product_slug": product_slug,
        "purchase_option": purchase_option,
        "product_title": product.get("title"),
        "amount": option["price"],
        "currency": option["currency"],
        "payment_provider": option["payment_provider"],
        "status": "pending_payment",
        "created_at": firestore.SERVER_TIMESTAMP,
    }

    document = db.collection("registrations").add(registration)
    registration_id = document[1].id

    if option["payment_provider"] == "mercadopago":

        sdk = mercadopago.SDK(
            MERCADOPAGO_ACCESS_TOKEN.value
        )

        preference_data = {
            "items": [
                {
                    "title": product["title"],
                    "quantity": 1,
                    "unit_price": option["price"],
                    "currency_id": option["currency"],
                }
            ],
            "external_reference": registration_id,
        }

        preference_response = sdk.preference().create(
            preference_data
        )

        if preference_response["status"] not in range(200, 300):
            db.collection("registrations").document(
                registration_id
            ).update({
                "status": "payment_creation_failed",
            })

            return https_fn.Response(
                "Could not create payment",
                status=502,
            )

        preference = preference_response["response"]

        payment_url = preference.get("init_point")
        preference_id = preference.get("id")

        db.collection("registrations").document(
            registration_id
        ).update({
            "preference_id": preference_id,
            "payment_url": payment_url,
        })

        return https_fn.Response(
            json.dumps({
                "registration_id": registration_id,
                "status": "pending_payment",
                "payment_url": payment_url,
            }),
            status=201,
            headers={
                "Content-Type": "application/json"
            },
        )

    return https_fn.Response(
        json.dumps({
            "registration_id": registration_id,
            "status": "pending_payment",
            "payment_provider": option["payment_provider"],
        }),
        status=201,
        headers={
            "Content-Type": "application/json"
        },
    )