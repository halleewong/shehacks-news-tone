from googleapiclient.discovery import build
import pprint

dkey_hallee ="AIzaSyCPL0cwFkubZ5vTkFOWmH81SbWWjRryLTI"
cx_foxnews = '004259363863783706405:p0jsn9xte3u'
cx_nyt = '004259363863783706405:phem9rfvts8'


cx_cynth = '007132195453603093421:pxo7dgmvtho'
dkey_cynth = "AIzaSyCPL0cwFkubZ5vTkFOWmH81SbWWjRryLTI"


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
            d['title'] = articles['items'][index]['title']
            d['snippet'] = articles['items'][index]['snippet']
            d['link'] = articles['items'][index]['link']
    return d

if __name__ == '__main__':
    temp = getOtherArticles('bitcoin capital markets', cx_key=cx_foxnews)
    print getSingleArticle(temp,index=0)

    temp2 = getOtherArticles('bitcoin', cx_key=cx_nyt)
    t = getSingleArticle(temp2,index=0)
    print t

    print t['snippet']
