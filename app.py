from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/api')
def api():
    return jsonify(message = "This is from API!")

@app.route('/not_found')
def not_found():
    return jsonify(message = "Not found"), 404

@app.route('/age_check')
def age_check():
    name = request.args.get('name')
    age = int(request.args.get('age'))

    if age > 18:
        return jsonify(message = "Welcome " + name)
    else:
        return jsonify(message = "Sorry " + name + " you are not old enough"), 401

if __name__ == '__main__':
    app.run()