import socket, logging, os, time

class ChatBot:
    def __init__(self):
        self.__host='irc.chat.twitch.tv'
        self.__port=6667
        self.__username="SET USERNAME" # Bot username
        self.__target_channel="SET CHANNEl" # Channel to join
        self.__token=os.environ.get("OAUTH") # Get Oauth for Twitch
        self.__color = "CadetBlue"
        self.__encode="utf-8"
        self.__twitch_socket=self.__connect()
        self.send_message(f"/color {self.__color}") # Set bot color.
        self.send_message("/me Connected.") # Notify chat bot has connected

    def __connect(self):
        logging.info("opening socket...")
        t_socket=socket.socket()
        logging.info("connecting...")
        t_socket.connect((self.__host,self.__port))
        logging.info("sending token...")
        t_socket.sendall(f"PASS {self.__token}\r\n".encode(self.__encode))
        logging.info("sending username...")
        t_socket.sendall(f"NICK {self.__username}\r\n".encode(self.__encode))
        logging.info("joining room...")
        t_socket.sendall(f"JOIN #{self.__target_channel}\r\n".encode(self.__encode))
        joining=True
        while joining:
            buffer=t_socket.recv(1024).decode()
            data=buffer.splitlines()
            for i in data:
                logging.info(i)
                if "End of /NAMES list" in i:
                    joining=False
        logging.info(f"connected to {self.__target_channel}'s chat room...")
        return t_socket

    def send_message(self, msg):
        self.__twitch_socket.sendall(f"PRIVMSG #{self.__target_channel} :{msg}\r\n".encode(self.__encode))
        logging.info(f"outgoing message:{msg}")

    # Respond to ping request from twitch.
    def __ping_pong(self, msg):
        if 'PING :tmi.twitch.tv' in msg:
            logging.info("sending pong...")
            self.__twitch_socket.sendall(f"{msg.replace('PING', 'PONG')}\n".encode(self.__encode))
            return True
        return False

    # Generator for messages.
    def recv_messages(self):
        buffer=self.__twitch_socket.recv(1024).decode()
        data=buffer.splitlines()
        for message in data:
            if self.__ping_pong(message)==False:
                message=message[1:].split("!",1)
                message[1]=message[1].split(":",1)[1]
                yield self.__Message(message[0], message[1])
    
    class __Message:
        def __init__(self, user, message):
            self.user=user
            self.message=message
            
if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%D %T", level=logging.INFO)
    bot = ChatBot()
    while 1:
        data=bot.recv_messages()
        for i in data:
            logging.info(f"{i.user}:{i.message}")
        
