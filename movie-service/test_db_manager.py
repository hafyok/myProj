import pytest
from unittest.mock import AsyncMock, patch
from app.api.models import MovieIn, MovieOut, MovieUpdate
from app.api.movies import create_movie, get_movies, get_movie, update_movie, delete_movie


@pytest.fixture
def mock_db_manager():
    with patch("app.api.movies.db_manager", autospec=True) as mock:
        yield mock


@pytest.mark.asyncio
async def test_get_movies(mock_db_manager):
    mock_db_manager.get_all_movies.return_value = [
        {"id": 1, "name": "Inception", "plot": "A mind-bending movie", "genres": ["Sci-Fi", "Action"],
         "casts_id": [1, 2, 3]},
        {"id": 2, "name": "Interstellar", "plot": "Space exploration", "genres": ["Sci-Fi", "Drama"],
         "casts_id": [4, 5, 6]}
    ]

    response = await get_movies()

    assert response == [
        {"id": 1, "name": "Inception", "plot": "A mind-bending movie", "genres": ["Sci-Fi", "Action"],
         "casts_id": [1, 2, 3]},
        {"id": 2, "name": "Interstellar", "plot": "Space exploration", "genres": ["Sci-Fi", "Drama"],
         "casts_id": [4, 5, 6]}
    ]
