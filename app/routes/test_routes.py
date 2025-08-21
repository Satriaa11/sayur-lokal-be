from flask import Blueprint, jsonify, request

test_bp = Blueprint("test", __name__, url_prefix="/api/test")

@test_bp.route("/cors", methods=["GET", "POST", "OPTIONS"])
def test_cors():
    """Test endpoint for CORS functionality"""
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'status': 'OK'})
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        return response

    return jsonify({
        "success": True,
        "message": "CORS is working correctly!",
        "method": request.method,
        "origin": request.headers.get('Origin'),
        "user_agent": request.headers.get('User-Agent'),
        "headers": {
            "Content-Type": request.headers.get('Content-Type'),
            "Authorization": "***" if request.headers.get('Authorization') else None,
            "Origin": request.headers.get('Origin')
        }
    })

@test_bp.route("/health", methods=["GET", "OPTIONS"])
def health_check():
    """Simple health check with CORS"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'OK'})
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    return jsonify({
        "status": "healthy",
        "cors_enabled": True,
        "message": "Backend is running with CORS support"
    })

@test_bp.route("/auth-test", methods=["GET", "POST", "OPTIONS"])
def auth_test():
    """Test authenticated request with CORS"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'OK'})
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response

    auth_header = request.headers.get('Authorization')

    return jsonify({
        "success": True,
        "message": "Auth test endpoint",
        "has_auth": bool(auth_header),
        "method": request.method,
        "cors_working": True
    })
