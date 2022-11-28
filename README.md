#YouTube Chat Plays
This program fascilitates Twitch Plays-style livestreams on YouTube. 
When you pass an active stream's 11-digit code (found in the url) into the program, it will read inputs from chat and send key presses to your active window.

All valid inputs will be displayed in the window and can be saved if you give the log file a name before the program quits(otherwise they're not saved).

Which chat inputs are bound to which keypress outputs are determined by the input map you select. For now, the only default mappings are for mGBA and snes9x, but you can easily add a JSON dictionary file to the Control Layouts folder for whatever program you choose. See the existing layouts for examples, it's really easy to make. The format is {"chat input": "key output"}.
Chat inputs are case INsensitive.

Chat can only press the keys you allow them to, with each key press happening sequentially (so no hotkeys or anything)
The connection to chat will be cut once the ytcp.exe window is closed.
