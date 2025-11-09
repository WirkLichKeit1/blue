from flask import Blueprint, jsonify
from Repository.repository import User

user_bp = Blueprint("users", __name__)
repo = User()

@user_bp.route("/users", methods=["GET"])
def getUsers():
    if repo.get_users() is None:
        return jsonify({"error", "Nenhum usuário encontrado"}), 404
    return repo.get_users()
