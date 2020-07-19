import sys
from os import path
from flask import Flask, jsonify
from flask import request

app_home = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
sys.path.append(app_home)

from db import query, context

app = Flask(__name__)
schema = {
    "tokyo": 1,
    "osaka": 2,
    "nagoya": 3,
    "fukuoka": 4
}


@app.route('/hourly')
def hourly_climates():
    try:
        city = request.args['city']
        range_h = int(request.args.get('range', 12))
        if not 0 < range_h <= 12:
            return jsonify({"BadRequest": "Invalid Parameter"}), 400
        city_id = schema[city]
    except KeyError:
        return jsonify({"BadRequest": "Invalid Parameter"}), 400

    try:
        with context.db_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            data = query.get_hourly_climate(cursor, city_id, range_h)
    except Exception:
        return jsonify({"InternalServerError": "Internal Server Error occurred"}), 500

    return jsonify({"status": "ok", "data": data}), 200


@app.route('/daily')
def daily_climates():
    try:
        city = request.args['city']
        range_d = int(request.args.get('range', 7))
        if not 0 < range_d <= 7:
            return jsonify({"BadRequest": "Invalid Parameter"}), 400
        city_id = schema[city]
    except KeyError:
        return jsonify({"BadRequest": "Invalid Parameter"}), 400

    try:
        with context.db_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            data = query.get_daily_climate(cursor, city_id, range_d)
    except Exception:
        return jsonify({"InternalServerError": "Internal Server Error occurred"}), 500

    return jsonify({"status": "ok", "data": data}), 200


@app.route('/health')
def health():
    return 'Health Check OK!!'
