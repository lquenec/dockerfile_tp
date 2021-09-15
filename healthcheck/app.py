from flask import Flask
from flask import request
from datetime import datetime
app = Flask(__name__)
calls=[]
@app.route('/')
def index():
    return 'Call count : <ul><li>{}</li></ul>'.format('</li><li>'.join(calls))
@app.route('/health')
def health():
    global calls
    dt = datetime.now()
    calls.append("from {} at {}".format(request.remote_addr, dt.strftime("%H:%M:%S")))
    return 'OK' , 500
if __name__ == '__main__':
    app.run(host="0.0.0.0")
