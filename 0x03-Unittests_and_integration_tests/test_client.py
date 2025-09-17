#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Tests for Github client orgs"""
    @parameterized.expand([
        ('google', {'payload': True}),
        ('abc', {'payload': False}),
    ])
    def test_org(self, org_name, response):
        """Test cases"""
        client = GithubOrgClient(org_name)

        with patch('client.get_json') as mocked:
            mock = Mock()
            mock.get_json.return_value = response
            mocked.return_value = mock

            json = client.org

        mocked.assert_called_once_with(client.ORG_URL.format(org=org_name))
