.. Copyright (C) 2015 taylor.fish (https://github.com/taylordotfish)

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

1.7.0
-----

* Added ``channels`` parameter, a list of channels the user was in, to
  :meth:`~IRCBot.on_quit`. The function signature is now:

  .. method:: IRCBot.on_quit(nickname, message, channels):
     :noindex:

* Fixed an issue where `IRCBot.nicklist` wouldn't update properly.
