import pytest
import asyncio
from app.api.db_manager import add_cast, get_cast
from app.api.models import CastIn
from app.api.db import database

@pytest.mark.asyncio
async def test_add_and_get_cast():
    await database.connect()

    test_cast_data = {
        "name": "Test Actor",
        "nationality": "Test Nationality"
    }
    test_cast = CastIn(**test_cast_data)

    try:
        cast_id = await add_cast(test_cast)

        retrieved_cast = await get_cast(cast_id)

        assert retrieved_cast['id'] == cast_id
        assert retrieved_cast['name'] == test_cast_data['name']
        assert retrieved_cast['nationality'] == test_cast_data['nationality']
    finally:
        await database.disconnect()
