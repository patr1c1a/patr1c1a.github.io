from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from firebase_admin import initialize_app, firestore


set_global_options(
    region="southamerica-east1",
    max_instances=1,
)

initialize_app()


@https_fn.on_request()
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

    db = firestore.client()

    registration = {
        "product_slug": product_slug,
        "purchase_option": purchase_option,
        "status": "pending_payment",
        "created_at": firestore.SERVER_TIMESTAMP,
    }

    document = db.collection("registrations").add(registration)

    return https_fn.Response(
        f"Registration created: {document[1].id}",
        status=201,
    )