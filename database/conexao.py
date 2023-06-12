from flask_sqlalchemy import SQLAlchemy

class Conexao:
    def __init__(self, app):
        self.app = app
        self.db = SQLAlchemy(app)
        
    def conectar(self):
        parametros = self._ler_parametros_conexao()
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = parametros['DATABASE_URI']
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db.init_app(self.app)
    
    def obter_sessao(self):
        return self.db.session
    
    def _ler_parametros_conexao(self):
        parametros = {}
        
        with open('config.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas:
                chave, valor = linha.strip().split('=')
                parametros[chave] = valor
    
        return parametros
    
    def fechar_conexao(self):
        self.db.session.remove()
        self.db.engine.dispose()