from .request_validator import request_validator
from .controller import AuthController
from .blueprint import auth_bp
from project.decorator.user_agent import user_agent_requeired

@auth_bp.route("/auth",methods=["POST"])
@request_validator.validate_auth()
@user_agent_requeired("masejli")
def auth(validate_data):
    controller=AuthController()
    response=controller.auth(validate_data)
    return response,201