from websocket_server import WebsocketHandler, WebsocketError


class MyWebsocketHandler(WebsocketHandler):
    def _setup_handlers(self):
        # In this method, add handlers for each of the types of messages that we support
        self._add_handler("/example1", self.on_example1)
        self._add_handler("/example2", self.on_example2)
        self._add_handler("/example3", self.on_example3)

    def on_example1(self, args):
        # args is a dict with unicode keys and values (it's been converted from JSON)
        # Do something, then return a result dict (if you want)
        return {
            "argument_back": ("You said %s" % args[u"value"])
        }

    def on_example2(self, args):
        # This example always raises a WebsocketError with a specific error code
        raise WebsocketError(1200, "We don't like this...")

    def on_example3(self, args):
        # This one just doesn't care about returning a result
        # It just executes an action basically
        pass


def test():
    handler = MyWebsocketHandler()

    # 15001 is the port to run the websocket server on
    handler.start(port=15001)

    # This only needs to be run when being run from command line
    handler.wait_until_keyboard_interrupt()


test()
