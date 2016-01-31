.. Copyright (C) 2016 taylor.fish <contact@taylor.fish>

.. This file is part of pyrcb-docs, documentation for pyrcb.

.. pyrcb-docs is free software: you can redistribute it and/or modify
   it under the terms of the GNU Lesser General Public License as
   published by the Free Software Foundation, either version 3 of the
   License, or (at your option) any later version.

.. pyrcb-docs is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU Lesser General Public License for more details.

.. You should have received a copy of the GNU Lesser General Public License
   along with pyrcb-docs.  If not, see <http://www.gnu.org/licenses/>.

.. currentmodule:: pyrcb

Custom commands
===============

This document will cover how to send and handle IRC commands that don't have
dedicated methods or event handlers.


Sending
-------

To send custom IRC commands, use :meth:`IRCBot.send_raw`. For example, to send
an ``INVITE`` command, you would call::

    mybot.send_raw("INVITE", ["<nickname>", "<channel>"])

You may find it useful to create methods for custom commands;
for example::

    class MyBot(IRCBot):
        def invite(self, nickname, channel):
            self.send_raw("INVITE", [nickname, channel])


Handling
--------

To handle custom IRC commands, define the event in your bot class and then call
:meth:`IRCBot.register_event` in your ``__init__`` method. To handle ``INVITE``
messages, for example, you would write something like this::

    class MyBot(IRCBot):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.register_event(self.on_invite, "INVITE")

        def on_invite(self, nickname, channel):
            # In custom event handlers, only the nickname parameter is of
            # type IStr. Other parameters must be converted manually.
            channel = IStr(channel)
            print(nickname, "has invited this bot to", channel)

As stated in the example above, in custom event handlers, only the first
parameter (usually the nickname of the user the command originated from) is of
type `IStr` (i.e. case-insensitive). All other parameters that represent
nicknames or channels should be converted to IStr. See
:meth:`IRCBot.register_event` for more information.
