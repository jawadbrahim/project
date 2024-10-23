from functools import wraps
from flask import request,jsonify



def user_agent_requeired(expected_user_agent):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            user_agent=request.headers.get('user_agent',"")
            if expected_user_agent not in user_agent:
                return jsonify({"error": "Unauthorized: Invalid User-Agent"}), 403
            return func(*args,**kwargs)
        return wrapper
    return decorator

    