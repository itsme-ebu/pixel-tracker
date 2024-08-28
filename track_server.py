import os
from flask import Flask, request, send_file
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Load MongoDB URI from environment variable
mongo_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client['email_tracking']
collection = db['email_opens']

@app.route('/track/<email>')
def track_email_open(email):
    # Log the email open event to MongoDB
    collection.insert_one({
        'email': email,
        'timestamp': datetime.utcnow()
    })
    
    # Return a 1x1 pixel image
    return send_file('pixel.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
