from flask import Blueprint
from .order_controller import (
    create_order,
    get_order,
    get_buyer_orders,
    get_seller_orders,
    update_order_status,
    cancel_order,
    # upload_payment_proof, # Uncomment if needed
)

order_bp = Blueprint("order", __name__, url_prefix="/orders")

order_bp.route("", methods=["POST"])(create_order)
order_bp.route("/<int:order_id>", methods=["GET"])(get_order)
order_bp.route("/buyer", methods=["GET"])(get_buyer_orders)
order_bp.route("/seller", methods=["GET"])(get_seller_orders)
order_bp.route("/<int:order_id>/status", methods=["PUT"])(update_order_status)
order_bp.route("/<int:order_id>/cancel", methods=["POST"])(cancel_order)
# order_bp.route("/<int:order_id>/payment-proof", methods=["POST"])(upload_payment_proof) # Uncomment if needed
