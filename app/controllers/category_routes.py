from flask import Blueprint
from .category_controller import (
    get_all_categories,
    get_category_by_id,
    get_category_with_products,
    create_category,
    manage_category
)

category_bp = Blueprint("category", __name__, url_prefix="/categories")

category_bp.route("", methods=["GET"])(get_all_categories)
category_bp.route("/<int:category_id>", methods=["GET"])(get_category_by_id)
category_bp.route("/<int:category_id>/products", methods=["GET"])(get_category_with_products)
category_bp.route("", methods=["POST"])(create_category)
category_bp.route("/<int:category_id>", methods=["PUT", "DELETE"])(manage_category)
