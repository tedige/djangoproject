from django.core.management.base import BaseCommand
import telebot
from djangoapp.models import User

TOKEN = "6641758955:AAG0Gtq0-5FAttlE3bwLsCQImPCNLkZ_6jQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! Welcome to the bot!")

@bot.message_handler(commands=['users'])
def show_users(message):
    users = User.objects.all()
    user_list = "\n".join([f"@{user.username}" for user in users])
    bot.send_message(message.chat.id, f"Users:\n{user_list}")

@bot.message_handler(commands=['add'])
def add_user(message):
    try:
        command, username, telegram_id = message.text.split()
        telegram_id = int(telegram_id)
        new_user = User.objects.create(username=username, telegram_id=telegram_id)
        bot.send_message(message.chat.id, f"Added user: {new_user.username}")
    except ValueError:
        bot.send_message(message.chat.id, "Invalid input! Use: /add <username> <telegram_id>")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
