#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging

from basegame import Ship
import credentials

sVersion = "1.0.0"


def setup(bot, update, args):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    # create a new game slot
    Ship.create_new_game(chat_id)
    bot.sendMessage(chat_id=update.message.chat_id, text="A new universe has been created...")
    # TODO send intro message of the game
    print("Game setup finished")


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    # Create the Updater and pass it your bot's token.
    updater = Updater(credentials.get_token())
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', setup, pass_args=True))
    #dispatcher.add_handler(CommandHandler('explore', explore, pass_args=True))
    #dispatcher.add_handler(CommandHandler('repair', repair, pass_args=True))
    #dispatcher.add_handler(CommandHandler('talk', talk, pass_args=True))
    #dispatcher.add_handler(CommandHandler('nothing', nothing, pass_args=True))

    # Start the Bot
    print("Creating the universe connector...\n")
    updater.start_polling()
    # to stop the bot if necessary: idle
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == "__main__":
    main()
