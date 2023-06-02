from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Conexao:
    def __init__(self, app):
        self.app = app
        
    def conectar(self):
        parametros = self._ler_parametros_conexao()
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = parametros['DATABASE_URI']
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)
    
    def obter_sessao(self):
        return db.session
    
    def _ler_parametros_conexao(self):
        parametros = {}
        
        with open('config.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas:
                chave, valor = linha.strip().split('=')
                parametros[chave] = valor
    
        return parametros