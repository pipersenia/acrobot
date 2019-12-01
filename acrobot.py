from flask import Flask, jsonify, request
import gsheets
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)
ACRONYMS = None

ACRONYM_KEY = 'Acronym'
DEFINITION_KEY = 'Definition'

@app.route('/')
def hello():
    return "Acrobot - expanding acronyms one word at a time."


def lookup_definition(term):
    keys = ACRONYMS.keys()
    if term in keys:
        return ACRONYMS[term]
    elif term.lower() in keys:
        return ACRONYMS[term.lower()]
    elif term.upper() in keys:
        return ACRONYMS[term.upper()]
    else:
        return None


@app.route('/acrobot', methods=['POST'])
def slash():
    # add token validation
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
    query_term = text.split()[-1]
    if ACRONYMS is None:
        fetch_acronyms()
    definition = lookup_definition(term=query_term)
    if definition is None:
        definition = "Acronym {} not found in database.".format(query_term)
    return jsonify({
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":thinking_face: *{acronym}*".format(acronym=query_term)
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


def normalize(records):
    master = {}
    for rec in records:
        master[rec[ACRONYM_KEY]] = rec[DEFINITION_KEY]
    return master


def fetch_acronyms():
    global ACRONYMS
    if ACRONYMS is None:
        db_client = gsheets.connect()
        records = gsheets.get_records(db_client)
        # normalize the list of records in sheets
        ACRONYMS = normalize(records=records)


if __name__ == '__main__':
    app.run()
