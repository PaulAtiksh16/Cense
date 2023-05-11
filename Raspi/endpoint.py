from flask import Flask, jsonify
from sensors import counter

app = Flask(__name__)

@app.route('/counter')
def get_counter():
    return jsonify({'counter': counter})

if __name__ == '__main__':
    app.run(debug=True)
