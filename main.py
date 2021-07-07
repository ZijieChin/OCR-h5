from controller.api import app
from src.methods import configReader
import uvicorn


if __name__ == "__main__":
    api = configReader()
    if api != '':
        uvicorn.run(app, host="localhost", port=8000)
