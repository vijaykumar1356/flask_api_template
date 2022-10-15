from src import create_app
from flask import Flask

if __name__ == "__main__":
    app: Flask = create_app()
    app.run(load_dotenv=True)
