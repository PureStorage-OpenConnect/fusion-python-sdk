import fusion
from fusion_helpers.shared_files.token_manager import TokenManager


class Configuration(fusion.configuration.Configuration):

    def __init__(self):
        self.token_endpoint = 'https://api.pure1.purestorage.com/oauth2/1.0/token'
        self._external_access_token = ''
        self._token_man = None
        self.issuer_id = ""
        self.private_key_file = ""
        self.private_key_password = ""

        super().__init__()

    @property
    def access_token(self):
        if self._external_access_token:
            return self._external_access_token
        if not self.issuer_id or not self.private_key_file:
            raise Exception(
                "you need to set access_token or set issuer_id and private_key_file")
        if self._token_man is None:
            self._token_man = TokenManager(self.token_endpoint,
                                           private_key_file=self.private_key_file,
                                           private_key_password=self.private_key_password,
                                           payload={'iss': self.issuer_id})
        return self._token_man.get_access_token()

    @access_token.setter
    def access_token(self, token):
        # when super class call self.access_token = '', this function will be called
        if token != '':
            print('INFO: setting access_token from external source. Generate access token from issuer_id and private_key_file is disabled')
            print('Recommand way of using Configuration: fusion.Configuration(issuer_id=<MY_ID>, private_key_file=<PATH_TO_KEY>)')
        if self._external_access_token != '':
            print('WARN: set overwriting access_token from external source')
        self._external_access_token = token
