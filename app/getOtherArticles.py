from googleapiclient.discovery import build
import pprint
import unicodedata

dkey_hallee ="AIzaSyCPL0cwFkubZ5vTkFOWmH81SbWWjRryLTI"
cx_foxnews = '004259363863783706405:p0jsn9xte3u'
cx_nyt = '004259363863783706405:phem9rfvts8'

service = build("customsearch", "v1",developerKey=dkey_hallee)

def getOtherArticles(query, cx_key):
    """
    Using google search API, returns json results
    """
    result = service.cse().list(q=query,cx=cx_key).execute()
    #pprint.pprint(result)
    return result

def getSingleArticle(articles, index=0):
    """
    returns dictionary of title, text and link of a single article
    """
    d = dict()
    if 'items' in articles:
        if len(articles['items']) > index:
            d['title'] = unicodedata.normalize('NFKD',articles['items'][index]['title']).encode('ascii','ignore')
            d['snippet'] = unicodedata.normalize('NFKD',articles['items'][index]['snippet']).encode('ascii','ignore')
            d['link'] = unicodedata.normalize('NFKD',articles['items'][index]['link']).encode('ascii','ignore')
    return d



if __name__ == '__main__':
    temp = getOtherArticles('bitcoin capital markets', cx_key=cx_foxnews)
    print getSingleArticle(temp,index=0)

    temp2 = getOtherArticles('bitcoin', cx_key=cx_nyt)
    t = getSingleArticle(temp2,index=0)
    print t

    print t['snippet']
