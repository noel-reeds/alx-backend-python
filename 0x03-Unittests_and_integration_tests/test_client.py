#!/usr/bin/env python3
import unittest
from typing import Dict
from unittest.mock import patch, Mock, PropertyMock as PM
from client import GithubOrgClient
import client as client_module
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Tests for Github client orgs"""
    @parameterized.expand([
        ('google', {'payload': True}),
        ('abc', {'payload': False}),
    ])
    def test_org(self, org_name, response):
        """Test cases"""
        with patch('client.get_json', return_value=response) as mocked:
            client = GithubOrgClient(org_name)
            json = client.org

        mocked.assert_called_once_with(client.ORG_URL.format(org=org_name))
        self.assertEqual(json, response)

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    def test_public_repos_url(self, name):
        """Tests"""
        github_client = GithubOrgClient(name)
        with patch('client.GithubOrgClient.org', new_callable=PM) as mocked:
            mocked.return_value = {'repos_url': 'some public repos'}
            _repos = github_client._public_repos_url

        self.assertEqual(_repos, 'some public repos')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "", False)
    ])
    def test_has_license(self, repo, _license, _bool):
        """Test case for has_license method"""
        self.assertIsNotNone(_license)
        self.assertIsInstance(repo, Dict)
        self.assertIs(GithubOrgClient.has_license(repo, _license), _bool)

