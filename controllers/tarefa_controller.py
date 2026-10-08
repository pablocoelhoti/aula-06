from models.tarefa import Tarefa

class TarefaController:
    def __init__(self):
        self.tarefas = []       # Lista em memória para armazenar os objetos Tarefa
        self.proximo_id = 1     # Contador para gerar IDs automáticos

    def adicionar_tarefa(self, descricao):
        """Cria uma nova tarefa e adiciona à lista."""
        nova_tarefa = Tarefa(id=self.proximo_id, descricao=descricao)
        self.tarefas.append(nova_tarefa)
        self.proximo_id += 1

    def listar_tarefas(self):
        """Retorna todas as tarefas cadastradas."""
        return self.tarefas

    def buscar_por_id(self, id):
        """Método auxiliar para encontrar uma tarefa pelo ID."""
        for tarefa in self.tarefas:
            if tarefa.id == id:
                return tarefa
        return None

    def remover_tarefa(self, id):
        """Remove uma tarefa da lista com base no ID."""
        tarefa = self.buscar_por_id(id)
        if tarefa:
            self.tarefas.remove(tarefa)

    def concluir_tarefa(self, id):
        """Marca uma tarefa específica como concluída."""
        tarefa = self.buscar_por_id(id)
        if tarefa:
            tarefa.marcar_como_concluida()