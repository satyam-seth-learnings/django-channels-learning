# Topic - Database
import json
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from .models import Chat, Group


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket Conncted...', event)
        # get default channel layer from a projet
        print('Channel Layer...', self.channel_layer)
        print('Channel Name...', self.channel_name)  # get channel name
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print('Group Name...', self.group_name)
        # by default group_add() is aysnc method and we are using it in SyncConsumer so that we must have to change this method from async to sync
        # self.channel_layer.group_add(self.group_name, self.channel_name)
        # Add channel to a new or existing group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,  # group name
            self.channel_name
        )
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        # print('Message Recieved Form Client...', event)
        print('Message Recieved Form Client...', event['text'])
        print('Type of Message Recieved Form Client...', type(event['text']))

        data = json.loads(event['text'])
        print('Complete Data...', data)
        print('Type of Complete Data...', type(data))
        print('Chat Message...', data['msg'])
        print(self.scope['user'])

        # Find Group Object
        group = Group.objects.get(name=self.group_name)

        if self.scope['user'].is_authenticated:
            # Create New Chat Object
            chat = Chat(content=data['msg'], group=group)
            chat.save()
            data['user'] = self.scope['user'].username
            print('Data...', data)
            print('Type of Data...', type(data))

            # by default group_send() is aysnc method and we are using it in SyncConsumer so that we must have to change this method from async to sync
            # self.channel_layer.group_send(self.group_name, {'type':'chat.message','message': event['text']})
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'chat.message',
                    # 'message': event['text']
                    'message': json.dumps(data)
                }
            )
        else:
            self.send({
                'type': 'websocket.send',
                # 'text': json.dumps({'msg': 'Login Required'})
                'text': json.dumps({'msg': 'Login Required', 'user': 'guest'})
            })

    def chat_message(self, event):
        print('Event...', event)
        print('Actual Data...', event['message'])
        print('Type of Actual Data...', type(event['message']))
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        print('Websocket Disconected...', event)
        # get default channel layer from a projet
        print('Channel Layer...', self.channel_layer)
        print('Channel Name...', self.channel_name)  # get channel name
        # by default group_discard() is aysnc method and we are using it in SyncConsumer so that we must have to change this method from async to sync
        # self.channel_layer.group_discard(self.group_name, self.channel_name)
        # Discard channel from a new or existing group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,  # group name
            self.channel_name
        )
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket Conncted...', event)
        # get default channel layer from a projet
        print('Channel Layer...', self.channel_layer)
        print('Channel Name...', self.channel_name)  # get channel name
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print('Group Name...', self.group_name)
        # Add channel to a new or existing group
        await self.channel_layer.group_add(
            self.group_name,  # group name
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        # print('Message Recieved Form Client...', event)
        print('Message Recieved Form Client...', event['text'])
        print('Type of Message Recieved Form Client...', type(event['text']))

        data = json.loads(event['text'])
        print('Data...', data)
        print('Type of Data...', type(data))
        print('Chat Message...', data['msg'])
        print(self.scope['user'])

        # Find Group Object
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)

        if self.scope['user'].is_authenticated:
            # Create New Chat Object
            chat = Chat(content=data['msg'], group=group)
            await database_sync_to_async(chat.save)()

            data['user'] = self.scope['user'].username
            print('Data...', data)
            print('Type of Data...', type(data))

            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat.message',
                    # 'message': event['text']
                    'message': json.dumps(data)
                }
            )
        else:
            await self.send({
                'type': 'websocket.send',
                # 'text': json.dumps({'msg': 'Login Required'})
                'text': json.dumps({'msg': 'Login Required', 'user': 'guest'})
            })

    async def chat_message(self, event):
        print('Event...', event)
        print('Actual Data...', event['message'])
        print('Type of Actual Data...', type(event['message']))
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    async def websocket_disconnect(self, event):
        print('Websocket Disconected...', event)
        # get default channel layer from a projet
        print('Channel Layer...', self.channel_layer)
        print('Channel Name...', self.channel_name)  # get channel name
        # Discard channel from a new or existing group
        await self.channel_layer.group_discard(
            self.group_name,  # group name
            self.channel_name
        )
        raise StopConsumer()
