from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection configuration
client = MongoClient('mongodb+srv://hamzaabid264:Uq5w81UyJIaoQLwH@testcluster.21vwurv.mongodb.net/')  # Update the URL as per your MongoDB configuration
db = client.sample_weatherdata
collection = db.data

@app.route('/get_weather_data', methods=['GET'])
def get_weather_data():
    # Query to retrieve the top 10 documents from MongoDB
    data = list(collection.find().limit(10))
    
    if data:
        # Remove the "_id" field if you don't need it in the response for each document
        for document in data:
            document.pop('_id', None)
        return jsonify(data), 200
    else:
        return "Data not tesrtt", 404
    
    
if __name__ == '__main__':
    app.run(debug=True)
