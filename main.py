import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    print(response.text)
    valutes = list(data['Valute'].values())
    date = data['Date'][:10]
    time = data['Timestamp'][11:]
    return valutes, date, time


app = Flask(__name__)


def create_html(valutes,date,time):
    text = '<h1>Мои курсы валют</h1>'
    text += f'<td> Следующая дата {date}</td>'
    text += '<div> </div>'
    text += f'<td>{time}</td>'
    text += '<table>'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes,date,time = get_valutes_list()
    html = create_html(valutes,date,time)
    return html


if __name__ == "__main__":

    app.run()
