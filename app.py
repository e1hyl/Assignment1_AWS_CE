from flask import Flask, jsonify
import requests
import boto3
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>UniEvent - University Event Management System</h1><a href='/events'>View Events</a>"

@app.route('/events')
def events():
    api_key = os.environ.get('TICKETMASTER_API_KEY')
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&city=London&size=10"
    try:
        r = requests.get(url, timeout=5)
        data = r.json()
        events = data.get('_embedded', {}).get('events', [])
        result = [{"title": e['name'], "date": e['dates']['start']['localDate'], "venue": e['_embedded']['venues'][0]['name']} for e in events]
        return jsonify({"university_events": result})
    except Exception as ex:
        return jsonify({"error": str(ex)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
