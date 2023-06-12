import bcrypt

class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = self._criptografar_senha(senha)

    def _criptografar_senha(self, senha):
        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return senha_hash.decode('utf-8')

    def verificar_senha(self, senha):
        senha_hash = self.senha.encode('utf-8')
        return bcrypt.checkpw(senha.encode('utf-8'), senha_hash)
