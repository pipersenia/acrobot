from flask import Flask, jsonify, request

app = Flask(__name__)

acronyms = {
    'INT': 'Inter Milan',
    'ASR': 'AS Roma'
}


@app.route('/')
def hello():
    return "Amme, I love you! - Maadhav"


@app.route('/acrobot', methods=['POST'])
def slash():
    # add token validation
    print("Received request")
    print(request.form)
    text = request.form.get('text', None)
    if text is None:
        return "You didn't ask for any term!"

    terms = text.split()
    if 'help' in terms[0]:
        return jsonify({
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "`/acrobot define <acronym>`\n"
                                "`/acrobot add <acronym> <definition> <url>"
                    }
                }
            ]
        })
    # last term is the acronym
    acronym = text.split()[-1]
    if acronym in acronyms:
        definition = acronyms[acronym]
    else:
        definition = "Unable to look up meaning for this acronym. <Help message for adding>"
    return jsonify({
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":thinking_face: *{acronym}*".format(acronym=acronym)
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": ":rocket: {definition}".format(definition=definition),
                    "emoji": True
                }
            }
        ]
    }
    )


if __name__ == '__main__':
    app.run()
