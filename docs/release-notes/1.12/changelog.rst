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

Changelog
=========

.. _changelog-1.12.0:

1.12.0
------

* Added :meth:`IRCBot.start_thread`, which starts a function on a separate
  thread. This should be used instead of :meth:`~IRCBot.listen_async`.
* Deprecated :meth:`IRCBot.listen_async`. Instead of running the bot in the
  background, start threads with :meth:`~IRCBot.start_thread` and call
  `~IRCBot.listen` on the main thread.
* Fixed possible errors when closing sockets.
