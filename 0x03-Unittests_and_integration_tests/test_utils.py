#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized, parameterized_class
access_nested_map = __import__('utils').access_nested_map
utils = __import__('utils')
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """unit test for utils.access_nested_map"""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_return):
        "Tests for access_nested_map function"
        self.assertEqual(access_nested_map(nested_map, path), expected_return)

    @parameterized.expand([
        ({}, ('a',), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mocks HTTP calls"""
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    def test_get_json(self, test_uri, params):
        with patch('utils.requests.get') as mocked:
            mock = Mock()
            mock.json.return_value = params
            mocked.return_value = mock

            response = utils.get_json(test_uri)
        mocked.assert_called_once_with(test_uri)
        self.assertEqual(response, params)


class TestMemoize(unittest.TestCase):
    """Tests for memoized method"""
    def test_memoize(self):

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_object = TestClass()

        with patch.object(test_object, 'a_method') as mocked_a:
            mock = Mock()
            mock.a_method.return_value = 42
            mocked_a.return_value = mock

            ret_value = test_object.a_property
            returned = test_object.a_property
        mocked_a.assert_called_once()
