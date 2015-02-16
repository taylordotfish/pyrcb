# pyrcb
`pyrcb` is a very simple library for Python IRC bots. It isn't a full implementation of IRC; it provides just enough to write IRC bots.

To use it, import `pyrcb` and create a class that inherits `IrcBot`. Override one or more of the events. (You will most likely want to call `send()` from within the events.) Create an instance of your class and call `connect()`, `register()`, optionally `join()`, and `listen()`. See `example.py` for an example.

`IrcBot`'s constructor takes one optional argument, `debug_print`. Setting this value to `True` will cause all communication with the IRC server to be printed to standard output.

### Events
`on_join(self, nickname, channel)`  
Called when a user joins a channel.
  
`on_part(self, nickname, channel)`  
Called when a user leaves a channel.
  
`on_quit(self, nickname)`  
Called when a user quits.
  
`on_message(self, nickname, target, is_query)`  
Called when a message is received.
`target` is who/what the bot should reply to. If the message is in a channel, `target` is the channel. If the message is in a private query, `target` is the other user.

### Methods
`connect(hostname, port)`  
Connects to the specified `hostname` and `port`.

`register(nickname)`  
Sends the IRC server nickname and user information.

`join(channel)`  
Joins the specified channel.

`part(channel)`  
Leaves the specified channel.

`quit()`  
Closes connection to the IRC server.

`send(target, message)`  
Sends `target` the specified message. `target` can be a channel or user.

`listen()`  
Listens for incoming messages, calling events when appropriate. This method is blocking and returns when connection to the IRC server is lost.
