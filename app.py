#!/usr/bin/python3

from flask import Flask, jsonify

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
        'github_file_url': 
