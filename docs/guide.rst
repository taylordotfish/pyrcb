.. Copyright (C) 2015-2016 taylor.fish <contact@taylor.fish>

.. This file is part of pyrcb-docs, documentation for pyrcb.
   pyrcb-docs is licensed under the following two licenses:

.. 1. The GNU Lesser General Public License as published by the Free
   Software Foundation, either version 3 of the License, or (at your
   option) any later version.

.. 2. The GNU Free Documentation License, Version 1.3 or any later
   version published by the Free Software Foundation; with no
   Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.

.. pyrcb-docs is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU Lesser General Public License for more details.

.. You should have received a copy of the GNU Lesser General Public
   License and the GNU Free Documentation License along with
   pyrcb-docs.  If not, see <http://www.gnu.org/licenses/>.

.. currentmodule:: pyrcb

Guide
=====

.. note::

   pyrcb bots are subclasses of `IRCBot`. They handle events by overriding
   methods such as :meth:`~IRCBot.on_message` or :meth:`~IRCBot.on_join`, and
   they send messages and commands by calling methods such as
   :meth:`~IRCBot.send` or :meth:`~IRCBot.join`.

   Throughout pyrcb, all parameters and attributes that represent nicknames or
   channels are case-insensitive strings (type `IStr`). This means that
   equality comparisons with those parameters are case-insensitive, so you
   don't have to call :meth:`~str.lower` on them first.

   Case-insensitive strings abide by `IRC case rules`_, which state that
   ``{}|^`` are lowercase equivalents of ``[]\~``. See `IStr` for more info.

   .. _IRC case rules: https://tools.ietf.org/html/rfc2812#section-2.2

If you haven't installed pyrcb yet, read :doc:`installation` first.

Begin by importing `IRCBot` from ``pyrcb``::

    from pyrcb import IRCBot

pyrcb bots are classes which inherit from `IRCBot`:

.. code-block:: python

   class MyBot(IRCBot):

pyrcb bots respond to actions by overriding events. Let's override
:meth:`~IRCBot.on_message` to handle messages:

.. code-block:: python

   class MyBot(IRCBot):
       def on_message(self, message, nickname, channel, is_query):

When this bot receives a message in a channel or private query,
:meth:`~IRCBot.on_message` will be called. Let's have the bot repeat whatever
someone says::

    def on_message(self, message, nickname, channel, is_query):
        if is_query:
            self.send(nickname, "You said: " + message)
        else:
            self.send(channel, nickname + " said: " + message)

``is_query`` is whether or not the message is in a private query. ``channel``
is the channel the message is in. If in a private query, this is `None`.
``nickname`` is the nickname of the user who sent the message.
:meth:`~IRCBot.send` sends a message to a channel or user.

Let's handle another event::

    def on_join(self, nickname, channel):
        if nickname != self.nickname:
            self.send(channel, nickname + " has joined " + channel)

Whenever someone joins a channel, our bot will send the message "<nickname> has
joined <channel>", except if our bot is the one that joined the channel.

To run our bot, let's create a main method and create an instance::

    def main():
        bot = MyBot()

We'll call :meth:`~IRCBot.connect` to connect to an IRC server, and
:meth:`~IRCBot.register` to register with the server. Calling these two methods
is required. ::

    bot.connect("<ip-or-hostname>", 6667)
    bot.register("mybot")

Then we'll call :meth:`~IRCBot.join` to join a channel::

    bot.join("#mybot")

Finally, we have to call :meth:`~IRCBot.listen`, which reads data from the
server and calls the appropriate events. This method will block until
connection to the server is lost. ::

    bot.listen()

All that's left is to call the main method::

    if __name__ == "__main__":
        main()

Our finished bot now looks like this::

    from pyrcb import IRCBot

    class MyBot(IRCBot):
        def on_message(self, message, nickname, channel, is_query):
            if is_query:
                self.send(nickname, "You said: " + message)
            else:
                self.send(channel, nickname + " said: " + message)

        def on_join(self, nickname, channel):
            if nickname != self.nickname:
                self.send(channel, nickname + " has joined " + channel)


    def main():
        bot = MyBot()
        bot.connect("<ip-or-hostname>", 6667)
        bot.register("mybot")
        bot.join("#mybot")
        bot.listen()

    if __name__ == "__main__":
        main()

If we run our bot, it will work like this in channels::

    [#mybot] --> mybot has joined #mybot
    [#mybot] --> user1234 has joined #mybot
    [#mybot] <mybot> user1234 has joined #mybot
    [#mybot] <user1234> Test message
    [#mybot] <mybot> user1234 said: Test message

And it will work like this in private queries::

    [query] <user1234> Test message
    [query] <mybot> You said: Test message

:doc:`reference` includes a complete list of all the methods, events, and
attributes you can use in pyrcb bots. Take a look at the `examples`_ as well.

.. _examples: https://github.com/taylordotfish/pyrcb/tree/master/examples
