import time
import telethon.sync
from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import asyncio
import datetime

import argparse

# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own
api_id = ##
api_hash = ''##

# fill in your own details here
phone = ''##
username = ''##
password = 'YOUR_PASSWORD'  # if you have two-step verification enabled

chatwars_bot_id = 265204902
chatwars_helper_id = 615010125

# content of the automatic reply
answer = "/go"
string_to_react = "/go"
test_string_to_react = "/shop"


client = TelegramClient(username, api_id, api_hash)

target_quest = "🍄Болото"

@client.on(events.NewMessage(incoming=True))
async def _(event):
    if event.is_private:
        bot_message = event.message.message
        if event.message.from_id == chatwars_bot_id:
            if bot_message and bot_message.find(string_to_react) != -1:
                await asyncio.sleep(5)
                msg = await client.send_message(event.message.from_id, answer)
            elif bot_message and bot_message.find(test_string_to_react) != -1: 
                msg = await client.send_message(event.message.from_id, "Bot is alive")

async def main(n):
    await client.start(phone, password)
    
    dialogs = await client.get_dialogs()
    
    while(True):
        t_start = datetime.datetime.now()
        print(t_start)
        for k in range(5):
            msg = await client.send_message(chatwars_bot_id, target_quest)
            await asyncio.sleep(8*60+30)
        
        print("Sleep between quests 25")
        await asyncio.sleep(260*60)

        for k in range(3):
            msg = await client.send_message(chatwars_bot_id, target_quest)
            await asyncio.sleep(8*60+30)
        t_end = datetime.datetime.now()
        t_delta = 480*60 -  (t_end - t_start).seconds
        
        print("Sleep for ", t_delta)
        await asyncio.sleep(t_delta)
    
    print(time.asctime(), '-', 'Auto-replying...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="number of quests", type=int)
    args = parser.parse_args()
    if args.number:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(args.number))
    else:
        print("No args passed")
