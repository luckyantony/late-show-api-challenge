from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server.app import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint("appearance", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get("rating")
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")

    if not (1 <= rating <= 5):
        return jsonify(error="Rating must be between 1 and 5"), 400

    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)
    if not guest or not episode:
        return jsonify(error="Guest or Episode not found"), 404

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()
    return jsonify(message="Appearance created", id=appearance.id), 201
