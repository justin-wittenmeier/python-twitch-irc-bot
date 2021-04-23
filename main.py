import logging, chat_bot, commands

def main():
    bot=chat_bot.ChatBot()
    command=commands.Commands()
    while True:
        for i in bot.recv_messages():
            if (message:=command.command(i))!=False:
                bot.send_message(message)

if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%D %T", level=logging.INFO)
    main()
