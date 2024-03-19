import asyncio
from time import sleep
from asyncio import WindowsSelectorEventLoopPolicy
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import UserStatus
from database.orm import AsyncORM, UsersORM

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())


api_id = 25432811
api_hash = "76ccba0da25c56fec0667084db89b6e6"
bot_token = '7010537585:AAF2CSFLvrVFCJo_SD3l_V4Ush3g5p0XTvg'


app = Client(name='my_account', api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters=filters.private)
async def bot_response(client, message: Message,):
        print(message.date)
        user_id = int(message.from_user.id)
        created_at = str(message.date)
        status = "Alive"
        status_updated_at = str(message.date)
        await AsyncORM.insert_user(user_id, created_at, status, status_updated_at)

@app.on_message(filters=filters.private)
async def bot_response2(client, message: Message,):
        print(message.date)
        user_id = int(message.from_user.id)
        created_at = str(message.date)
        status = "Dead"
        status_updated_at = str(message.date)
        await AsyncORM.update_user(user_id, created_at, status, status_updated_at)


@app.on_message(filters=filters.private)
async def update_user_status(client, message: Message,):
    print(message.date)
    user_id = int(message.from_user.id)
    status_updated_at = str(message.date)
    await AsyncORM.update_user(user_id, status_updated_at)



@app.on_message(filters=filters.private)
async def message_text(client, message: Message, UserStatus):
    status = int(message.from_user.id)
    if status == "Active":
        sleep(1)
        await message.reply('Какой-то текст1')
    elif status == "Active":
        sleep(2)
        await message.reply('Какой-то текст2')
    elif status == "Active":
        sleep(3)
        await message.reply('Какой-то текст3')
    else:
        return

@app.on_message(filters=filters.private)
async def check_message(client, message: Message,):
    if "прекрасно" in message.text.lower():
        await message.from_user('message.date')
        exit()
    elif "ожидать" in message.text.lower():
        await message.from_user('message.date')
        exit()


while True:
    try:
        @bot_respose
        @update_user_status
        @message_text
        @check_message
        @bot_response2
    else:
    exit()


app.run()

