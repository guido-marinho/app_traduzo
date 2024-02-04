from flask import Blueprint, jsonify
from models.history_model import HistoryModel

bp = Blueprint("history_controller", __name__)


@bp.get("/")
def list_history():
    return jsonify(HistoryModel.list_as_json())
