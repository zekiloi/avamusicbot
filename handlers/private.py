from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAADBQADKAIAAmQgIVd2e584kTrkUgI")
    await message.reply_text(
        f"""**Hai 👋🏻, I am {bn} 🎵

I can play music in your group's voice call. Developed by [Hendra](https://t.me/IamYourEnemy).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎛 Commands", url="https://telegra.ph/Sujandra-Musik-04-24")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/VcgSupportGroup"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Kutipankataaa"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 Donasi", url="https://t.me/IamYourEnemy"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Sujandra Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Follow Instagram 🌻", url="https://instagram.com/hendraputraaaaaa")
                ]
            ]
        )
   )


