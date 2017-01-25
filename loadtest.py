import os
from molotov import scenario, setup


_SERVER = os.getenv('SERVER', 'http://localhost:8080')
_STUB = 'https://www-demo4.allizom.org/en-US/firefox/stub_attribution_code/'


@setup()
async def _init(args):
    return {}


@scenario(10)
async def scenario_one(session):
    headers = {'X-Requested-With': 'XMLHttpRequest'}
    query = '?utm_source=1&utm_medium=2&utm_referrer=ok'
    async with session.get(_STUB + query, headers=headers) as resp:
        result = await resp.json()
        assert resp.status == 200
