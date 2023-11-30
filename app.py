from flask import Flask, jsonify, request

app = Flask(__name__)

# Your tweet data (replace this with your actual data or import it)
tweet_data = [
    {"id": 1, "text": "This is tweet 1"},
    {"id": 2, "text": "Another tweet here"},
    # Add more tweet data as needed
]

# Define a GET endpoint to return the JSON data of a specific tweet
@app.route('/tweet/<int:tweet_id>', methods=['GET'])
def get_specific_tweet(tweet_id):
    try:
        specific_tweet = next((tweet for tweet in tweet_data if tweet['id'] == tweet_id), None)

        if specific_tweet:
            return jsonify(specific_tweet)
        else:
            return jsonify({"error": "Tweet not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask app if this script is the main module
if __name__ == '__main__':
    app.run(debug=True)
    
# Curl requests to test the endpoints

# Test retrieving a specific tweet with ID 1
# curl http://localhost:5000/tweet/1

# Test retrieving a specific tweet with ID 3 (nonexistent)
# curl http://localhost:5000/tweet/3

# Test a malformed request (invalid tweet ID)
# curl http://localhost:5000/tweet/invalid

# Test the base URL
# curl http://localhost:5000/
