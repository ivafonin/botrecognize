import telebot as tb
import imgtotext
token=''
bot= tb.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,f"Привет, {message.from_user.first_name}. \nОтправь мне картинку и я преобразую ее в текст. 😀 ")
@bot.message_handler(commands=['about'])
def about_message(message):
  bot.send_message(message.chat.id,f"Создал - Афонин Иван. Школа №1580")
@bot.message_handler(content_types=['photo'])
def reply(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id,"Ожидайте, Фото Обрабатывается")
    text = imgtotext.imgtxt('image.jpg')
    bot.send_message(message.chat.id,f"{text}")


bot.infinity_polling()
