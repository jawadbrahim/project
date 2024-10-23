from .controller import UserController
from .request_validator import request_validator
from .blueprint import user_bp


@user_bp.route("/user",methods=["POST"])
@request_validator.validate_create_user()
def create_user(validate_data):
    controller=UserController()
    response=controller.create_user(validate_data)
    return response,201