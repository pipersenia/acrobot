from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Amme, I love you! - Maadhav"


@app.route('/acrobot', methods=['POST'])
def slash():
    return jsonify({
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "A message *with some bold text* and _some italicized text_."
                }
            }
        ]
    })


if __name__ == '__main__':
    app.run()
