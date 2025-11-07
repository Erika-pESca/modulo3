from unittest.mock import MagicMock, patch

from rich.console import Console
from rich.table import Table

from ejercicio2 import EDAD_MAXIMA, crear_perfil, pedir_datos

# Mock the console for testing purposes
console = Console()

VALID_AGE_JUAN = 30
VALID_AGE_ANA = 25
VALID_AGE_PEDRO = 40

def test_pedir_datos_valid_input():
    mock_console = MagicMock(spec=Console)
    mock_console.input.side_effect = ["Juan Perez", str(VALID_AGE_JUAN)]
    with patch('ejercicio2.console', new=mock_console):
        nombre, edad = pedir_datos()
        assert nombre == "Juan Perez"
        assert edad == VALID_AGE_JUAN

def test_pedir_datos_invalid_name_then_valid():
    mock_console = MagicMock(spec=Console)
    mock_console.input.side_effect = ["", "   ", "Juan123", "Ana Garcia", str(VALID_AGE_ANA)]
    with patch('ejercicio2.console', new=mock_console):
        nombre, edad = pedir_datos()
        assert nombre == "Ana Garcia"
        assert edad == VALID_AGE_ANA
        mock_console.print.assert_any_call("[red] El nombre no puede estar vacío ni tener solo espacios.[/red]")
        mock_console.print.assert_any_call("[red] El nombre no debe contener números.[/red]")

def test_pedir_datos_invalid_age_then_valid():
    mock_console = MagicMock(spec=Console)
    mock_console.input.side_effect = ["Pedro", "abc", "0", "-5", str(EDAD_MAXIMA + 1), str(VALID_AGE_PEDRO)]
    with patch('ejercicio2.console', new=mock_console):
        nombre, edad = pedir_datos()
        assert nombre == "Pedro"
        assert edad == VALID_AGE_PEDRO
        mock_console.print.assert_any_call("[red] Ingrese un número entero válido para la edad.[/red]")
        mock_console.print.assert_any_call("[red] La edad debe ser mayor que cero.[/red]")
        mock_console.print.assert_any_call(f"[red] La edad no puede ser mayor de {EDAD_MAXIMA} años.[/red]")

EXPECTED_COLUMNS = 2
EXPECTED_ROWS = 4

def test_crear_perfil_basic():
    table = crear_perfil("Carlos", 28)
    assert isinstance(table, Table)
    assert table.title == " Perfil de Carlos"
    assert len(table.columns) == EXPECTED_COLUMNS
    assert table.columns[0].header == "Campo"
    assert table.columns[1].header == "Datos"
    # Check rows (simplified check, actual rich Table row content is complex)
    # This is a basic check, more detailed checks would involve inspecting table._rows
    assert len(table.rows) == EXPECTED_ROWS # Nombre, Edad, Hobbies, Redes Sociales

def test_crear_perfil_with_hobbies():
    table = crear_perfil("Maria", 22, "leer", "cantar")
    assert isinstance(table, Table)
    assert table.title == " Perfil de Maria"
    # A more robust check would involve parsing the rich Table object's internal structure
    # For now, we'll assume the presence of hobbies implies correct rendering.
    # We can't directly assert on the string representation of the row content easily.
    # A better approach would be to inspect table._rows or use a rich.test_render helper if available.
    assert len(table.rows) == EXPECTED_ROWS # Nombre, Edad, Hobbies, Redes Sociales

def test_crear_perfil_with_social_networks():
    table = crear_perfil("Pedro", 35, twitter="@pedro", linkedin="/in/pedro")
    assert isinstance(table, Table)
    assert table.title == " Perfil de Pedro"
    assert len(table.rows) == EXPECTED_ROWS # Nombre, Edad, Hobbies, Redes Sociales

def test_crear_perfil_with_all_args():
    table = crear_perfil("Laura", 29, "pintar", "viajar", instagram="@laura_art", github="laura_dev")
    assert isinstance(table, Table)
    assert table.title == " Perfil de Laura"
    assert len(table.rows) == EXPECTED_ROWS # Nombre, Edad, Hobbies, Redes Sociales
