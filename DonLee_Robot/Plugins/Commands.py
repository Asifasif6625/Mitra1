# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG
# (e) @Muhammed_RK, @Mo_Tech_YT , @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee_Robot/blob/main/LICENSE

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from DonLee_Robot import Translation, LOGGER # pylint: disable=import-error
from DonLee_Robot.Database import Database # pylint: disable=import-error
from DonLee_Robot.donlee_robot import DonLee_Robot

db = Database()

@DonLee_Robot.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/mo_tech_YT"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('𝑴𝒚 𝒅𝒆𝒗 🧒', url='https://t.me/malayalamvibead'),
        InlineKeyboardButton('𝑺𝒐𝒖𝒓𝒄𝒆 𝑪𝒐𝒅𝒆 🧾', url ='https://github.com/Asifasif6625/Mitra')
    ],[
        InlineKeyboardButton('🛠 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 🛠', url='https://t.me/viberepo')
    ],[
        InlineKeyboardButton('⚙ 𝑯𝒆𝒍𝒑 ⚙', callback_data="help")
        InlineKeyboardButton(' 𝑫𝒆𝒑𝒍𝒐𝒚 𝒊𝒎𝒈🖼️', url='https://telegra.ph/file/92688f5694ff8d115b663.jpg') 
    ]] 
   
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@DonLee_Robot.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('𝑯𝒐𝒎𝒆 🏡', callback_data='start'),
        InlineKeyboardButton('𝑨𝒃𝒐𝒖𝒕 🤨', callback_data='about')
    ],[
        InlineKeyboardButton('𝑪𝒍𝒐𝒔𝒆 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@DonLee_Robot.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('𝑯𝒐𝒎𝒆 🏡', callback_data='start'),
        InlineKeyboardButton('𝑪𝒍𝒐𝒔𝒆 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
