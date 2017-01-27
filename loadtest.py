import hashlib
import hmac
import os
from time import time
from urllib.parse import quote_plus
from uuid import uuid4

from molotov import scenario


_SERVER = os.getenv('SERVER', 'https://stubattribution-default.stage.mozaws.net/')
_HMAC_KEY = os.getenv('HMAC_KEY', default=None)


def signed_codes():
    # random data
    codes = (
        ('source', 'google'),
        ('medium', str(uuid4())),
        ('campaign', '(not set)'),
        ('content', '(not set)'),
        ('timestamp', str(int(time()))),
    )
    code = '&'.join('='.join(attr) for attr in codes)
    code = quote_plus(code)
    sig = hmac.new(_HMAC_KEY.encode(), code.encode(), hashlib.sha256).hexdigest()
    return code, sig


@scenario(100)
async def scenario_one(session):
    if _HMAC_KEY is None:
        raise RuntimeError('No HMAC_KEY set')

    code, sig = signed_codes()
    params = [('product', 'test-stub'), ('os', 'win'),
              ('lang', 'en-US'), ('attribution_code', code),
              ('attribution_sig', sig)]

    async with session.get(_SERVER, params=params) as resp:
        assert resp.status == 200
