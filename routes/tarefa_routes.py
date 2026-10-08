from flask import Blueprint, render_template, request, redirect, url_for
from controllers.tarefa_controller import TarefaController

# Criação do Blueprint para as rotas de tarefas
tarefa_bp = Blueprint('tarefa_bp', __name__)

# Instância global do controller para gerenciar os dados durante a execução
controller = TarefaController()

@tarefa_bp.route('/')
def index():
    """Rota principal: lista todas as tarefas na página HTML."""
    tarefas = controller.listar_tarefas()
    return render_template('index.html', tarefas=tarefas)

@tarefa_bp.route('/adicionar', methods=['POST'])
def adicionar():
    """Rota para processar o formulário de cadastro de nova tarefa."""
    descricao = request.form.get('descricao')
    if descricao:
        controller.adicionar_tarefa(descricao)
    return redirect(url_for('tarefa_bp.index'))

@tarefa_bp.route('/concluir/<int:id>', methods=['POST', 'GET'])
def concluir(id):
    """Rota para marcar uma tarefa como concluída."""
    controller.concluir_tarefa(id)
    return redirect(url_for('tarefa_bp.index'))

@tarefa_bp.route('/remover/<int:id>', methods=['POST', 'GET'])
def remover(id):
    """Rota para remover uma tarefa da lista."""
    controller.remover_tarefa(id)
    return redirect(url_for('tarefa_bp.index'))