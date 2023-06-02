class Usuario:
    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email
        
    def verificar_login(self, email_usuario, senha_usuario):
        return self.email == email_usuario and self.senha == senha_usuario
    
    def obter_informacoes(self):
        return f"Nome: {self.nome}, Email: {self.email}"