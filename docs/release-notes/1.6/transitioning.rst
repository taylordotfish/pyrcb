.. Copyright (C) 2015 taylor.fish <contact@taylor.fish>

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

Transitioning from older versions
=================================

This version of pyrcb includes many changes, so here's what you need to do to
update existing bots using an older version of pyrcb (before version 1.6).

Changes
-------

IrcBot renamed
~~~~~~~~~~~~~~

The class ``IrcBot`` has been renamed to `IRCBot`.

on_message() and on_notice() parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``target`` parameter in :meth:`~IRCBot.on_message` and
:meth:`~IRCBot.on_notice` has been replaced with ``channel``. The function
signatures are now:

.. method:: IRCBot.on_message(message, nickname, channel, is_query)
   :noindex:

.. method:: IRCBot.on_notice(message, nickname, channel, is_query)
   :noindex:

``channel`` will be `None` if the message is in a private query. You can use
``channel or nickname`` as a replacement for ``target``.

is_self removed
~~~~~~~~~~~~~~~

The ``is_self`` parameter has been removed from events. Use ``self.nickname ==
nickname`` instead (or ``self.nickname == target`` for
:meth:`~IRCBot.on_kick()`)

on_kick() parameters
~~~~~~~~~~~~~~~~~~~~

In addition to the removal of ``is_self``, ``message`` as been added as a
parameter of :meth:`~IRCBot.on_kick()`. The function signature is now:

.. method:: IRCBot.on_kick(nickname, channel, target, message)
   :noindex:

is_alive() removed
~~~~~~~~~~~~~~~~~~

``is_alive()`` has been removed. Use the attribute :attr:`~IRCBot.alive`
instead.

send_raw() parameters
~~~~~~~~~~~~~~~~~~~~~

:meth:`~IRCBot.send_raw()` now takes two parameters: an IRC command and a list
of arguments to the command.

on_other() changes
~~~~~~~~~~~~~~~~~~

``on_other()`` has been renamed to :meth:`~IRCBot.on_raw()`. It is also now
called for every IRC message, not only ones without a specific event.

async_events removed
~~~~~~~~~~~~~~~~~~~~

The ``async_events`` parameter in :meth:`~IRCBot.listen` and
:meth:`~IRCBot.listen_async` has been removed. For events which must start long
operations, run those operations on a separate thread.
