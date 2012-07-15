import __future__
from spyre.core import Spore
from errors import *
import os.path
from httpclient import HTTPClient


def new_from_spec(spec_file, base_url=None):
    spec_string = _read_from_file(spec_file)
    spore = new_from_string(spec_string, base_url)
    return spore


def new_from_string(spec_string, base_url=None):
    try:
        spore = Spore(spec_string=spec_string, base_url=base_url)
    except Exception, e:
        raise SpyreObjectBuilder(e)
    return spore


def new_from_url(spec_url, base_url=None):
    http_client = HTTPClient()
    response = http_client.get(spec_url)
    return new_from_string(response.content, base_url)


def _read_from_file(spec_file):
    if os.path.exists(spec_file) == False:
        raise SpyreObjectBuilder(
            "Spec file {file} does not exists".format(file=spec_file))

    try:
        f = open(spec_file, 'r')
        spec = f.read()
        f.close()
    except Exception, e:
        raise RuntimeError(
            "Error while loading JSON spec {file}: {error}".format(
                file=spec_file, error=e))

    return spec
