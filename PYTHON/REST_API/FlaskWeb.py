from flask import Flask, url_for, request, json
from flask import Response
from flask import jsonify
from functools import wraps

'''test https://segmentfault.com/a/1190000005642670'''

app = Flask(__name__)

'''open log
@app.route('/hello', methods = ['GET'])
def api_hello():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')

    return "check your logs\n"
'''
import logging
file_handler = logging.FileHandler('D:\\app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/hellolog', methods = ['GET'])
def api_hellolog():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')

    return "check your logs\n"

'''open authenticate'''


def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/secrets')
@requires_auth
def api_helloauth():
    return "Shhh this is top secret spy stuff!"

'''
Flask RESTful API
'''


@app.route('/')
def api_root():
    app.logger.info('api_root called')
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    app.logger.info('api_article called')
    return 'You are reading ' + articleid

@app.route('/hello')
def api_hello():
    app.logger.info('api_hello called')
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    app.logger.info('api_echo called')
    if request.method == 'GET':
        return "ECHO: GET\n"
    elif request.method == 'POST':
        return "ECHO: POST\n"
    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"
    elif request.method == 'PUT':
        return "ECHO: PUT\n"
    elif request.method == 'DELETE':
        return "ECHO: DELETE"

@app.route('/messages', methods = ['POST'])
def api_message():
    app.logger.info('api_message called')
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

@app.route('/helloworld', methods = ['GET'])
def api_helloworld():
    app.logger.info('api_helloworld called')
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    #resp = Response(js, status=200, mimetype='application/json')
    #resp.headers['Link'] = 'http://luisrei.com'
    resp = jsonify(data)
    resp.status_code = 200
    return resp



@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'john', '2':'steve', '3':'bill'}

    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()

if __name__ == '__main__':
    app.run(debug=True)
