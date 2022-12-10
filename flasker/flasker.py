import typer

from rich.console import Console
from rich.theme import Theme
from helpers import cleanup_files, print_to_console, write_main_files, run_app
from pathlib import Path


app = typer.Typer()


@app.command("init")
def init_flask(
    cleanup: bool = typer.Option(True, "--clean", "c", is_flag=True),
    app_path: str = "app",
) -> None:

    # Define console and theme
    con = Console(theme=Theme({"question": "bold green"}))

    app_name, run = print_to_console(con)

    # Clean up files if needed, used for development
    if cleanup:
        cleanup_files(app_name)

    # Create initial directory structure
    Path(f"{app_name}/{app_path}").mkdir(exist_ok=True, parents=True)

    write_main_files(app_name, app_path)

    if run == "y":
        run_app(app_name)
    else:
        typer.launch(app_name)
