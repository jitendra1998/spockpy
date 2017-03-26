class Event(object):
	'''
	Event object
	'''
	NONE    = None
	ROCK    = 0
	SCISSOR = 1
	SPOCK   = 2
	PAPER   = 4
	
	def __init__(self, type_ = None):
		self.type = type_
		self.tip  = (None, None)

	def setType(self, type_):
		self.type = type_

	def setTip(self, position):
		if self.type == Event.ROCK:
			self.tip  = position
		else:
			self.tip  = (None, None)

	def get_tip(self):
		return self.tip