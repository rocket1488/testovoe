from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, StreamingResponse
from starlette.templating import Jinja2Templates
from jinja2 import Template
from io import BytesIO

import converter
from models import Body, Data
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
    if not prices:
        return {"status_code": status.HTTP_204_NO_CONTENT, "body": "something went wrong"}
    html = Template(open('templates/result.html').read()).render(
        currencies=prices
    )
    #return HTMLResponse(html)
    return prices


@app.post("/get_csv")
async def get_csv(data: Data):
    csv_file = converter.json2csv(data.data)
    return StreamingResponse(BytesIO(csv_file))


@app.post("/get_xls")
async def get_xls(data: Data):
    xls_file = converter.json2csv(data.data)
    return StreamingResponse(BytesIO(xls_file))


@app.post("/get_pdf")
async def get_pdf(data: Data):
    pdf_file = converter.json2pdf(data.data)
    return StreamingResponse(BytesIO(pdf_file))

