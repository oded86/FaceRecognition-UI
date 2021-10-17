from flask import Flask
from flask import render_template
from flask import json
import shutil
import time
import http.client
import urllib.parse

app = Flask(__name__)


@app.route('/simulate')
def simulate():
    data = {"status": "simulation is running"}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    for i in range(15):
        src = f"static/video/hallway{i}.jpg"
        shutil.copyfile(src, "static/security_images/hallway.jpg")
        time.sleep(2)

    return response


@app.route('/compareHallway')
def compare():
    conn = http.client.HTTPSConnection("face-verification2.p.rapidapi.com")
    src1 = "https://www.20il.co.il/wp-content/uploads/2020/08/F190227NIFF03-1536x1060.jpg"
    src2 = "https://www.20il.co.il/wp-content/uploads/2020/08/F190227NIFF03-1536x1060.jpg?d=s"
   # payload = 'linkFile1=' + urllib.parse.quote(src1) + '&linkFile=' + urllib.parse.quote(src2)
    payload = "linkFile1=https%3A%2F%2Fincontrol-sys.com%2FFaceRecognition%2Fimages%2Fhallway.jpg&linkFile2=https%3A%2F%2Fincontrol-sys.com%2FFaceRecognition%2Fprisoners%2Fitzik.jpg"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "face-verification2.p.rapidapi.com",
        'x-rapidapi-key': "819885f2cbmsh33f70033e6d2050p1aff94jsn27a9c2299f59"
    }

    conn.request("POST", "/faceverification", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Security Webcams')


app.run(port=81)
