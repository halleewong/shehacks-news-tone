
def binScores(lst):
    """
    Takes a list of scores, each score is between -1,1
    Returns a list: [<number positive>,<number neutral>,<number neg>]
    """
    posCount = 0
    neutralCount = 0
    negCount = 0

    for num in lst:
        if num <= -0.1:
            negCount += 1
        elif num > -0.1 and num < 0.1:
            neutralCount += 1
        else:
            posCount += 1

    return([posCount,neutralCount,negCount])

if __name__ == '__main__':
    print(binScores([-0.5,0,0.5]))
    print(binScores([-0.5,-0.5,0,0.5]))
