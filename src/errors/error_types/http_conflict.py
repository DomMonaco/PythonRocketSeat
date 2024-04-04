class HttpConflictError(Exception):
    def __init__(self, mensagem: str) -> None:
        super().__init__(mensagem)
        self.mensagem = mensagem
        self.nome = "Conflito"
        self.statusCode = 409
