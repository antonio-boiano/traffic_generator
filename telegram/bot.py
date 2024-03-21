from pyrogram import Client, filters
import time
import random

api_id = 123456 # Insert your API ID
api_hash = '' # Insert your API Hash
bot_token = '' # Insert your bot token

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.private)
async def hello(client, message):
    while True:
        await message.reply("Hello from the telegram bot!")
        time.sleep(random.randint(1, 10))


app.run()