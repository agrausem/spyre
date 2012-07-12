# -*- coding: utf-8 -*-

"""
"""

import base64
from . import Middleware


class Auth(Middleware):
    """
    """

    def __init__(self, *args, **kwargs):
        super(Auth, self).__init__(*args, **kwargs)

    def __call__(self, env):
        raise NotImplementedError

    def should_authenticate(self, env):
        return env['spore.authentication']


class Basic(Auth):
    """
    """

    def __init__(self, username, password, *args, **kwargs):
        super(Basic, self).__init__(*args, **kwargs)
        self.username = username
        self.password = password

    def __call__(self, env):
        if self.should_authenticate(env):
            env.setdefault('spore.headers', [])
            auth_basic_header = ('Authorization', 'Basic {0}'.format(
                base64.b64encode('{0}:{1}'.format(self.username, self.password)))
            )
            env['spore.headers'].append(auth_basic_header)


class Header(Auth):
    """
    """

    def __init__(self, header_name, header_value, *args, **kwargs):
        super(Header, self).__init__(*args, **kwargs)
        self.header_name = header_name
        self.header_value = header_value

    def __call__(self, env):
        if self.should_authenticate(env):
            env.setdefault('spore.headers', [])
            header = (self.header_name, self.header_value)
            env['spore.headers'].append(header)
