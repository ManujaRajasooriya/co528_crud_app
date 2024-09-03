from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'Sahan', 'email': 'sahan@gmail.com'},
    {'id': 2, 'name': 'Ruwan', 'email': 'ruwan@yahoo.com'},
    {'id': 3, 'name': 'Gayan', 'email': 'gayan@gmail.com'}
]

# get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    return jsonify(user) if user else ('User is not found', 404)

# create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

# update a user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        user.update(request.json)
        return jsonify(user)
    return ('User is not found', 404)

# delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
