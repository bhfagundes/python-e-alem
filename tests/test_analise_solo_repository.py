import pytest
from unittest.mock import Mock, patch
from repositories.analise_solo_repository import AnaliseSoloRepository

@pytest.fixture
def repository():
    return AnaliseSoloRepository()

@patch('db.connection.OracleConnection')
def test_salvar(mock_connection, repository):
    mock_cursor = Mock()
    mock_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

    repository.salvar(6.5, 60, 25, 120, 45, 80, 1)

    mock_cursor.execute.assert_called_once()
    mock_cursor.execute.assert_called_with(
        """
            INSERT INTO analise_solo (pH, umidade, temperatura, N, P, K, fertilidade)
            VALUES (:1, :2, :3, :4, :5, :6, :7)
        """,
        (6.5, 60, 25, 120, 45, 80, 1)
    )

@patch('db.connection.OracleConnection')
def test_obter_todos_dados(mock_connection, repository):
    mock_cursor = Mock()
    mock_cursor.fetchall.return_value = [
        (6.5, 60, 25, 120, 45, 80, 1),
        (5.8, 45, 22, 80, 30, 60, 0)
    ]
    mock_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

    result = repository.obter_todos_dados()

    assert len(result) == 2
    assert result[0] == (6.5, 60, 25, 120, 45, 80, 1)
    assert result[1] == (5.8, 45, 22, 80, 30, 60, 0)
    mock_cursor.execute.assert_called_once_with(
        'SELECT pH, umidade, temperatura, N, P, K, fertilidade FROM analise_solo'
    )
