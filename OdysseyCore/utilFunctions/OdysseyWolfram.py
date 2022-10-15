import wolframalpha
import logging


class OdysseyWolfram:
    def __init__(self, APPID):
        self.APPID = APPID
        self.client = wolframalpha.Client(APPID)

    def queryForResult(self, search):
        answer = ""
        try:
            result = self.client.query(search)
            answer = next(result.results).text

        except Exception as e:
            logging.exception(e)
            return "E^^EXCEPTION|Could not find"

        return answer

