from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Amme, I love you! - Maadhav"


@app.route('/acrobot', methods=['POST'])
def slash():
    print(request)
    return jsonify({
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Wonder what ** means?"
                }
            }
        ]
    })


if __name__ == '__main__':
    app.run()
