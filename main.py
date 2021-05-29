from typing import Optional
from youdao import *
from fastapi import FastAPI
import uvicorn
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
##假如需要放在阿里云等云服务器供外部访问，需要将host改为 '0.0.0.0'
uvicorn.run(app,host='127.0.0.1',port=8000)    
