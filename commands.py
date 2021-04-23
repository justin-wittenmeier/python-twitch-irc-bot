import logging, cardsNdice, random

class Commands():
    def __init__(self):
        self.__target_message=None
        self.__target_user=None
        self.__command_char="!" # This must be added before the command for execution to occur.
        self.__commands={} # Commands are parsed by adding "_command" after the name of the command.
        self.__outgoing=None
        for i in [i for i in dir(Commands) if "_command" in i]:
            self.__commands[f'{self.__command_char}{i.replace("_command", "")}']=f"self.{i}()"

    # Roll d20
    def roll_command(self):
        d20=cardsNdice.Dice(d_num=20)
        return f"@{self.__target_user} rolled a d20 and got {d20.value}."

    # Toss a coin    
    def toss_command(self):
        coin=cardsNdice.Coin()
        return f"@{self.__target_user} flipped a coin and got {coin.value}."

    # Shake magic 8 ball.
    def magic8_command(self):
        outcomes = ['Try again later.','Positive.','Negative.','The odds are good.','The odds are bad.','The future is hard to see right now try again later.','It is certain.','We can not know.','Never.','Maybe.','Yes.','No.']
        return f"@{self.__target_user} {random.choice(outcomes)}"

    # Checks chat message for command and returns False if unable to find a command.
    def command(self, msg):
        self.__target_message=msg.message
        self.__target_user=msg.user
        try:
            return eval(self.__commands[msg.message.split(" ")[0]])
        except Exception:
            return False

if __name__=="__main__":
    class Message:
        def __init__(self):
            self.user="test_user"
            self.message="!roll"

    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%D %T", level=logging.INFO)
    command=Commands()
    logging.info(command.command(Message()))
