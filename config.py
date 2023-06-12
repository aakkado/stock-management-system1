import json

class Config:
    
    with open("config.json") as file:
        data = json.load(file)
    
    SQLALCHEMY_DATABASE_URI = data['db_key']
    
config = Config    
print(config.SQLALCHEMY_DATABASE_URI)    