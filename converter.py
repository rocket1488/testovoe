import json, os
from jinja2 import Template
import pandas as pd
from xhtml2pdf import pisa
from io import BytesIO


def json2csv(data):
    data = json.loads(data)
    df = pd.DataFrame(data)
    df.to_csv('tmp.csv')
    file = open('tmp.csv', 'rb').read()
    os.remove('tmp.csv')
    return file


def json2xls(data):
    data = json.loads(data)
    df = pd.DataFrame(data)
    df.to_excel('tmp.xlsx')
    file = open('tmp.xlsx', 'rb').read()
    os.remove('tmp.xlsx')
    return file


def json2pdf(data):
    data = json.loads(data)
    html = Template(open('templates/result.html').read()).render(
        currencies=data
    )
    buffer = BytesIO()
    pisa.CreatePDF(html, dest=buffer, encoding='UTF-8')
    return buffer.getvalue()

