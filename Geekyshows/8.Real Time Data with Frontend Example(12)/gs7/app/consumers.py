# Topic - Web API WebSocket - JavaScript
from time import sleep
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
import asyncio
import json


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket Connected...', event)
        self.send({
            'type': 'websocket.accept',
        })

    # def websocket_receive(self, event):
    #     print('Message received from Client...', event['text'])
    #     for i in range(10):
    #         self.send({
    #             'type': 'websocket.send',
    #             'text': str(i)
    #         })
    #         sleep(1)

    def websocket_receive(self, event):
        print('Message received from Client...', event['text'])
        for i in range(10):
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({'count': i})
            })
            sleep(1)

    def websocket_disconnect(self, event):
        print('Websocket Disconnected...', event)
        raise StopConsumer


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket Connected...', event)
        await self.send({
            'type': 'websocket.accept',
        })

    # async def websocket_receive(self, event):
    #     print('Message received from Client...', event['text'])
    #     for i in range(10):
    #         await self.send({
    #             'type': 'websocket.send',
    #             'text': str(i)
    #         })
    #         await asyncio.sleep(1)

    async def websocket_receive(self, event):
        print('Message received from Client...', event['text'])
        for i in range(10):
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({'count': i})
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print('Websocket Disconnected...', event)
        raise StopConsumer
