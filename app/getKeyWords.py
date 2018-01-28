def getKeyWords(entities, numDesired = 3):
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

    return(str)
