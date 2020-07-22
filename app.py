from inshorts_api import get_news
from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key = "do we really need it!"


@app.route("/", defaults={'category': 'latest'})
@app.route('/<path:category>', methods=['GET'])
def news(category):
    return jsonify(get_news(category))


if __name__ == "__main__":
    app.run(threaded=True)
