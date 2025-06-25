from flask import Blueprint, jsonify, request
from server.models.episode import Episode
from server.models.appearance import Appearance
from flask_jwt_extended import jwt_required
from server.app import db

episode_bp = Blueprint("episode", __name__)

@episode_bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {"id": e.id, "date": e.date, "number": e.number}
        for e in episodes
    ])

@episode_bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify(error="Episode not found"), 404
    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [
            {
                "id": a.id,
                "rating": a.rating,
                "guest_name": a.guest.name
            } for a in episode.appearances
        ]
    })

@episode_bp.route("/episodes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify(error="Episode not found"), 404
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message="Episode deleted")
