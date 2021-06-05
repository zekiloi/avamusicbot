from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEKORJguwR4VsN1PCqbNh82LgABstqGU2EAAjMCAAK8hthX2HwTiIOxnxofBA")
    await message.reply_text(
        f"""hai 👋🏻, nama saya ava music bot, saya dapat memutar lagu di voice chat group anda.

➠ Tekan tombol panduan menggunakan bot di bawah jika ingin mengetahui bagaimana cara menggunakan saya.

➠ Tambahkan juga [ava asisstant](htttps://t.me/avaasisstant) ke dalam grup jika anda ingin menambahkan saya ke grup anda.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Panduan Menggunakan Bot", url="https://telegra.ph/ava-command-list-05-27")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group Support", url="https://t.me/gcsupportbots"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel Support", url="https://t.me/levinachannel"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 Kirim Donasi", url="https://t.me/dlwrml"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ ava music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌺 Channel Support", url="https://t.me/levinachannel")
                ]
            ]
        )
   )


