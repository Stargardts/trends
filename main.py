from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse as Html, FileResponse as File, JSONResponse as Json
from retrive import retrieve_data

app = FastAPI()

geodata = retrieve_data()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=Html)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/script.js", response_class=File)
async def script():
    file = File("script.js")
    return file


@app.get("/geojson", response_class=Json)
async def geojson():
    return Json(content=geodata)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
