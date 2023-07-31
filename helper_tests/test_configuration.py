# coding: utf-8

"""
    Pure Fusion API
"""

from __future__ import absolute_import

import unittest
import io

from fusion import Configuration


valid_input_configs = [
    """
    {
        "default_profile": "my_profile",
        "profiles": {"my_profile": {"auth": {"issuer_id": "issuer1", "private_pem_file": "pkey1"}, "endpoint": "http://localhost:8080", "env": "pure1stg"}}
    }
    """,
    """
    {
        "default_profile": "my_profile2",
        "profiles": {
            "my_profile": {"auth": {"issuer_id": "issuer1", "private_pem_file": "pkey1"}, "endpoint": "http://localhost:8080", "env": "pure1stg"},
            "my_profile2": {"auth": {"access_token": "token", "private_pem_file": "pkey2", "private_key_password": "pass"}, "endpoint": "http://localhost:8081", "env": "pure1stg"}
        }
    }
    """,
    """
    {
        "default_profile": "my_profile2",
        "profiles": {
            "my_profile": {"auth": {"issuer_id": "issuer1", "private_pem_file": "pkey1"}, "endpoint": "http://localhost:8080", "env": "pure1stg"},
            "my_profile2": {"auth": {"issuer_id": "issuer2", "private_pem_file": "pkey2"}, "endpoint": "http://localhost:8081", "env": "pure1stg"}
        }
    }
    """,
    """
    {
        "default_profile": "my_profile",
        "profiles": {
            "my_profile": {"auth": {"access_token": "token", "private_pem_file": "pkey1", "token_endpoint": "token_endpoint:8000"}, "endpoint": "http://localhost:8080", "env": "pure1stg"}
        }
    }
    """
]

valid_input_profiles = [None, None, "my_profile", None]

valid_expected = [
    {
        "issuer_id": "issuer1",
        "private_key_file": "pkey1",
        "host": "http://localhost:8080/api/v1",
        "token_endpoint": "https://api.pure1.purestorage.com/oauth2/1.0/token",
        "_external_access_token": "",
    },
    {
        "private_key_file": "pkey2",
        "private_key_password": "pass",
        "host": "http://localhost:8081/api/v1",
        "token_endpoint": "https://api.pure1.purestorage.com/oauth2/1.0/token",
        "_external_access_token": "token",
    },
    {
        "issuer_id": "issuer1",
        "private_key_file": "pkey1",
        "host": "http://localhost:8080/api/v1",
        "token_endpoint": "https://api.pure1.purestorage.com/oauth2/1.0/token",
        "_external_access_token": "",
    },
    {
        "private_key_file": "pkey1",
        "host": "http://localhost:8080/api/v1",
        "token_endpoint": "token_endpoint:8000",
        "access_token": "token",
    },
]


invalid_input_configs = [
    '{}',
    '{"default_profile": {}}',
    '{}',
    '{"profiles": "abc"}',
    '{"profiles": {}}',
    '{"profiles": {"my_profile": "abc"}}',
    '{"profiles": {"my_profile": {}}}',
    '{"profiles": {"my_profile": {"auth": "abc"}}}',
]

invalid_input_profiles = [None, None, "my_profile", "my_profile", "my_profile"]

invalid_expected = [
    (ValueError, "Invalid configuration file format - missing the 'default_profile' field"),
    (ValueError, "Expected selected 'profile' to be a string, got <class 'dict'>"),
    (ValueError, "Invalid configuration file format - missing the 'profiles' field"),
    (ValueError, "Invalid configuration profiles - expected 'profiles' to be a dict, got <class 'str'>"),
    (ValueError, "Invalid configuration profile - cannot find profile 'my_profile'"),
    (ValueError, "Invalid configuration profiles - expected 'profiles' to be a dict, got <class 'str'>"),
    (ValueError, "Invalid configuration profiles - expected selected 'profile' to be a dict, got <class 'str'>"),
    (ValueError, "Invalid configuration profiles - cannot find 'auth'"),
    (ValueError, "Invalid configuration profiles - expected 'auth' to be a dict, got <class 'str'>"),
]


class TestConfiguration(unittest.TestCase):
    """Configuration unit tests"""

    def test_valid_configuration(self):
        """Test case for getting valid configuration"""
        for expected, config, profile in zip(valid_expected, valid_input_configs, valid_input_profiles):
            file = io.StringIO(config)
            configuration = Configuration(fusion_config=file, fusion_config_profile=profile)

            for key, expected_value in expected.items():
                self.assertEqual(expected_value, getattr(configuration, key))

    def test_get_placement_recommendation(self):
        """Test case for getting invalid configuration"""
        for (expected_type, expected_msg), config, profile in zip(invalid_expected, invalid_input_configs, invalid_input_profiles):
            file = io.StringIO(config)
        
            with self.assertRaises(expected_type) as ctx:
                Configuration(fusion_config=file, fusion_config_profile=profile)
            self.assertEqual(expected_msg, str(ctx.exception))
    
    def test_url_contains_version(self):
        """Test case for testing url contains version"""
        test_cases = [
            ("x/api/v1", True),
            ("x/api/v1/", True),
            ("api/v1/", True),
            ("api/v1", True),
            ("api/1.0/", True),
            ("api/1.0", True),
            ("x/api/vabc", False),
            ("x/api/vabc/", False),
            ("api/1.0/abc", False),
            ("abc/1.0", False),
        ]

        for url, expected in test_cases:
            self.assertEqual(expected, Configuration._url_contains_version(url))


if __name__ == '__main__':
    unittest.main()
