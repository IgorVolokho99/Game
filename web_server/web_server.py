from flask import Flask, request, jsonify

from room import rooms
from user_dao import UserDAO
from web_server.db.models import engine

app = Flask(__name__)
user_dao = UserDAO(engine)


@app.route('/registration', methods=['POST'])
def registration():
    username = request.form['name']
    password = request.form['password']

    if user_dao.is_exist(username):
        return jsonify({'response': 'Aleready exist', 'status': 409})
    else:
        user_dao.add_user(username, password)
        player_id = user_dao.get_id(username)
        return jsonify({'response': 'create', 'status': 201, 'player_id': player_id})


@app.route('/input', methods=['POST'])
def input():
    username = request.form['name']
    password = request.form['password']
    if user_dao.validate_user(username, password):
        player_id = user_dao.get_id(username)
        return jsonify({'response': 'Allowed', 'status': 200, 'player_id': player_id})
    else:
        return jsonify({'response': 'Not Allowed', 'status': 401})


@app.route('/create_room', methods=['POST'])
def create_room():
    name_room = request.form['name']
    password = request.form['password']
    active = request.form['active']
    creater_id = request.form['creater_id']
    type = request.form['type']
    # r = Room(name_room, password, active, creater_id, type)
    # rooms.append(r)
    user_dao.add_room(name_room, password, active, creater_id, type)
    return jsonify({'response': 'create', 'status': 201}), 201


@app.route('/input_room', methods=['POST'])
def input_room():
    name = request.form['name']
    password = request.form['password']
    for room in rooms:
        if room.name == name:
            return jsonify({'response': 'input', 'status': 200}) if room.pasword == password else jsonify(
                {'response': 'stop', 'status': 412})
    return jsonify({'response': 'stop', 'status': 401})


@app.route('/room/<string:name>/get_users', methods=['GET'])
def get_users(name: str):
    for room in rooms:
        if name == room.name:
            return jsonify({'Response': 'Success', 'User': room.get_names()}), 200
    return jsonify({'Response': 'Not found'}), 404


@app.route('/room/<string:name>/start_game', methods=['GET'])
def start_game(name: str):
    for room in rooms:
        if name == room.name:
            room.start()
            return jsonify({'Response': 'Success'}), 200
    return jsonify({'Response': 'Not found'}), 404


@app.route('/character/create', methods=['POST'])
def create_character():
    user_id = request.form['user_id']
    character_name = request.form['character_name']

    try:
        user_dao.add_character(user_id, character_name)
        return jsonify({'response': 'create'}), 201
    except Exception as e:
        return jsonify({'response': str(e)}), 404


app.run()
