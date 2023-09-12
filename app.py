#!/usr/bin/python3

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/user_info', methods=['GET'])
def user_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track are required'})

    current_time = datetime.utcnow()
    day_of_week = current_time.strftime('%A')

    user_info = {
        'slack_name': slack_name,
        'current_day': day_of_week,
        'utc_time': current_time,
        'track': track,
        'github_file_url': 'https://github.com/ShogoMark/Zuri_intern/blob/main/app.py',
        'github_repo_url': 'https://github.com/ShogoMark/Zuri_intern',
        'status_code': 200
    }

    return jsonify(user_info)

if __name__ == '__main__':
    app.run(debug=True)
