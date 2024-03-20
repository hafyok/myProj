import pytest
from unittest.mock import AsyncMock, patch
from app.api.models import CastIn, CastOut
from app.api.casts import create_cast, get_cast


@pytest.fixture
def mock_db_manager():
    with patch("app.api.casts.db_manager", autospec=True) as mock:
        yield mock


@pytest.mark.asyncio
async def test_create_cast(mock_db_manager):
    payload = CastIn(name="John Doe", nationality="American")
    mock_db_manager.add_cast.return_value = 1  # Simulate the ID returned by the database

    response = await create_cast(payload)

    assert response == {"id": 1, "name": "John Doe", "nationality": "American"}
    mock_db_manager.add_cast.assert_called_once_with(payload)


@pytest.mark.asyncio
async def test_get_cast(mock_db_manager):
    cast_id = 1
    mock_db_manager.get_cast.return_value = {"id": cast_id, "name": "John Doe", "nationality": "American"}

    response = await get_cast(cast_id)

    assert response == {"id": cast_id, "name": "John Doe", "nationality": "American"}
    mock_db_manager.get_cast.assert_called_once_with(cast_id)
