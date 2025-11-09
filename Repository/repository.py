import json

class User:
    def get_users(self):
        users = "usuarios.json"
        with open(users, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return dados
