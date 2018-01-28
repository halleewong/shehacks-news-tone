# -*- coding: ascii -*-
from flask import Flask, redirect, render_template, request
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import pprint
import unicodedata

# human written functions
from getKeyWords import *
from getOtherArticles import *
from binScores import *
import ArticlesTables

app = Flask(__name__)

@app.route('/')
def homepage():
    # Return a Jinja2 HTML template and pass in image_entities as a parameter.
    return render_template('base.html')

@app.route('/analytics', methods=['GET', 'POST'])
def get_analytics():

    if request.method == 'POST':
        text = request.form['text']

        # Create a Cloud Natural Language client.
        client = language.LanguageServiceClient()

        # Retrieve inputs and create document object
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

        for cx in [cx_foxnews, cx_nyt, cx_cnn, cx_wapo, cx_new_yorker, cx_google_news, cx_econ, cx_nbc, cx_abc, cx_cbs]: # note cx_... are defined in getOtherArticles
            # get search results
            results = getOtherArticles(query, cx_key = cx)

            for i in range(3):
                topresult = getSingleArticle(results, index=i)

                if 'snippet' in topresult:
                    temp = topresult['snippet']
                    #temp = unicodedata.normalize('NFKD',temp).encode('ascii','ignore')
                    document = language.types.Document(content=temp, type=enums.Document.Type.PLAIN_TEXT)

                    # get sentiment score
                    score = client.analyze_sentiment(document=document).document_sentiment.score
                    topresult['sentiment_score'] = score

                    # save info
                    sentiment_scores.append(score)
                    other_articles.append(topresult)

        # bin the sentiment scores for pie chart
        numbers_for_pie = binScores(sentiment_scores)

        # sort the dictionary of articles by score
        other_articles_sorted = sorted(other_articles, key=lambda k: k['sentiment_score'])

        table = ArticlesTables.get_articles_table(other_articles_sorted)

        return render_template('analytics.html',
                                query = ", ".join(query.split()),
                                numbers_for_pie = numbers_for_pie,
                                other_articles_sorted = other_articles_sorted,
                                table = table,
                                text=text, # text from user
                                sentiment=sentiment # the sentiment of the text from user
                                )
    else:
        return render_template('base.html')


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
