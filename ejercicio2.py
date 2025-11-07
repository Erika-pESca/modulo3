# Ejercicio 2: Generador de Perfiles de Usuario con Argumentos Flexibles
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
EDAD_MAXIMA = 120

def pedir_datos():
    """
    Pide y valida los datos del usuario: nombre y edad.
    Validaciones:
      - El nombre no puede estar vacío ni tener solo espacios.
      - La edad debe ser un número entero positivo.
      - La edad no puede superar los 120 años.
    Returns:
        tuple: (nombre, edad) si los datos son válidos.
    """
    # Validar nombre
    while True:
        nombre = console.input("[cyan]Ingrese su nombre:[/cyan] ").strip()
        if not nombre:
            console.print(
                "[red] El nombre no puede estar vacío ni tener solo espacios.[/red]"
            )
            continue
        # Comprueba si existe al menos un carácter numérico dentro de la variable nombre
        if any(numero.isdigit() for numero in nombre):
            console.print("[red] El nombre no debe contener números.[/red]")
            continue
        break

    # Validar edad
    while True:
        try:
            edad = int(console.input("[cyan]Ingrese su edad:[/cyan] ").strip())
            if edad <= 0:
                console.print("[red] La edad debe ser mayor que cero.[/red]")
                continue
            if edad > EDAD_MAXIMA:
                console.print("[red] La edad no puede ser mayor de 120 años.[/red]")
                continue
            break
        except ValueError:
            console.print("[red] Ingrese un número entero válido para la edad.[/red]")

    return nombre, edad

def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera un perfil de usuario con los datos ingresados.
    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        *hobbies (str): Lista de hobbies opcionales.
        **redes_sociales (str): Diccionario de redes sociales y usuarios.
    Returns:
        str: Texto formateado con la información del perfil.
    """
    # Usamos Rich para mostrar el perfil bonito
    tabla = Table(title=f" Perfil de {nombre}", border_style="cyan")
    tabla.add_column("Campo", style="bold magenta")
    tabla.add_column("Datos", style="bold white")

    tabla.add_row("Nombre", nombre)
    tabla.add_row("Edad", f"{edad} años")

    # Si hay hobbies, los añadimos
    if hobbies:
        tabla.add_row("Hobbies", ", ".join(hobbies))
    else:
        tabla.add_row("Hobbies", "No especificados")

    # Si hay redes sociales, las añadimos
    if redes_sociales:
        redes = "\n".join(
            [f"{red}: {usuario}" for red, usuario in redes_sociales.items()]
        )
        tabla.add_row("Redes Sociales", redes)
    else:
        tabla.add_row("Redes Sociales", "No especificadas")

    return tabla


def main():
    console.print(
        Panel.fit(
            "[bold magenta on white]GENERADOR DE PERFIL DE USUARIO "
            "[/bold magenta on white]"
        )
    )

    # Pedir nombre y edad con validaciones
    nombre, edad = pedir_datos()

    # Pedir hobbies (opcional)
    hobbies_input = console.input(
        "[cyan]Ingrese sus hobbies separados por comas (opcional):[/cyan] "
    ).strip()
    hobbies = [h.strip() for h in hobbies_input.split(",") if h.strip()]

    # Pedir redes sociales (opcional)
    redes_sociales = {}
    while True:
        red = console.input(
            "[cyan]Ingrese el nombre de una red social (o Enter para "
            "finalizar):[/cyan] "
        ).strip()
        if not red:
            break
        usuario = console.input(f"[cyan]Ingrese su usuario en {red}:[/cyan] ").strip()
        if not usuario:
            console.print("[red]El usuario no puede estar vacío.[/red]")
            continue
        redes_sociales[red] = usuario

    # Crear y mostrar el perfil
    perfil = crear_perfil(nombre, edad, *hobbies, **redes_sociales)
    console.print(
        Panel(
            perfil,
            title="[bold magenta]Perfil del usuario[/bold magenta]",
            border_style="green"
        )
    )


if __name__ == "__main__":
    main()
