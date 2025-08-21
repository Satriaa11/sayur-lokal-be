from flask_cors import CORS
from flask import request, jsonify
from functools import wraps

def init_cors(app):
    """Initialize CORS with environment-specific configuration"""
    
    origins = app.config.get('CORS_ORIGINS', ["*"])
    
    # Enhanced CORS configuration
    CORS(app,
         origins=origins,
         methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
         allow_headers=[
             "Content-Type",
             "Authorization",
             "Access-Control-Allow-Credentials", 
             "X-Requested-With",
             "Accept",
             "Origin",
             "Cache-Control",
             "X-Requested-With"
         ],
         supports_credentials=True,
         max_age=3600,
         expose_headers=["Content-Range", "X-Content-Range"]
    )
    
    return app

def add_cors_headers(response):
    """Manually add CORS headers if needed"""
    origin = request.headers.get('Origin')
    
    # List of allowed origins
    allowed_origins = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8080",
        "https://your-frontend-domain.com"
    ]
    
    if origin in allowed_origins or origin is None:
        response.headers['Access-Control-Allow-Origin'] = origin or '*'
    
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With, Accept, Origin'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Max-Age'] = '3600'
    
    return response

def cors_enabled(f):
    """Decorator to add CORS headers to specific routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Handle preflight OPTIONS request
        if request.method == 'OPTIONS':
            response = jsonify({'status': 'OK'})
            return add_cors_headers(response)
        
        # Handle actual request
        response = f(*args, **kwargs)
        
        # Add CORS headers to response
        if hasattr(response, 'headers'):
            return add_cors_headers(response)
        else:
            # If response is not a Response object, create one
            resp = jsonify(response) if not isinstance(response, tuple) else response
            return add_cors_headers(resp)
    
    return decorated_function

def handle_preflight():
    """Handle preflight OPTIONS requests"""
    response = jsonify({'status': 'OK'})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
    response.headers['Access-Control-Max-Age'] = '3600'
    return response
