class HttpNotFoundError(Exception):
    def __init__(self, mensagem: str) -> None:
        super().__init__(mensagem)
        self.mensagem = mensagem
        self.nome = "Sem Funcionamento"
        self.statusCode = 404
