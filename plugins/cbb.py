# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from bot import Bot
from config import OWNER_ID, OWNER
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>{OWNER}</a>\n○ Source Code : <a href='https://github.com/mondar111/File-Sharing-Man'>Klik Disini</a>\n○ Channel : @familynvn\n○ Support Group : @Siniajaloh</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗑 Close", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
