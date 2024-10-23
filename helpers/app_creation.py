from flask import Flask

from project.config.development import Development
def create_app(db):
  app=Flask(__name__,template_folder="C:/Python/chatbot/templates")
  
  app.config.from_object(Development)

  db.init_app(app)
  with app.app_context():
   from project.feature.chatbot.route import chatbot_bp
   from project.feature.auth.route import auth_bp
   from project.feature.user.route import user_bp
   app.register_blueprint(chatbot_bp)
   app.register_blueprint(auth_bp)
   app.register_blueprint(user_bp)
   print(app.url_map)

  return app