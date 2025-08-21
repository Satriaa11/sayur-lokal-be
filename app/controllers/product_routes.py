from flask import Blueprint
from .product_controller import (
    create_product,
    get_all_products_item,
    get_product,
    get_products_by_category,
    get_products_by_seller,
    get_products_by_price_range,
    search_products,
    manage_product
)

product_bp = Blueprint("product", __name__, url_prefix="/products")

product_bp.route("", methods=["POST"])(create_product)
product_bp.route("", methods=["GET"])(get_all_products_item)
product_bp.route("/<int:product_id>", methods=["GET"])(get_product)
product_bp.route("/category/<int:category_id>", methods=["GET"])(get_products_by_category)
product_bp.route("/seller/<int:seller_id>", methods=["GET"])(get_products_by_seller)
product_bp.route("/price-range", methods=["GET"])(get_products_by_price_range)
product_bp.route("/search", methods=["GET"])(search_products)
product_bp.route("/<int:product_id>", methods=["PUT", "DELETE"])(manage_product)
