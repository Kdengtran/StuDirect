from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():

    text = str(request.args.get('input'))
    text = text.upper()

    def format_to_json(text):

        data = {'input': text}
        return json.dumps(data)

    return format_to_json(text)