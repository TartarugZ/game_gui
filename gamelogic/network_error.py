class AuthError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Wrong email address or password. Try again'


class TokenError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Somthing is wrong with registration process. Please, try again.'


class NoGameError(Exception):
    def __init__(self, game_id):
        self.id = game_id

    def __str__(self):
        return f'Game with the id {self.id} is not available'


class RegistrationError(Exception):
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return f'User with email {self.email} already exists. Try to log in or reset password'


class DbUnavailableError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'Bad news. Server can\'t connect to our database. Sorry :( Use your local saves to play'


class NotEmailError(Exception):
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return f'Email {self.email} doesn\'t look like a proper email. Please, check it or try another email'


class WrongCodeError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'Wrong code :( Please, check your code and try again'


class WrongEnterError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'Wrong input :( Please, check and try again'


class NeedRefreshToken(Exception):
    def __init__(self):
        pass
    
    def __str__(self):
        return f'Need refresh token'