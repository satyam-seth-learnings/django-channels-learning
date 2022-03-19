# Topic - Generic Consumer - WebsocketConsumer and AsyncWebsoacketConsumer
# Authentication

import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from .models import Chat, Group


class MyWebsocketConsumer(WebsocketConsumer):
    # This handler is called when client initially opens a connectin and is about to finish the websocket handshake.
    def connect(self):
        print('Websocket Connected...')
        print('Channel Layer...', self.channel_layer)
        print('Channel Name...', self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print('Group Name...', self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()  # To accept the connection

    # This handler is called when data received from client
    def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...', text_data)
        data = json.loads(text_data)
        print('Data...', data)
        message = data['msg']
        group = Group.objects.get(name=self.group_name)
        if self.scope['user'].is_authenticated:
            chat = Chat(
                content=data['msg'],
                group=group
            )
            chat.save()
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'chat.message',
                    'message': message
                }
            )
        else:
            self.send(text_data=json.dumps({
                'msg': 'Login Required'
            }))

    def chat_message(self, event):
        print('Event...', event)
        self.send(text_data=json.dumps({
            'msg': event['message']
        }))

    # This handler is called when either connectionto the client is lost, either from client closing the connection, the server closing the connection, or loss of the socket

    def close(self, close_code):
        print('Websocket Disconnected...', close_code)
        print('Channel Layer...', self.channel_layer)
        print('Channel Name...', self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    # This handler is called when client initially opens a connectin and is about to finish the websocket handshake.
    async def connect(self):
        print('Websocket Connected...')
        print('Channel Layer...', self.channel_layer)
        print('Channel Name...', self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print('Group Name...', self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()  # To accept the connection

    # This handler is called when data received from client
    async def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...', text_data)
        data = json.loads(text_data)
        print('Data...', data)
        message = data['msg']
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        if self.scope['user'].is_authenticated:
            chat = Chat(
                content=data['msg'],
                group=group
            )
            await database_sync_to_async(chat.save)()
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat.message',
                    'message': message
                }
            )
        else:
            await self.send(text_data=json.dumps({
                'msg': 'Login Required'
            }))

    async def chat_message(self, event):
        print('Event...', event)
        await self.send(text_data=json.dumps({
            'msg': event['message']
        }))

    # This handler is called when either connectionto the client is lost, either from client closing the connection, the server closing the connection, or loss of the socket
    async def close(self, close_code):
        print('Websocket Disconnected...', close_code)
        print('Channel Layer...', self.channel_layer)
        print('Channel Name...', self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
