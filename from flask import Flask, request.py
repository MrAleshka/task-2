from flask import Flask, request

app = Flask(__name__)

@app.route('/item/<string:name>', methods=['GET'])
def get_item(name):
    return {'item': name}, 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
