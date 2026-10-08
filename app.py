from flask import Flask
from routes.tarefa_routes import tarefa_bp

app = Flask(__name__)

# Registra o Blueprint das rotas na aplicação principal
app.register_blueprint(tarefa_bp)

if __name__ == '__main__':
    # Roda o servidor ecd "Tarefa POO"m modo de desenvolvimento local
    app.run(debug=True)