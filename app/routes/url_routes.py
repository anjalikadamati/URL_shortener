from flask import Blueprint, request, jsonify, redirect
from app.services.url_service import create_short_url, get_original_url
from app.utils.rate_limiter import check_rate_limit

url_bp = Blueprint("url", __name__)

@url_bp.route("/shorten", methods=["POST"])
def shorten_url():

    if not check_rate_limit():
        return jsonify({"error": "Too many requests"}), 429

    data = request.get_json()
    original_url = data.get("url")
    expires_in = data.get("expires_in")

    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    short_code = create_short_url(original_url, expires_in)

    return jsonify({
        "short_url": f"http://localhost:5000/{short_code}"
    })


@url_bp.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):

    if not check_rate_limit():
        return jsonify({"error": "Too many requests"}), 429

    original_url = get_original_url(short_code)

    if original_url:
        return redirect(original_url)

    return jsonify({"error": "URL not found"}), 404
