from flask import Flask, redirect, render_template, request
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from getKeyWords import *
import pprint
from googleapiclient.discovery import build

app = Flask(__name__)
service = build("customsearch", "v1",
                    developerKey="AIzaSyCPL0cwFkubZ5vTkFOWmH81SbWWjRryLTI")
@app.route('/')
def homepage():
    # Return a Jinja2 HTML template and pass in image_entities as a parameter.
    return render_template('homepage.html')

@app.route('/run_language', methods=['GET', 'POST'])
def run_language():
    # Create a Cloud Natural Language client.
    client = language.LanguageServiceClient()

    # Retrieve inputs and create document object
    text = request.form['text']
    document = language.types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

    # Retrieve response from Natural Language's analyze_entities() method
    response = client.analyze_entities(document=document)
    entities = response.entities

    # Retrieve response from Natural Language's analyze_sentiment() method
    response = client.analyze_sentiment(document=document)
    sentiment = response.document_sentiment
    
    query = getKeyWords(entities, numDesired=3)

    other_articles = service.cse().list(q=query,
                             cx='007132195453603093421:pxo7dgmvtho',
                             siteSearch='https://www.mirror.co.uk/news/').execute()
    #pprint.pprint(other_articles)

    return render_template('../index.html', text=text, sentiment=sentiment, other=other_articles)

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
