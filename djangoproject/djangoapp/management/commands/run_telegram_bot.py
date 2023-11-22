from django.core.management.base import BaseCommand
import telebot
from djangoapp.models import Product

bot = telebot.TeleBot("6641758955:AAG0Gtq0-5FAttlE3bwLsCQImPCNLkZ_6jQ")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['products'])
def products(message):
    products = Product.objects.all()
    for product in products:
        bot.send_message(message.chat.id, f"{product.name} - {product.price}")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Список доступных команд:\n/products - Показать список товаров\n/add <название_товара> <цена> - Добавить товар")

@bot.message_handler(commands=['add'])
def add_product(message):
    try:
        command, *args = message.text.split()  # Разделяем команду и аргументы
        if len(args) != 2:
            bot.send_message(message.chat.id, "Неверный формат. Используйте: /add <название_товара> <цена>")
        else:
            product_name, product_price = args
            new_product = Product(name=product_name, price=product_price)
            new_product.save()
            bot.send_message(message.chat.id, f"Товар '{product_name}' добавлен успешно.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
