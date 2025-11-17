from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)

@app.route('/api/posts', methods=['POST'])
def add_post():

    # Getting form data
    data = request.get_json()

    # Validation all fields are mandatory
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "Missing title or content"}), 400

    # Creating a new ID
    if POSTS:
        max_id = max(post['id'] for post in POSTS)
        new_id = max_id + 1
    else:
        new_id = 1

    # Creating a new post dict
    new_post = {
        'id': new_id,
        'title': data['title'],
        'content': data['content']
    }

    # Add the new post to the POST list
    POSTS.append(new_post)

    return jsonify(new_post), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
