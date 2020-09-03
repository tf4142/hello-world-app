'''
    A simple Hello! http site that also provide some health info
'''

from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime

app = Flask(__name__)

# for http://localhost:8080
@app.route('/')
def index():
    return render_template('index.html')


# for http://localhost:8080/healthz
@app.route('/healthz')
def health():

    # Get app status
    ret_code = urllib.request.urlopen("http://localhost:8080").getcode()
    if ret_code == 200:
        app_status = '0K'
    else:
        app_status = 'FAILED'

    # Make request and store response
    webpage = requests.get('http://localhost:8080')

    # Parse content with html parser
    soup = BeautifulSoup(webpage.content, 'html.parser')

    # Finding all the meta tag for version, store in list format
    meta_tag = soup.findAll('meta', {"version" : True})

    # Only expect one version, but if there are multiple, will use last one
    for a in meta_tag:
        app_version = a.attrs['version']

    time_str = 'up since ' + dt_string
    app_health = {'status':app_status, 'version':app_version,'uptime':time_str}
    return jsonify(app_health)

# start app on port 8080
if __name__ == "__main__":
    # get current date and time
    now = datetime.now()

    # YYYY-mm-dd H:M:S
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    app.run(port=8080,debug=False)
