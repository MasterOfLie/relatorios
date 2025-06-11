from flask import Flask
from .models import db, Usuario, Tramite, Telefone
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atendimentos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sua_chave_secreta'
    @app.template_filter('minutos_para_hora_minuto')
    def minutos_para_hora_minuto(minutos):
        if minutos is None:
            return "00:00"
        horas = int(minutos // 60)
        minutos_restantes = int(minutos % 60)
        return f"{horas:02}:{minutos_restantes:02}"
    db.init_app(app)

    from .models import Usuario
    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app