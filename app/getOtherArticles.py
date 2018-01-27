from googleapiclient.discovery import build
import pprint

service = build("customsearch", "v1",
                developerKey="AIzaSyCPL0cwFkubZ5vTkFOWmH81SbWWjRryLTI")

def getOtherArticles(query):
    """Using google search API, returns json"""
    result = service.cse().list(q=query,
                         cx='007132195453603093421:pxo7dgmvtho',
                         siteSearch='https://www.mirror.co.uk/news/').execute()
    pprint.pprint(result)
    return(result)
