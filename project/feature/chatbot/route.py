from flask import Blueprint, request, render_template, jsonify
from .controller import ChatBotController
from .request_validator import request_validtor

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/QA", methods=["POST"])
@request_validtor.Validate_Qa()
def create_qa(validate_data):
    controller = ChatBotController()
    response = controller.create_qa(validate_data)
    return response, 201

@chatbot_bp.route("/")
def home():
    return render_template('home.html')
