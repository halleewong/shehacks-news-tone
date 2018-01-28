from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def getKeyWords(entities, numDesired = 4):
    # parameters:
    #    entities - an entity object list  returned by google NLP API
    #    numDesired - number of entity names to return
    #                 ordered by salience (high to low)
    # returns:
    #    string with keywords joined by single space
    d = dict()

    # put entity name and salience in dictionary for sorting
    for entity in entities:
      d[str(entity.name)] = entity.salience

    string = ""
    count = 0

    # get keywords with highest salience
    for name in sorted(d, key=d.get, reverse=True):
        if count < numDesired:
            string = string + " " + name
	if count == numDesired:
	    break
        count += 1

    return(string)

if __name__ == '__main__':

    text = 'bitcoin'

    # Create a Cloud Natural Language client.
    client = language.LanguageServiceClient()

    # Retrieve inputs and create document object
    document = language.types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

    # Retrieve response from Natural Language's analyze_entities() method
    response = client.analyze_entities(document=document)
    entities = response.entities
    print(entities)
    print(getKeyWords(entities, numDesired = 3))
