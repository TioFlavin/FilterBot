import random 
from pyrogram import Client as FilterBot, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from configs import BOT_PICS, StartTxT, HelpTxT, AboutTxT, LOGGER
from FilterBot.database import db

@FilterBot.on_message(filters.private & filters.command("start"))
async def startCMD(client: FilterBot, message: Message):

    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.first_name, message.from_user.id)

    bot = await client.get_me()
    keyboard = [[
      InlineKeyboardButton('Adicione-me ao seu bate-papo', url=f"https://t.me/{bot.username}?startgroup=true")
      ],[
      InlineKeyboardButton('Ajuda', callback_data='main#help'),
      InlineKeyboardButton('Sobre', callback_data='main#about')
      ],[
      InlineKeyboardButton('Atualizaçao', url='t.me/FlixGoOficial'),
      InlineKeyboardButton('Support', url='t.me/TioFlixBROff')
      ]]

    if "motech" == BOT_PICS[0]:
        await message.reply_text(text=StartTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await message.reply_photo(photo=random.choice(BOT_PICS), caption=StartTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))



@FilterBot.on_message(filters.private & filters.command("help"))
async def helpCMD(client: FilterBot, message: Message):

    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.first_name, message.from_user.id)

    keyboard = [[ InlineKeyboardButton('Home', callback_data='main#start'),
                  InlineKeyboardButton('Close', callback_data='main#close') ]]

    if "motech" == BOT_PICS[0]:
        await message.reply_text(text=HelpTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await message.reply_photo(photo=random.choice(BOT_PICS), caption=HelpTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))

@FilterBot.on_message(filters.private & filters.command("about"))
async def aboutCMD(client: FilterBot, message: Message):

    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.first_name, message.from_user.id)

    keyboard = [[ InlineKeyboardButton('Tutorial', url='https://youtube.com/@TioFlixBR')],
                [ InlineKeyboardButton('Volta', callback_data='main#start'),
                  InlineKeyboardButton('Ajuda', callback_data='main#help') ]]

    if "motech" == BOT_PICS[0]:
        await message.reply_text(text=AboutTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await message.reply_photo(photo=random.choice(BOT_PICS), caption=AboutTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))


@FilterBot.on_callback_query(filters.regex('main'))
async def maincallback(client: FilterBot, message):

    try:
        x, type = message.data.split("#")
    except:
        await message.answer("Erorrrr....")
        await message.message.delete()
        return

    if type == "start":
        bot = await client.get_me()
        keyboard = [[ InlineKeyboardButton('Adicione-me ao seu bate-papo', url=f"t.me/{bot.username}?startgroup=true") ],
                    [ InlineKeyboardButton('ajuda', callback_data='main#help'),
                      InlineKeyboardButton('sobrw', callback_data='main#about') ],
                    [ InlineKeyboardButton('atualizaçao', url='t.me/FlixGoOficial'),
                      InlineKeyboardButton('Support', url='t.me/TioFlixBROff') ]]
        await message.message.edit(text=StartTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard), disable_web_page_preview=True)

    elif type == "help":
        keyboard = [[ InlineKeyboardButton('voltar', callback_data='main#start'),
                      InlineKeyboardButton('Close', callback_data='main#close') ]]
        await message.message.edit(text=HelpTxT, reply_markup=InlineKeyboardMarkup(keyboard), disable_web_page_preview=True)

    elif type == "about":
        keyboard = [[ InlineKeyboardButton('Canal YouTube', url='https://youtube.com/@TioFlixBR')],
                    [ InlineKeyboardButton('Home', callback_data='main#start'),
                      InlineKeyboardButton('Help', callback_data='main#help') ]]
        await message.message.edit(text=AboutTxT, reply_markup=InlineKeyboardMarkup(keyboard), disable_web_page_preview=True)
