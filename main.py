import webbrowser

import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from typing_extensions import Annotated
from datetime import datetime

from src.servershell.Config import cmdList

app = FastAPI()
templates = Jinja2Templates(directory="src/tmpl")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        name="index.html", context={"object_list": cmdList, "request": request}
    )


@app.post("/task/")
async def cmd(name: Annotated[str, Form()], date: Annotated[str, Form()], path: Annotated[str, Form()]):
    print(name,
          datetime.strptime(date, "%Y-%m-%d"),
          path.strip())
    return True


if __name__ == "__main__":
    webbrowser.open_new("http://127.0.0.1:8808")
    uvicorn.run(app, host="127.0.0.1", port=8808)
