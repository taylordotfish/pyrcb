from __future__ import print_function
from pyrcb import IrcBot
from datetime import datetime


class TimeBot(IrcBot):
    def on_message(self, message, nickname, target, is_query):
        if message.lower() == "!time":
            self.send(target, str(datetime.utcnow()))


def main():
    bot = TimeBot(debug_print=True)
    bot.connect("irc.freenode.net", 6667)
    bot.register("timebot")
    bot.join("##timebot-test")
    bot.listen()
    print("Disconnected from server.")


if __name__ == "__main__":
    main()
