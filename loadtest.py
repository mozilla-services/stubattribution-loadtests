import os
from molotov import scenario


_SERVER = os.getenv('SERVER', 'http://localhost:8080')


@scenario(10)
async def scenario_one(session):
    async with session.get(_SERVER) as resp:
        assert resp.status == 200
