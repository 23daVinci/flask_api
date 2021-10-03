from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name = "Naman")

@app.route('/api')
def api():
    return jsonify(message = "This is from API!")

@app.route('/not_found')
def not_found():
    return jsonify(message = "Not found"), 404


if __name__ == '__main__':
    app.run()