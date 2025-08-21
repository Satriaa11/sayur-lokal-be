from flask import Blueprint
from .rating_controller import (
    create_rating_endpoint,
    update_rating_endpoint,
    delete_rating_endpoint,
    get_product_ratings,
    get_user_ratings,
    get_rating_detail
)

rating_bp = Blueprint('rating', __name__, url_prefix='/ratings')

rating_bp.route('', methods=['POST'])(create_rating_endpoint)
rating_bp.route('/<int:rating_id>', methods=['PUT', 'PATCH'])(update_rating_endpoint)
rating_bp.route('/<int:rating_id>', methods=['DELETE'])(delete_rating_endpoint)
rating_bp.route('/product/<int:product_id>', methods=['GET'])(get_product_ratings)
rating_bp.route('/user', methods=['GET'])(get_user_ratings)
rating_bp.route('/<int:rating_id>', methods=['GET'])(get_rating_detail)
