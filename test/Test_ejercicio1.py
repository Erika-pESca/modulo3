from unittest.mock import MagicMock, patch

from rich.console import Console

from ejercicio1 import calcular_imc, interpretar_imc, pedir_dato

# Mock the console for testing purposes
console = Console()

IMC_70_175 = 22.86
IMC_80_180 = 24.69

def test_calcular_imc_metros():
    # Test con altura en metros
    assert calcular_imc(70, 1.75) == IMC_70_175
    assert calcular_imc(80, 1.80) == IMC_80_180

def test_calcular_imc_centimetros():
    # Test con altura en centímetros (debe convertir a metros)
    assert calcular_imc(70, 175) == IMC_70_175
    assert calcular_imc(80, 180) == IMC_80_180

IMC_50_160 = 19.53
IMC_120_170 = 41.52

def test_calcular_imc_edge_cases():
    # Test con valores límite o cercanos a ellos
    assert calcular_imc(50, 1.60) == IMC_50_160 # Normal
    assert calcular_imc(120, 1.70) == IMC_120_170 # Obesidad

def test_interpretar_imc_bajo_peso():
    assert interpretar_imc(18.0) == "Bajo peso"
    assert interpretar_imc(15.0) == "Bajo peso"

def test_interpretar_imc_normal():
    assert interpretar_imc(18.5) == "Normal"
    assert interpretar_imc(22.0) == "Normal"
    assert interpretar_imc(24.9) == "Normal"

def test_interpretar_imc_sobrepeso():
    assert interpretar_imc(25.0) == "Sobrepeso"
    assert interpretar_imc(27.5) == "Sobrepeso"
    assert interpretar_imc(29.9) == "Sobrepeso"

def test_interpretar_imc_obesidad():
    assert interpretar_imc(30.0) == "Obesidad"
    assert interpretar_imc(35.0) == "Obesidad"

VALID_WEIGHT_1 = 70.0
VALID_WEIGHT_2 = 60.0

def test_pedir_dato_valid_input():
    mock_console = MagicMock(spec=Console)
    mock_console.input.side_effect = [str(VALID_WEIGHT_1)]
    with patch('ejercicio1.console', new=mock_console):
        assert pedir_dato("Ingrese su peso:") == VALID_WEIGHT_1

def test_pedir_dato_invalid_then_valid_input():
    mock_console = MagicMock(spec=Console)
    mock_console.input.side_effect = ['-10', 'abc', '0', str(VALID_WEIGHT_2)]
    with patch('ejercicio1.console', new=mock_console):
        assert pedir_dato("Ingrese su peso:") == VALID_WEIGHT_2
        mock_console.print.assert_any_call("[red]El valor debe ser mayor que cero.[/red]")
        mock_console.print.assert_any_call("[red]Por favor, ingrese un número válido.[/red]")
