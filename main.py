from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from models import Body
from api import BT_API

app = FastAPI()
templates = Jinja2Templates(directory="templates")
bt = BT_API()


@app.get("/")
async def index():
    return HTMLResponse(open('templates/index.html').read())


@app.post("/result")
async def result(body: Body):
    prices = bt.get_prices(body.currencies)
    print(prices)
    return HTMLResponse(open('templates/result.html').read())
