import telebot
from telebot import types
import datetime

TOKEN = "TOKEN"
CHAT_ID = "CHAT_ID"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'sticker', 'photo', 'audio', 'video', 'document', 'animation'])
def handle_message(message):
    user_name = get_user_name(message)
    user_id = message.from_user.id
    date = message.date
    formatted_date = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')

    if message.text:
        text = message.text
        bot.send_message(
            CHAT_ID,
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время: {formatted_date}"  
        )
    elif message.sticker:
        text = "Стикер"
        bot.send_message(
            CHAT_ID,
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время: {formatted_date}"  
        )
        bot.send_sticker(CHAT_ID, message.sticker.file_id)
    elif message.photo:
        text = "Фото"
        bot.send_message(
            CHAT_ID,
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время: {formatted_date}"  
        )
        bot.send_photo(CHAT_ID, message.photo[0].file_id)
    elif message.audio:
        text = "Аудио"
        bot.send_message(
            CHAT_ID,
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время: {formatted_date}"  
        )
        bot.send_audio(CHAT_ID, message.audio.file_id)
    elif message.video:
        text = "Видео"
        bot.send_message(
            CHAT_ID,
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время: {formatted_date}"  
        )
        bot.send_video(CHAT_ID, message.video.file_id)
    elif message.document:
        text = "Документ"
        bot.send_message(
            CHAT_ID,
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время: {formatted_date}"  
        )
        bot.send_document(CHAT_ID, message.document.file_id)
    elif message.animation:
        text = "GIF"
        bot.send_message(
            CHAT_ID,
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время: {formatted_date}"  
        )
        bot.send_animation(CHAT_ID, message.animation.file_id)
    else:
        text = "Неизвестный тип"

@bot.edited_message_handler(content_types=['text', 'sticker', 'photo', 'audio', 'video', 'document', 'animation'])
def handle_edited_message(message):
    user_name = get_user_name(message)
    user_id = message.from_user.id
    date = message.edit_date
    formatted_date = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')

    if message.text:
        text = message.text
        bot.send_message(
            CHAT_ID,
            f"Измененное сообщение:\n"
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время изменения: {formatted_date}"  
        )
    elif message.sticker:
        text = "Стикер"
        bot.send_message(
            CHAT_ID,
            f"Измененный стикер:\n"
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время изменения: {formatted_date}"  
        )
        bot.send_sticker(CHAT_ID, message.sticker.file_id)
    elif message.photo:
        text = "Фото"
        bot.send_message(
            CHAT_ID,
            f"Измененное фото:\n"
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время изменения: {formatted_date}"  
        )
        bot.send_photo(CHAT_ID, message.photo[0].file_id)
    elif message.animation:
        text = "GIF"
        bot.send_message(
            CHAT_ID,
            f"Измененный GIF:\n"
            f"Имя: {user_name}\n"
            f"ID: {user_id}\n"
            f"Сообщение: {text}\n" 
            f"Время изменения: {formatted_date}"  
        )
        bot.send_animation(CHAT_ID, message.animation.file_id)
    # Обработка измененных сообщений для других типов

def get_user_name(message):
    user = message.from_user
    if user.first_name:
        if user.last_name:
            return f"{user.first_name} {user.last_name}"
        return user.first_name
    return "Анонимный пользователь"

bot.polling()
