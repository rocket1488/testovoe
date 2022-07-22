import json, os
import pandas as pd


def json2csv(data):
    data = json.loads(data)
    df = pd.DataFrame(data)
    df.to_csv('tmp.csv')
    file = open('tmp.csv', 'rb').read()
    os.remove('tmp.csv')
    return file
