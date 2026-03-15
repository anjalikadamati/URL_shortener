from flask import Blueprint, request, jsonify, redirect
from app.services.url_service import create_short_url, get_original_url

url_bp = Blueprint("url", __name__)


@url_bp.route("/shorten", methods=["POST"])
def shorten_url():

    data = request.get_json()
    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    short_code = create_short_url(original_url)

    short_url = f"http://localhost:5000/{short_code}"

    return jsonify({"short_url": short_url}), 201


@url_bp.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):

    original_url = get_original_url(short_code)

    if original_url:
        return redirect(original_url)

    return jsonify({"error": "URL not found"}), 404