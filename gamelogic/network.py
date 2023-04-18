import requests

from gamelogic.network_error import *


class Network:
    URL = 'http://25.45.70.241:8000'
    session = requests.Session()
    access_token = None
    refresh_token = None

    def update_tokens(self, callback, **args):
        try:
            self.session.headers.update(
                {'Authorization': f'Bearer {self.refresh_token}'})
            response = self.session.get(f'{self.URL}/refresh')

            response = response.json()
            self.access_token = response.get('access_token')
            self.refresh_token = response.get('refresh_token')

            self.session.headers.update(
                {'Authorization': f'Bearer {self.access_token}'})

            return callback(**args)
        except WrongCodeError:
            print('ERROR refresh token')

    def register(self, email, password):

        body = {
            "email": email,
            "password": password
        }
        response = self.session.post(
            url=f'{self.URL}/register', json=body)
        if response.status_code == 409:
            raise RegistrationError(email)
        elif response.status_code == 503:
            raise DbUnavailableError
        elif response.status_code == 422:
            raise NotEmailError(email)

        self.login(email, password)

    def login(self, email: str, password: str):
        data = {
            'username': email,
            'password': password
        }
        response = self.session.post(url=f'{self.URL}/login', data=data)
        if response.status_code == requests.codes.not_found:
            raise AuthError

        if response.status_code == 404:
            raise AuthError
        if response.status_code == 422:
            raise WrongEnterError
        response = response.json()
        self.access_token = response.get('access_token')
        self.refresh_token = response.get('refresh_token')
        self.session.headers.update(
            {'Authorization': f'Bearer {self.access_token}'})

    def confirm_account(self, code):
        data = {
            'code': code
        }
        try:
            response = self.session.post(
                url=f'{self.URL}/confirm', params=data)
            if response.status_code == 406:
                raise WrongCodeError
            elif response.status_code == 401:
                raise TokenError
            elif response.status_code == 426:
                raise NeedRefreshToken
        except NeedRefreshToken:
            self.update_tokens(self.confirm_account, code=code)

    def forgot_password(self, email):
        body = {
            'email': email
        }
        response = self.session.post(
            url=f'{self.URL}/codereset', json=body)
        if response.status_code == 404:
            raise NotEmailError

    def reset_password(self, email, password, code):
        body = {
            'email': email,
            'password': password,
            'code': code
        }
        response = self.session.post(url=f'{self.URL}/reset', json=body)
        if response.status_code == 404:
            raise NotEmailError
        elif response.status_code == 406:
            raise WrongCodeError
        self.access_token = None
        self.refresh_token = None

    def get_game_save(self, game_id):
        data = {
            'game_id': game_id
        }
        try:
            response = self.session.post(url=f'{self.URL}/reset', data=data)

            if response.status_code == 426:
                raise NeedRefreshToken

            response = response.json()
            army = response.get('army')
            resources = response.get('resources')
            houses = response.get('houses')

            return army, resources, houses

        except NeedRefreshToken:
            return self.update_tokens(self.get_game_save, game_id=game_id)

    def update_game_save(self, game_id, army, resources, houses):
        body = {
            'army': army,
            'resources': resources,
            'houses': houses
        }
        try:
            response = self.session.put(
                url=f'{self.URL}/game/{game_id}', json=body)
            if response.status_code == 426:
                raise NeedRefreshToken
        except NeedRefreshToken:
            self.update_tokens(self.update_game_save, game_id=game_id,
                               army=army, resources=resources, houses=houses)

    def get_all_game_info(self):
        try:
            response = self.session.get(url=f'{self.URL}/game')
            if response.status_code == 426:
                raise NeedRefreshToken
            return response.json()
        except NeedRefreshToken:
            return self.update_tokens(self.get_all_game_info)
