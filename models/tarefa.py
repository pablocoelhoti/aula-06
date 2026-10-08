class Tarefa:
    def __init__(self, id, descricao, concluida=False):
        self.id = id                  # Identificador único da tarefa
        self.descricao = descricao    # Texto da tarefa
        self.concluida = concluida    # Booleano (True ou False, padrão é False)

    def marcar_como_concluida(self):
        """Muda o status da tarefa para concluída."""
        self.concluida = True

    def atualizar_descricao(self, nova_descricao):
        """Atualiza o texto descritivo da tarefa."""
        self.descricao = nova_descricao