# nao execute falsk run
from flask import Flask, jsonify
from flask_cors import CORS

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + os.sep + 'src')

import backend

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/show-videos")
def get_videos():
  list_videos, status = backend.get_all_videos()
  msg, http_status =  ('success', 200) if status else ('failed', 401)
  return jsonify(
    { 'status': msg, 'list_videos': list_videos}), http_status

# Update Database, Cost long time
@app.route('/update-db')
def update_database():
  result, status, time_cost = backend.update_db()
  msg, http_status =  ('success', 201) if status else ('failed', 401)
  return jsonify(
    { 'status': msg, 'count': result, 'time_cost': time_cost}), http_status

# app name
@app.errorhandler(404)
def not_found(e):
  return jsonify({'status': 'failed', 'message': 'URL Not Found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')