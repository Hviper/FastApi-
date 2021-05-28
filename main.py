from typing import Optional
from youdao import *
from fastapi import FastAPI

app = FastAPI()


t = Translate()


@app.get("/query")
def read_root(
        *, word: str,
        enc=None
):
    return "".join(t.download(word)).strip().replace("\r\n"," ")
##json格式



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
