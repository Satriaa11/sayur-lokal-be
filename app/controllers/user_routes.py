from flask import Blueprint
from .user_controller import (
    get_current_user,
    update_buyer_profile,
    update_seller_profile,
    update_profile_picture,
    update_password
)

user_bp = Blueprint("user", __name__, url_prefix="/users")

user_bp.route("/profile", methods=["GET"])(get_current_user)
user_bp.route("/profile/buyer", methods=["PUT"])(update_buyer_profile)
user_bp.route("/profile/seller", methods=["PUT"])(update_seller_profile)
user_bp.route("/profile/picture", methods=["PUT"])(update_profile_picture)
user_bp.route("/password", methods=["PUT"])(update_password)
