# Topic - Consumer

from channels.consumer import SyncConsumer, AsyncConsumer


class MySyncConsumer(SyncConsumer):
    # This handler is called when client initially opens a  connection and is about to finish the Websocket handshake.
    def websocket_connect(self, event):
        print('Websocket Connected...')

    # This handler is called when data received from client.
    def websocket_receive(self, event):
        print('Websocket Received...')

    # This handler is called when either caonnection to the client is lost, either from the client closing the connection, the server closing the connection or loss of the socket.
    def websocket_disconnect(self, event):
        print('Websocket Disconnected...')


class MyAsyncConsumer(AsyncConsumer):
    # This handler is called when client initially opens a  connection and is about to finish the Websocket handshake.
    async def websocket_connect(self, event):
        print('Websocket Connected...')

    # This handler is called when data received from client.
    async def websocket_receive(self, event):
        print('Websocket Received...')

    # This handler is called when either caonnection to the client is lost, either from the client closing the connection, the server closing the connection or loss of the socket.
    async def websocket_disconnect(self, event):
        print('Websocket Disconnected...')
