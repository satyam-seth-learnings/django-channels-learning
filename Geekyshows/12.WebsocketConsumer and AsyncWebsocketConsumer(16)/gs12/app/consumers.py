# Topic - Generic Consumer - WebsocketConsumer and AsyncWebsoacketConsumer
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class MyWebsocketConsumer(WebsocketConsumer):
    # This handler is called when client initially opens a connectin and is about to finish the websocket handshake.
    def connect(self):
        print('Websocket Connected...')
        self.accept()  # To accept the connection
        # self.close()  # To reject the connection

    # This handler is called when data received from client
    def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...', text_data)
        # To send Data to Client
        self.send(text_data='Message from Server to Client')
        # self.send(bytes_data=data) # To Send Binary Frame to Client
        # self.close()  # To force-close the connection
        # self.close(code=4123)  # To Add a custom websocket error code

    # This handler is called when either connectionto the client is lost, either from client closing the connection, the server closing the connection, or loss of the socket
    def close(self, close_code):
        print('Websocket Disconnected...', close_code)


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    # This handler is called when client initially opens a connectin and is about to finish the websocket handshake.
    async def connect(self):
        print('Websocket Connected...')
        await self.accept()  # To accept the connection
        # await self.close()  # To reject the connection

    # This handler is called when data received from client
    async def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...', text_data)
        # To send Data to Client
        await self.send(text_data='Message from Server to Client')
        # self.send(bytes_data=data) # To Send Binary Frame to Client
        # await self.close()  # To force-close the connection
        # self.close(code=4123)  # To Add a custom websocket error code

    # This handler is called when either connectionto the client is lost, either from client closing the connection, the server closing the connection, or loss of the socket
    def close(self, close_code):
        print('Websocket Disconnected...', close_code)
