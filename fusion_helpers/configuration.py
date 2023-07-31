import os
import json
import urllib.parse
from typing import Optional, Union, TextIO, Dict
from pathlib import Path

import fusion
from fusion_helpers.shared_files.token_manager import TokenManager


#Env Var Constants
ENV_API_HOST = "FUSION_API_HOST"
ENV_ISSUER_ID = "FUSION_ISSUER_ID"
ENV_PRIVATE_KEY_FILE = "FUSION_PRIVATE_KEY_FILE"
ENV_PRIVATE_KEY_PASSWORD = "FUSION_PRIVATE_KEY_PASSWORD"
ENV_ACCESS_TOKEN = "FUSION_ACCESS_TOKEN"
ENV_TOKEN_ENDPOINT = "FUSION_TOKEN_ENDPOINT"
ENV_FUSION_CONFIG = "FUSION_CONFIG"
ENV_FUSION_CONFIG_PROFILE = "FUSION_CONFIG_PROFILE"

#Config Constants
CONFIG_API_HOST = "endpoint"
CONFIG_ISSUER_ID = "issuer_id"
CONFIG_PRIVATE_KEY_FILE = "private_pem_file"
CONFIG_PRIVATE_KEY_PASSWORD = "private_key_password"
CONFIG_ACCESS_TOKEN = "access_token"
CONFIG_TOKEN_ENDPOINT = "token_endpoint"

# Field Constants
FUSION_CONFIG = "fusion_config"
FUSION_CONFIG_PROFILE = "fusion_config_profile"
TOKEN_ENDPOINT = "token_endpoint"
ACCESS_TOKEN = "access_token"
ISSUER_ID = "issuer_id"
PRIVATE_KEY_FILE = "private_key_file"
PRIVATE_KEY_PASSWORD = "private_key_password"
API_HOST = "host"

DEFAULT_CONFIG = {
    TOKEN_ENDPOINT: "https://api.pure1.purestorage.com/oauth2/1.0/token",
    ACCESS_TOKEN: "",
    ISSUER_ID: "",
    PRIVATE_KEY_FILE: "",
    PRIVATE_KEY_PASSWORD: "",
    API_HOST: "",
}

DEFAULT_CONFIG_FILE = "~/.pure/fusion.json"


# Hack for broken __call__ on TypeWithDefault class (disable weird "singleton"-like behavior)
fusion.configuration.TypeWithDefault.__call__ = type.__call__


class Configuration(fusion.configuration.Configuration):

    __slots__ = (
        "_token_man", "host", "_external_access_token", "token_endpoint",
        "issuer_id", "private_key_file", "private_key_password",
    )

    def __init__(
        self,
        api_host: Optional[str] = None,
        access_token: Optional[str] = None,
        issuer_id: Optional[str] = None,
        private_key_file: Optional[str] = None,
        private_key_password: Optional[str] = None,
        token_endpoint: Optional[str] = None,
        fusion_config: Optional[Union[str, os.PathLike, TextIO]] = None,
        fusion_config_profile: Optional[str] = None, 
    ):
        self._token_man: Optional[TokenManager] = None
        self._external_access_token = ""
        self.token_endpoint = ""
        self.issuer_id = ""
        self.private_key_file = ""
        self.private_key_password = ""

        super().__init__()

        input_config = Configuration._clean_and_validate({
            API_HOST: api_host,
            ISSUER_ID: issuer_id,
            PRIVATE_KEY_FILE: private_key_file,
            PRIVATE_KEY_PASSWORD: private_key_password,
            ACCESS_TOKEN: access_token,
            TOKEN_ENDPOINT: token_endpoint,
        })

        env_config = Configuration.from_env()
        profile = fusion_config_profile or env_config.get(FUSION_CONFIG_PROFILE)

        file_config = {}
        if isinstance(fusion_config, (str, os.PathLike, Path)):
            file_config = Configuration.from_filepath(fusion_config, profile)
        elif fusion_config is not None:
            file_config = Configuration.from_file(fusion_config, profile)
        elif env_config.get(FUSION_CONFIG) is not None:
            file_config = Configuration.from_filepath(env_config.get(FUSION_CONFIG), profile)
        else:
            try:
                file_config = Configuration.from_filepath(DEFAULT_CONFIG_FILE, profile)
            except Exception:
                pass
        
        config = DEFAULT_CONFIG.copy()
        config = Configuration.merge(config, file_config)
        config = Configuration.merge(config, env_config)
        config = Configuration.merge(config, input_config)
        self.set_from_dict(config)

    def set_from_dict(self, config_dict: Dict[str, Optional[str]]):
        """
        Create configuration values from dict.

        Args:
            config_dict (dict): The configuration dictionary.
        """
        for key, value in config_dict.items():
            if key in (FUSION_CONFIG, FUSION_CONFIG_PROFILE):
                continue
            if key not in DEFAULT_CONFIG:
                raise ValueError(f"Invalid config parameter - '{key}'")
            if key == ACCESS_TOKEN:
                self._external_access_token = value
                continue
            if key == API_HOST and value is not None and not Configuration._url_contains_version(value):
                value = urllib.parse.urljoin(value, "api/v1")
            setattr(self, key, "" if value is None else value)

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
            print('Recommended way of using Configuration: fusion.Configuration(issuer_id=<MY_ID>, private_key_file=<PATH_TO_KEY>)')
        if self._external_access_token != '':
            print('WARN: set overwriting access_token from external source')
        self._external_access_token = token

    @staticmethod
    def from_dict(config_dict: Dict[str, Optional[str]]) -> "Configuration":
        """
        Create a configuration from configuration dictionary.

        Args:
            config_dict (dict): The configuration dictionary.

        Returns:
            Configuration
        """
        configuration = Configuration.__new__(Configuration)
        fusion.Configuration.__init__(configuration)
        configuration.set_from_dict(config_dict)

        return configuration

    @staticmethod
    def merge(config_dict1: Dict[str, Optional[str]], config_dict2: Dict[str, Optional[str]]) -> Dict[str, Optional[str]]:
        """
        Merge two config dicts together. The second config dict has a higher priority.
        Both configurations are supposed to be flat dictionaries without nested structures.

        Args:
            config_dict1 (dict): The configuration dictionary.
            config_dict2 (dict): The configuration dictionary.

        Returns:
            dict 
        """
        res = config_dict1.copy()
        
        if ISSUER_ID in config_dict2 and ACCESS_TOKEN in res:
            res[ACCESS_TOKEN] = ""

        res.update(config_dict2)
        return res

    @staticmethod
    def from_env() -> Dict[str, Optional[str]]:
        """
        Create a configuration dict from env variables. If the config env var is provided, it will load
        this config as well, with lower priority than the rest of env vars.

        Returns:
            dict

        Raises:
            FileNotFoundError: If the configuration path does not reference a file.
            ValueError: If the configuration has a wrong format.
        """
        return Configuration._clean_and_validate({
            API_HOST: os.getenv(ENV_API_HOST),
            ISSUER_ID: os.getenv(ENV_ISSUER_ID),
            PRIVATE_KEY_FILE: os.getenv(ENV_PRIVATE_KEY_FILE),
            PRIVATE_KEY_PASSWORD: os.getenv(ENV_PRIVATE_KEY_PASSWORD),
            ACCESS_TOKEN: os.getenv(ENV_ACCESS_TOKEN),
            TOKEN_ENDPOINT: os.getenv(ENV_TOKEN_ENDPOINT),
            FUSION_CONFIG: os.getenv(ENV_FUSION_CONFIG),
            FUSION_CONFIG_PROFILE: os.getenv(ENV_FUSION_CONFIG_PROFILE),
        })

    @staticmethod
    def from_filepath(path: Union[str, os.PathLike, Path], profile: Optional[str]=None) -> Dict[str, str]:
        """
        Create a configuration dictionary from a config filepath.

        Args:
            path (Union[str, os.PathLike, Path]): The path to the configuration file.
            profile (Optional[str]): The profile to load configuration from. If `None`, 
                the profile is read from the `default_profile` field in the configuration.

        Returns:
            dict

        Raises:
            FileNotFoundError: If the configuration path does not reference a file.
            ValueError: If the configuration has a wrong format. 
        """
        path = Path(path).expanduser()
        if not path.is_file():
            raise FileNotFoundError(f"'{path}' is not a file")        

        with open(str(path), mode="r") as file:
            return Configuration.from_file(file, profile)

    @staticmethod
    def from_file(file: TextIO, profile: Optional[str]=None) -> Dict[str, str]:
        """
        Create a configuration dictionary from a config file.

        Args:
            file (TextIO): The configuration file.
            profile (Optional[str]): The profile to load configuration from. If `None`, 
                the profile is read from the `default_profile` field in the configuration.

        Returns:
            dict

        Raises:
            FileNotFoundError: If the configuration path does not reference a file.
            ValueError: If the configuration has a wrong format. 
        """
        config = json.load(file)

        if profile is None:
            if "default_profile" not in config:
                raise ValueError("Invalid configuration file format - missing the 'default_profile' field")
            profile = config["default_profile"]

            if not isinstance(profile, str):
                raise ValueError(f"Expected selected 'profile' to be a string, got {type(profile)}")

        if "profiles" not in config:
            raise ValueError("Invalid configuration file format - missing the 'profiles' field")

        profiles = config["profiles"]
        if not isinstance(profiles, dict):
            raise ValueError(f"Invalid configuration profiles - expected 'profiles' to be a dict, got {type(profiles)}")
        if profile not in profiles:
            raise ValueError(f"Invalid configuration profile - cannot find profile '{profile}'")

        profile_config = profiles[profile]
        if not isinstance(profile_config, dict):
            raise ValueError(f"Invalid configuration profiles - expected selected 'profile' to be a dict, got {type(profile_config)}")

        if "auth" not in profile_config:
            raise ValueError(f"Invalid configuration profile - cannot find 'auth'")
        auth = profile_config["auth"]
        if not isinstance(auth, dict):
            raise ValueError(f"Invalid configuration profiles - expected 'auth' to be a dict, got {type(auth)}")

        return Configuration._clean_and_validate({
            API_HOST: profile_config.get(CONFIG_API_HOST),
            ISSUER_ID: auth.get(CONFIG_ISSUER_ID),
            PRIVATE_KEY_FILE: auth.get(CONFIG_PRIVATE_KEY_FILE),
            PRIVATE_KEY_PASSWORD: auth.get(CONFIG_PRIVATE_KEY_PASSWORD),
            ACCESS_TOKEN: auth.get(CONFIG_ACCESS_TOKEN),
            TOKEN_ENDPOINT: auth.get(CONFIG_TOKEN_ENDPOINT),
        })

    @staticmethod
    def _clean_and_validate(config_dict: Dict[str, Optional[str]]) -> Dict[str, str]:
        return_dict = {}
        for key, value in config_dict.items():
            if value is None:
                continue
            if not isinstance(value, str):
                raise ValueError(f"Got unexpected type '{type(value)}' of the configuration key {key}, value {value}")
            return_dict[key] = value
        return return_dict

    @staticmethod
    def _is_version_number(string: str) -> bool:
        if len(string) == 0:
            return False

        try:
            float(string)
            return True
        except ValueError:
            return string[0] == "v" and string[1:].isnumeric()

    @staticmethod
    def _url_contains_version(url: str) -> bool:
        parts = url.split("/")
        if len(parts) < 2:
            return False
        if parts[-2] == "api":
            return Configuration._is_version_number(parts[-1])
        if len(parts) > 2 and parts[-3] == "api" and parts[-1] == "":
            return Configuration._is_version_number(parts[-2])
        return False
