from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, UnknownEvent, LiveEndEvent, DisconnectEvent
from TikTokLive.types.errors import FailedParseUserHTML
from setting import tiktok_username

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id=tiktok_username)


# Unknown types
@client.on("unknown")
async def on_connect(event: UnknownEvent):
    print(f"Event Type: {event.type}")
    print(f"Event Base64: {event.base64}")

# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
    print("Disconnected")

# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")
    
# Live end
@client.on("live_end")
async def on_connect(event: LiveEndEvent):
    print(f"Livestream ended :(")


# Define handling an event via a "callback"
client.add_listener("comment", on_comment)


if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    try:
        client.run()
    except:
        print('Mia is not connect yet', end="")
        client.stop()
        