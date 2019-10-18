from websocket_server import WebsocketHandler

class MyWebsocketHandler(WebsocketHandler):
	def _setup_handlers(self):
		# In this method, add handlers for each of the types of messages that we support
		self._add_handler("/example1", self.on_example1)
		self._add_handler("/example2", self.on_example2)

	def on_example1(self, args):
		# Do something, then return a result
		return {
			"argument_back": ("You said %s" % args[u"value"])
		}

	def on_example2(self, args):
		# This example always raises an Exception
		raise Exception("We don't like this...")

def test():
	handler = MyWebsocketHandler()

	# 15001 is the port to run the websocket server on
	handler.start(port = 15001)

	# This only needs to be run when being run from command line
	handler.wait_until_keyboard_interrupt()

test()
