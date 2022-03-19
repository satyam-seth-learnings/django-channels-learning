# Topic - Generic Consumer - WebsocketConsumer and AsyncWebsoacketConsumer
# Real-time Data Example
# Real-time Data Example with Front end

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
import asyncio


class MyWebsocketConsumer(WebsocketConsumer):
    # This handler is called when client initially opens a connectin and is about to finish the websocket handshake.
    def connect(self):
        print('Websocket Connected...')
        self.accept()  # To accept the connection

    # This handler is called when data received from client
    def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...', text_data)
        for i in range(20):
            self.send(text_data=str(i))  # To send Data to Client
            sleep(1)

    # This handler is called when either connectionto the client is lost, either from client closing the connection, the server closing the connection, or loss of the socket
    def close(self, close_code):
        print('Websocket Disconnected...', close_code)


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    # This handler is called when client initially opens a connectin and is about to finish the websocket handshake.
    async def connect(self):
        print('Websocket Connected...')
        await self.accept()  # To accept the connection

    # This handler is called when data received from client
    async def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...', text_data)
        for i in range(20):
            await self.send(text_data=str(i))  # To send Data to Client
            await asyncio.sleep(1)

    # This handler is called when either connectionto the client is lost, either from client closing the connection, the server closing the connection, or loss of the socket
    def close(self, close_code):
        print('Websocket Disconnected...', close_code)
