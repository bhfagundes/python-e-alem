import pytest
from unittest.mock import Mock, patch
from services.analise_solo_service import AnaliseSoloService

@pytest.fixture
def mock_repository():
    return Mock()

@pytest.fixture
def service(mock_repository):
    service = AnaliseSoloService()
    service.repository = mock_repository
    return service

def test_salvar_analise(service, mock_repository):
    service.salvar_analise(6.5, 60, 25, 120, 45, 80, 1)
    mock_repository.salvar.assert_called_once_with(6.5, 60, 25, 120, 45, 80, 1)

def test_ler_e_salvar_csv(service, mock_repository):
    with patch('builtins.open', create=True) as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.readlines.return_value = [
            "pH,umidade,temperatura,N,P,K,fertilidade\n",
            "6.5,60,25,120,45,80,1\n",
            "5.8,45,22,80,30,60,0\n"
        ]
        result = service.ler_e_salvar_csv("dummy_path.csv")
    
    assert result == 2
    mock_repository.salvar_em_lote.assert_called_once()

@patch('joblib.load')
def test_prever_fertilidade(mock_joblib_load, service):
    mock_scaler = Mock()
    mock_model = Mock()
    mock_joblib_load.side_effect = [mock_scaler, mock_model]

    service.carregar_modelo()
    mock_scaler.transform.return_value = [[1, 2, 3, 4, 5, 6]]
    mock_model.predict.return_value = [1]

    result = service.prever_fertilidade(6.5, 60, 25, 120, 45, 80)
    assert result == 1

    mock_scaler.transform.assert_called_once()
    mock_model.predict.assert_called_once()

def test_treinar_modelo(service, mock_repository):
    mock_repository.obter_todos_dados.return_value = [
        (6.5, 60, 25, 120, 45, 80, 1),
        (5.8, 45, 22, 80, 30, 60, 0)
    ]

    with patch('joblib.dump') as mock_joblib_dump:
        result = service.treinar_modelo()

    assert result == True
    assert mock_joblib_dump.call_count == 2
