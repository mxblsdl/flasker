from logging import warning
import shutil

import typer
import os


def print_to_console(con):
    con.rule("  Welcome to the Flask Initializer  ", style="white on blue")
    con.print("[green]_\n_")

    # Collect inputs from user
    app_name = con.input("[question]What is name of your app?").lower()

    if " " in app_name:
        con.print("[magenta]Spaces in app name have been removed")
        app_name = replace_spaces(app_name)
        con.print(f"Name of app will be [magenta]{app_name}[/magenta]")

    run = con.input("[question]Do you want to run the app on creation?(y/n)").lower()
    while run not in ["y", "n"]:
        run = con.input("[question]Please answer with y or n")
    return app_name, run


# Helper functions
def write_main_files(app_name, app_path):
    # Create the init file
    f = open(f"{app_name}/{app_path}/__init__.py", "w")
    f.writelines(
        [
            "from flask import Flask\n\n\n",
            "app = Flask(__name__)\n",
            "from app import routes",
        ]
    )
    f.close()

    # Create the environment file
    f = open(f"{app_name}/.flaskenv", "w")
    f.writelines(
        ["FLASK_DEBUG=1\n", "TEMPLATES_AUTO_RELOAD=1\n", f"FLASK_APP={app_name}.py\n"]
    )
    f.close()

    # Create the routes file
    text = """
    <h1>Welcome to Flask!</h1>
    <br>
    <h3>Edit the `routes.py` file to see changes in the app</h3>
    """
    f = open(f"{app_name}/{app_path}/routes.py", "w")
    f.writelines(
        [
            "from app import app\n\n\n",
            "@app.route('/')\n",
            "@app.route('/index')\n",
            "def index():\n",
            f"\treturn '''{text}",
            "'''",
        ],
    )
    f.close()

    # Create the app file
    f = open(f"{app_name}/{app_name}.py", "w")
    f.write("from app import app\n")
    f.close()


def cleanup_files(app_name):
    try:
        shutil.rmtree(f"{app_name}")
    except:
        warning("Path does not exist to remove")


def replace_spaces(string):
    while "  " in string:
        string = string.replace("  ", " ")
    string = string.replace(" ", "_")
    return string


def run_app(app_name):
    typer.launch("http://127.0.0.1:5000/")
    os.system(f"cd {app_name} && flask run")
