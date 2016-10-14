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

.. module:: pyrcb

Reference
=========

IRCBot
------

.. autoclass:: IRCBot

IRC commands
~~~~~~~~~~~~

.. seealso::

   To learn how to send custom IRC commands, see :doc:`custom-commands`.

.. automethod:: IRCBot.password
.. automethod:: IRCBot.register
.. automethod:: IRCBot.join
.. automethod:: IRCBot.part
.. automethod:: IRCBot.quit
.. automethod:: IRCBot.send
.. automethod:: IRCBot.send_notice
.. automethod:: IRCBot.nick
.. automethod:: IRCBot.names
.. automethod:: IRCBot.send_raw

Other methods
~~~~~~~~~~~~~

.. automethod:: IRCBot.connect
.. automethod:: IRCBot.start_thread
.. automethod:: IRCBot.listen
.. automethod:: IRCBot.listen_async
.. automethod:: IRCBot.wait
.. automethod:: IRCBot.register_event
.. automethod:: IRCBot.safe_message_length
.. automethod:: IRCBot.split_string

Events
~~~~~~

.. seealso::

   To learn how to handle custom IRC commands, see :doc:`custom-commands`.

.. note::

   In events, all parameters that represent nicknames or channels are
   case-insensitive strings (type `IStr`). This means that equality comparisons
   with those parameters are case-insensitive, so you don't have to call
   :meth:`~str.lower` on them first.

   Nicknames which represent the user a command originated from are of type
   `Nickname`, a subclass of `IStr`. This means they have two additional
   attributes: ``username`` and ``hostname``. See individual methods'
   descriptions for more information.

   Case-insensitive strings abide by `IRC case rules`_, which state that
   ``{}|^`` are lowercase equivalents of ``[]\~``. See `IStr` for more info.

   .. _IRC case rules: https://tools.ietf.org/html/rfc2812#section-2.2

.. automethod:: IRCBot.on_join
.. automethod:: IRCBot.on_part
.. automethod:: IRCBot.on_quit
.. automethod:: IRCBot.on_kick
.. automethod:: IRCBot.on_message
.. automethod:: IRCBot.on_notice
.. automethod:: IRCBot.on_nick
.. automethod:: IRCBot.on_names
.. automethod:: IRCBot.on_raw

Attributes
~~~~~~~~~~

`IRCBot` instances have the following attributes. These should not be changed,
except for ones under :ref:`delay-options`.

.. attribute:: IRCBot.hostname

   The hostname of the IRC server this bot is connected to.

   :type: `str`

.. attribute:: IRCBot.port

   The port of the IRC server this bot is connected to.

   :type: `int`

.. attribute:: IRCBot.alive

   Whether or not this bot is connected to an IRC server.

   For infinite loops, use ``while IRCBot.alive`` instead of ``while True``,
   so the loop stops when the bot loses connection. Use :meth:`IRCBot.wait()`
   instead of :func:`time.sleep` as well.

   :type: `bool`

.. attribute:: IRCBot.is_registered

   Whether or not this bot has registered with the IRC server.

   :type: `bool`

.. attribute:: IRCBot.nickname

   The nickname of this bot (case-insensitive).

   :type: `IStr`

.. attribute:: IRCBot.channels

   A list of channels this bot is in (case-insensitive). Channels are of type
   :class:`IStr`.

   :type: `list` of `IStr`

.. attribute:: IRCBot.nicklist

   A dictionary which maps channel names to collections of the nicknames of
   users in those channels.

   For example::

      >>> list(bot.nicklist["#channel-name"])
      [IStr('nickname1'), IStr('nickname2'), IStr('nickname3')]

   Keys are case-insensitive, as are the nicknames retrieved from the a
   dictionary lookup. If there is no collection of nicknames for a particular
   channel, a dictionary lookup will return an empty collection instead of
   producing an error.

   The items retrieved from dictionary lookups are actually dictionaries
   themselves: each nicklist is an `IDefaultDict` instance that maps a nickname
   to a `VoiceOpInfo` object. These objects behave just like normal `IStr`
   nicknames, but have two additional attributes: `~VoiceOpInfo.is_voiced` and
   `~VoiceOpInfo.is_op`.

   However, you can still iterate over these dictionaries like lists or sets.
   ``for nickname in bot.nicklist["#channel"]:`` will iterate over the keys in
   the dictionary, which are normal `IStr` nicknames. ::

      >>> bot.nicklist["#test-channel"]
      IDefaultDict([(IStr('nickname'), VoiceOpInfo('nickname'))])
      >>> nickname = bot.nicklist["#test-channel"]["nickname"]
      >>> nickname
      VoiceOpInfo('nickname')
      >>> nickname.is_voiced
      True
      >>> nickname.is_op
      False

   :type: `IDefaultDict`; maps `str` to `IDefaultDict`

.. _delay-options:

Delay options
^^^^^^^^^^^^^

The following instance attributes are related to the ``delay`` parameter of
`IRCBot`'s constructor. These may be changed.

.. attribute:: IRCBot.delay_multiplier

   Multiplied by the number of consecutive messages sent to determine how many
   seconds to wait before sending the next one. (Default: 0.1)

   :type: `float`

.. attribute:: IRCBot.max_delay

   The maximum number of seconds to wait before sending a message. (Default:
   1.5)

   :type: `float`

.. attribute:: IRCBot.consecutive_timeout

   How many seconds must pass before a message is not considered consecutive.
   (Default: 5)

   :type: `float`

IStr
----

.. autoclass:: IStr()

IDefaultDict
------------

.. autoclass:: IDefaultDict
   :show-inheritance:

ISet
----

.. autoclass:: ISet
   :show-inheritance:

UserHostInfo
------------

.. autoclass:: UserHostInfo(\*args, username, hostname, \*\*kwargs)
   :show-inheritance:

   .. attribute:: UserHostInfo.username

      The user's username (not to be confused with the user's nickname). This
      attribute may be ``None`` if unknown.

      :type: `str`

   .. attribute:: UserHostInfo.hostname

      The user's hostname. This attribute may be ``None`` if unknown.

      :type: `str`

VoiceOpInfo
-----------

.. autoclass:: VoiceOpInfo(\*args, is_voiced, is_op, \*\*kwargs)
   :show-inheritance:

   .. attribute:: is_voiced

      Whether or not the user is voiced.

      :type: `bool`

   .. attribute:: is_op

      Whether or not the user is a channel operator.

      :type: `bool`
