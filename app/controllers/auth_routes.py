from flask import Blueprint
from .auth_controller import (
    register_buyer_route,
    register_seller_route,
    login_route,
    resend_verification_route,
    logout_route,
    refresh_token_route,
    delete_account_route
)

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

auth_bp.route("/register/buyer", methods=["POST"])(register_buyer_route)
auth_bp.route("/register/seller", methods=["POST"])(register_seller_route)
auth_bp.route("/login", methods=["POST"])(login_route)
auth_bp.route("/resend-verification", methods=["POST"])(resend_verification_route)
auth_bp.route("/logout", methods=["POST"])(logout_route)
auth_bp.route("/refresh-token", methods=["POST"])(refresh_token_route)
auth_bp.route("/delete-account", methods=["DELETE"])(delete_account_route)
