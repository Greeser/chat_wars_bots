import time
import telethon.sync
from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import asyncio
import datetime
import random
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

quests=["🌲Лес", "🍄Болото","⛰️Долина"]

event_quests = ["🍂Лихолесье", "🧟‍♀Мёртвые Топи", "🌋Лощина Дьявола"]

pet = "/pet"
pet_game = "⚽️Поиграть"
pet_clean = "🛁Почистить"

castle_defense = "🛡Защита"

@client.on(events.NewMessage(incoming=True))
async def _(event):
    if event.is_private:
        bot_message = event.message.message
        if event.message.from_id == chatwars_bot_id:
            if bot_message and bot_message.find(string_to_react) != -1:
                await asyncio.sleep(5)
                msg = await client.send_message(event.message.from_id, answer)
                await asyncio.sleep(10)
                msg = await client.send_message(event.message.from_id, castle_defense)
            elif bot_message and bot_message.find(test_string_to_react) != -1:
                msg = await client.send_message(event.message.from_id, "Bot is alive")

async def main():
    await client.start(phone, password)
    
    dialogs = await client.get_dialogs()
    
    while(True):
        t_start = datetime.datetime.now()
        print("Begin questing", t_start)
        for k in range(9):
            msg = await client.send_message(chatwars_bot_id, random.choice(quests))
            await asyncio.sleep(8*60+30)

        msg = await client.send_message(chatwars_bot_id, pet_game)
        await asyncio.sleep(10)
        msg = await client.send_message(chatwars_bot_id, pet_clean)
        
        t_end = datetime.datetime.now()
        t_delta = 410*60 -  (t_end - t_start).seconds
        
        print("Waiting for battle", t_delta)
        await asyncio.sleep(t_delta)
        
        msg = await client.send_message(chatwars_bot_id, castle_defense)
	print("Stand in def", datetime.datetime.now())
	await asyncio.sleep(70*60)
    
    print(time.asctime(), '-', 'Auto-replying...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
