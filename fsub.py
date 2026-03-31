import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "23828737"
CHANNEL = "https://t.me/medianikmathbot"

bot = telebot.TeleBot(8669955676:AAHh-7YyqA51wxxaFfD_ocHDYtiOk5O93uQ)

def cek_sub(user_id):
    try:
        status = bot.get_chat_member(CHANNEL, user_id)
        return status.status in ["member", "administrator", "creator"]
    except:
        return False

@bot.message_handler(commands=['start'])
def start(msg):
    user_id = msg.from_user.id

    if cek_sub(user_id):
        bot.send_message(msg.chat.id, "✅ Akses diterima, welcome!")
    else:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL[1:]}"))
        markup.add(InlineKeyboardButton("Sudah Join", callback_data="cek"))

        bot.send_message(msg.chat.id, "❌ Harus join dulu!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "cek")
def cek_lagi(call):
    if cek_sub(call.from_user.id):
        bot.edit_message_text("✅ Akses diterima!", call.message.chat.id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, "Masih belum join!", show_alert=True)

bot.infinity_polling()
