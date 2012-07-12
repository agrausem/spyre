# -*- coding: utf-8 -*-

from functools import partial
from ..request import Request

"""
"""


class Middleware(object):
    """
    """

    def __init__(self, *args, **kwargs):
        pass


class Mock(Middleware):
    """
    """

    def __init__(self, fakes):
        self.fakes = fakes

    def __call__(self, env):
        finalized_request = Request(env)
        for path, func in self.fakes.items():
            if path == finalized_request.path:
                response = func(finalized_request())
                return response if response else None
