from flask import Flask, redirect, render_template, request
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from getKeyWords import *
from getOtherArticles import *
import pprint

app = Flask(__name__)

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
    sentiment = response.document_sentiment.score #sentiment score of input text

    # assembly query for custom google searches
    query = getKeyWords(entities, numDesired=3)

    other_articles = list()
    sentiment_scores = list()

    for cx in [cx_foxnews, cx_nyt]: # note cx_... are defined in getOtherArticles
        # get search results
        results = getOtherArticles(query, cx_key = )
        topresult = getSingleArticle(results, index=0)

        # get sentiment score
        score = client.analyze_sentiment(document=topresult['snippet']).document_sentiment.score

        # save info
        sentiment_scores.append(score)
        other_articles.append(topresult)

    #pprint.pprint(other_articles)

    return render_template('../index.html', text=text,
                                            sentiment=sentiment,
                                            other_articles=other_articles
                                            sentiment_scores=sentiment_scores)

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
