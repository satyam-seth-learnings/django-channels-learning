# Topic - Chat App with Static Group Name
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket Conncted...', event)
        print('Channel Layer...', self.channel_layer) # get default channel layer from a projet 
        print('Channel Name...', self.channel_name) # get channel name
        # by default group_add() is aysnc method and we are using it in SyncConsumer so that we must have to change this method from async to sync
        # self.channel_layer.group_add('programmers', self.channel_name)
        # Add channel to a new or existing group 
        async_to_sync(self.channel_layer.group_add)(
            'programmers', # group name
             self.channel_name
        )
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self, event):
        # print('Message Recieved Form Client...', event)
        print('Message Recieved Form Client...', event['text'])
        print('Type of Message Recieved Form Client...', type(event['text']))
        # by default group_send() is aysnc method and we are using it in SyncConsumer so that we must have to change this method from async to sync
        # self.channel_layer.group_send('programmers', {'type':'chat.message','message': event['text']})
        async_to_sync(self.channel_layer.group_send)(
            'programmers',
            {
                'type':'chat.message',
                'message': event['text']
            }
        )

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
        print('Channel Layer...', self.channel_layer) # get default channel layer from a projet 
        print('Channel Name...', self.channel_name) # get channel name
        # by default group_discard() is aysnc method and we are using it in SyncConsumer so that we must have to change this method from async to sync
        # self.channel_layer.group_discard('programmers', self.channel_name)
        # Discard channel from a new or existing group 
        async_to_sync(self.channel_layer.group_discard)(
            'programmers', # group name
             self.channel_name
        )
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket Conncted...', event)
        print('Channel Layer...', self.channel_layer) # get default channel layer from a projet 
        print('Channel Name...', self.channel_name) # get channel name
        # Add channel to a new or existing group 
        await self.channel_layer.group_add(
            'programmers', # group name
             self.channel_name
        )
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        # print('Message Recieved Form Client...', event)
        print('Message Recieved Form Client...', event['text'])
        print('Type of Message Recieved Form Client...', type(event['text']))
        await self.channel_layer.group_send(
            'programmers',
            {
                'type':'chat.message',
                'message': event['text']
            }
        )

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
        print('Channel Layer...', self.channel_layer) # get default channel layer from a projet 
        print('Channel Name...', self.channel_name) # get channel name
        # Discard channel from a new or existing group 
        await self.channel_layer.group_discard(
            'programmers', # group name
             self.channel_name
        )
        raise StopConsumer()
