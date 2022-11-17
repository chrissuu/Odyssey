import plivo
from decouple import config

#Paid endpoint, may be useless
class OdysseyMessenger:
	def __init__(self, strDestinationNumber, strSenderNumber):
		self.destinationNumber = strDestinationNumber
		self.senderNumber = strSenderNumber
		self.client = plivo.RestClient(config('plivoAuthID'),config('plivoAuthToken'))

	def sendMsg(self, strMsgContent):

		response = self.client.messages.create(
			src=self.senderNumber,
			dst=self.destinationNumber,
			text=strMsgContent,)
		print(response)




