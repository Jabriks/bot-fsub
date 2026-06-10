import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

# Mengambil data dari Environment Variables (Langkah yang kita bahas tadi)
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# USERNAME CHANNEL YANG WAJIB DI-SUBSCRIBE (Ganti dengan channelmu tanpa @)
CHANNEL_USERNAME = "NamaChannelKamu" 

bot = Client("fsub_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    user_id = message.from_user.id
    
    try:
        # Cek apakah user sudah join channel
        await client.get_chat_member(CHANNEL_USERNAME, user_id)
        # Jika sudah join, kirim pesan ini:
        await message.reply_text(f"Halo {message.from_user.mention}! Kamu sudah subscribe. Silakan gunakan bot.")
        
    except UserNotParticipant:
        # Jika belum join, suruh join dulu:
        await message.reply_text(
            text=f"Halo {message.from_user.mention}!\n\nKamu harus bergabung ke Channel kami terlebih dahulu sebelum bisa menggunakan bot ini.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 Gabung Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
                [InlineKeyboardButton("🔄 Coba Lagi", url=f"https://t.me/{client.me.username}?start=start")]
            ])
        )

print("Bot berhasil dijalankan...")
bot.run()
