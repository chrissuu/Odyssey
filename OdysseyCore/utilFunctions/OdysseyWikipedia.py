import wikipedia


def queryForSuggestions(search):
    result = wikipedia.search(search)
    return result


def queryForSummary(search, numSentences):
    result = wikipedia.summary(search, numSentences)
    return result


def queryForPage(search):
    result = wikipedia.page(search)
    return result


class OdysseyWikipedia:
    def __init__(self):
        pass
