from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEKORJguwR4VsN1PCqbNh82LgABstqGU2EAAjMCAAK8hthX2HwTiIOxnxofBA")
    await message.reply_text(
        f"""hai 👋🏻, nama saya zonix bot, saya dapat memutar lagu di voice chat group anda.

➠ Tekan tombol panduan menggunakan bot di bawah jika ingin mengetahui bagaimana cara menggunakan saya.

➠ Tambahkan juga [zonix asst](htttps://t.me/zonix_asst) ke dalam grup jika anda ingin menambahkan saya ke grup anda.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner Ig", url="https://instagram.com/zekiloil/")
                  ],[
                    InlineKeyboardButton(
                        "panduan singkat", url="https://telegra.ph/aaksnsn-06-06"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel Bucin", url="https://t.me/randfeels"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ zonix music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner Ig", url="https://instagram.com/zekiloi/")
                ]
            ]
        )
   )


