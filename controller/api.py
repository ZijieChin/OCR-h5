from fastapi import FastAPI
from src.methods import getImg, configReader, getrec
from pydantic import BaseModel

app = FastAPI()
api = configReader()


class Image(BaseModel):
    image: str


@app.post("/")
async def home(img: Image):
    img_path = getImg(img.image)
    if img_path == 0:
        return {
            "code": 5001,
            "msg": "无法获取图片信息，请重试",
        }
    rec = getrec(img_path, api)
    return {
        "code": 2001,
        "msg": rec,
    }
