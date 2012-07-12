# -*- coding: utf-8 -*-

"""
"""

import os
import unittest
from http import Response, Headers
import spyre


MY_DIR = os.path.dirname(__file__)
spec = MY_DIR + "/specs/api.json"


def expected_response(request):
    """
    """
    authentication = request.header('Authorization')
    if authentication:
        return Response(200, Headers({'Content-Type': 'text/plain'}),
            content="OK", request=request)
    return Response(403, Headers({'Content-Type': 'text/plain'}), content="KO",
            request=request)


class TestSpyreMiddlewareAuthBasic(unittest.TestCase):
    """
    """

    def setUp(self):
        self.fake_server = {'/test': expected_response}
        self.client = spyre.new_from_spec(spec, base_url='http://localhost')
        self.username = 'my_username'
        self.password = 'my_strongest_password'

    def tearDown(self):
        del self.client

    def test_forbidden(self):
        self.client.enable('Mock', fakes=(self.fake_server))
        result = self.client.get_info()
        self.assertEqual(result.status, 403)
        self.assertEqual(result.content, 'KO')

    def test_authenticated(self):
        self.client.enable('auth.Basic', username=self.username,
            password=self.password)
        self.client.enable('Mock', fakes=(self.fake_server))
        result = self.client.get_info()
        self.assertEqual(result.status, 200)
        self.assertEqual(result.content, 'OK')
