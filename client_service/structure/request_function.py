import requests
import json

from client_service.helpers.enums import StateOfGame


class MessageToServer:

    def check_users(self, login, password, game):
        try:
            d = {'name': login, 'password': password}
            data = requests.post('http://127.0.0.1:5000/input', data=d)
            return_data = json.loads(data.text)
            if return_data['status'] == 200:
                game.data['player_id'] = return_data['player_id']
                return StateOfGame.MENU.name
            else:
                return 'error'
        except requests.exceptions.ConnectionError:
            return 'error_server'

    def connect_to_room(self, name, password, username):
        d = {'name': name, 'password': password, 'username': username}
        data = requests.post('http://127.0.0.1:5000/input_room', data=d)
        return StateOfGame.GAME_ROOM.name if data.status_code == 200 else StateOfGame.INPUT_ROOM.name

    def create_a_room(self, name, password, max_player=15):
        d = {'name': name, 'password': password, 'limited': max_player}
        data = requests.post('http://127.0.0.1:5000/create_room', data=d)
        return StateOfGame.GAME_ROOM.name if data.status_code == 201 else StateOfGame.CREATE_ROOM.name

    def get_list_of_users(self, name):
        data = requests.get(f'http://127.0.0.1:5000/room/{name}/get_users')
        return_data = json.loads(data.text)
        return return_data['User']

    def button_registration(self, login_input, password_input, password_input2):
        if password_input == password_input2:
            d = {'name': login_input, 'password': password_input}
            data = requests.post('http://127.0.0.1:5000/registration', data=d)

            return_data = json.loads(data.text)
            if return_data == {'response': 'create', 'status': 201}:
                return StateOfGame.REGISTRATION.name
            else:
                return 'name_error'
        else:
            return 'password_error'

    def create_character(self, game, character_name):
        d = {'user_id': game.data['player_id'], 'character_name': character_name}
        data = requests.post('http://127.0.0.1:5000/character/create', data=d)

        if data.status_code == 201:
            print('Create')
        else:
            print('Error')


if __name__ == '__main__':
    mesage = MessageToServer()
    mesage.create_character(1, 1, 'Ice mage')
