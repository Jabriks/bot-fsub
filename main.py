
import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

# --- KODE PANCINGAN UNTUK RENDER WEB SERVICE ---
def run_dummy_server():
    # Render mewajibkan aplikasi web mendengarkan Port yang mereka sediakan
    port = int(os.environ.get("PORT", 8080))
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(self_name := f"Dummy web server berjalan di port {port}")
    httpd.serve_forever()

# Jalankan server pancingan di latar belakang (thread terpisah)
threading.Thread(target=run_dummy_server, daemon=True).start()
# ------------------------------------------------

# --- KODE BOT TELEGRAM KAMU ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
CHANNEL_USERNAME = "NamaChannelKamu" # Ganti dengan username channelmu tanpa @

bot = Client("fsub_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    user_id = message.from_user.id
    try:
        await client.get_chat_member(CHANNEL_USERNAME, user_id)
        await message.reply_text(f"Halo {message.from_user.mention}! Kamu sudah subscribe. Silakan gunakan bot.")
    except UserNotParticipant:
        await message.reply_text(
            text=f"Halo {message.from_user.mention}!\n\nKamu harus bergabung ke Channel kami terlebih dahulu sebelum bisa menggunakan bot ini.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 Gabung Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
                [InlineKeyboardButton("🔄 Coba Lagi", url=f"https://t.me/{client.me.username}?start=start")]
            ])
        )

print("Bot fsub berhasil dijalankan...")
bot.run()
