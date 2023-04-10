import requests

from gamelogic.network_error import *


class Network:
    URL = 'http://25.45.70.241:8000'
    session = requests.Session()
    access_token = None
    refresh_token = None

    def register(self, email, password):
        try:
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
        except (RegistrationError, DbUnavailableError, NotEmailError) as e:
            return e.__str__()
        except Exception:
            return 'Oh my God! Server is down!'

    def login(self, email: str, password: str):
        try:
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

        except (AuthError, WrongEnterError) as e:
            return e.__str__()
        except Exception:
            return 'Oh my God! Server is down!'

    def refresh_tokens(self):
        try:
            self.session.headers.update(
                {'Authorization': f'Bearer {self.refresh_token}'})
            response = self.session.get(f'{self.URL}/refresh')

            response = response.json()
            self.access_token = response.get('access_token')
            self.refresh_token = response.get('refresh_token')

            self.session.headers.update(
                {'Authorization': f'Bearer {self.access_token}'})
        except WrongCodeError:
            print('ERROR refresh token')

    def confirm_account(self, code):
        try:
            data = {
                'code': code
            }
            response = self.session.post(url=f'{self.URL}/confirm', params=data)
            if response.status_code == 406:
                raise WrongCodeError
            if response.status_code == 401:
                raise TokenError

        except (WrongCodeError, TokenError) as e:
            return e.__str__()
        except Exception:
            return 'Oh my God! Server is down!'

    def forgot_password(self, email):
        try:
            body = {
                'email': email
            }
            response = self.session.post(url=f'{self.URL}/codereset', json=body)
            if response.status_code == 404:
                raise NotEmailError
        except NotEmailError as e:
            return e.__str__()
        except Exception:
            return 'Oh my God! Server is down!'

    def reset_password(self, email, password, code):
        try:
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
        except (NotEmailError, WrongCodeError) as e:
            return e.__str__()
        except Exception as e:
            return 'Oh my God! Server is down!'

    def get_game_save(self, game_id):
        data = {
            'game_id': game_id
        }
        response = self.session.post(url=f'{self.URL}/reset', data=data)

        response = response.json()
        army = response.get('army')
        resources = response.get('resources')
        houses = response.get('houses')

        return army, resources, houses

    def update_game_save(self, game_id, army, resources, houses):
        body = {
            'army': army,
            'resources': resources,
            'houses': houses
        }

        response = self.session.put(
            url=f'{self.URL}/game/{game_id}', json=body)

    def get_all_game_info(self):
        response = self.session.get(url=f'{self.URL}/game')

        return response.json()

    def create_game_save(self, game_id, game_name, army, resources, houses):
        body = {
            'game_id': game_id,
            'game_name': game_name,
            'army': army,
            'resources': resources,
            'houses': houses
        }

        response = self.session.post(url=f'{self.URL}/game', json=body)
