#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Tests for Github client orgs"""
    @parameterized.expand([
        ('google', {'payload': True}),
        ('abc', {'payload': False}),
    ])
    def test_org(self, org_name, res):
        """Test cases"""
        with patch('client.get_json', new_callable=PropertyMock) as mocked:
            mocked.return_value = res
            client = GithubOrgClient(org_name)
            json = client.org

        mocked.assert_called_once_with(client.ORG_URL.format(org=org_name))
        self.assertEqual(json, res)
