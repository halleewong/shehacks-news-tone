
def binScores(lst):
    """
    Takes a list of scores, each score is between -1,1
    Returns a list: [<number positive>,<number neutral>,<number neg>]
    """
    posCount = 0
    neutralCount = 0
    negCount = 0

    for num in lst:
        if num <= -0.3:
            negCount += 1
        else if num > -0.3 and num < 0.3:
            neutralCount += 1
        else:
            posCount += 1

    return([posCount,neutralCount,negCount])
