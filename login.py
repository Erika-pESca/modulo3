# -- coding: utf-8 --
import time

from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.prompt import Prompt
from rich.text import Text
from sesion import Sesion
from utils import mostrar_error, pedir_password  # tus funciones auxiliares

import modelo  # tu módulo de datos

console = Console()

def login_ui() -> bool:
    """
    Flujo de inicio de sesión mejorado con diseño visual.
    """
    console.clear()
    console.print(
        Panel.fit(
            Text("🔐 Iniciar Sesión de Autor", style="bold cyan"),
            border_style="bright_blue",
        )
    )

    try:
        email = Prompt.ask(
            "[bold yellow]📧 Correo electrónico[/bold yellow]"
        ).strip().lower()
        password = pedir_password("🔑 Contraseña")

        # Animación de "verificación"
        for _ in track(range(30), description="Verificando credenciales..."):
            time.sleep(0.02)

        autor = modelo.autenticar_autor(email, password)
        if not autor:
            mostrar_error("Correo o contraseña incorrectos. Intenta nuevamente.")
            return False

        # Animación de éxito
        console.print()
        console.print(Panel.fit("✅ Acceso concedido", border_style="green"))
        time.sleep(0.6)
        Sesion.establecer(autor)

        console.clear()
        console.print(
            Panel(
                f"👋 ¡Bienvenido de nuevo, "
                f"[bold green]{autor['nombre_autor']}[/bold green]! ✨",
                border_style="bright_green",
                expand=False,
            )
        )
        return True

    except modelo.ValidacionError as e:
        mostrar_error(str(e))
        return False
    except KeyboardInterrupt:
        console.print("\n[yellow]Operación cancelada por el usuario.[/yellow]")
        return False
