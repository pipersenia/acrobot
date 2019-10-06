from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Amme, I love you! - Maadhav"


@app.route('/acrobot', methods=['POST'])
def slash():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Wonder what *<>* means?"
            }
        }
    ]


if __name__ == '__main__':
    app.run()
