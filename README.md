# YouTube Chat Plays

This program fascilitates Twitch Plays-style livestreams on YouTube.

I am not currently updating this project, but the basic functionality is there

## Description
When you select an input map and pass an active stream's 11-digit code (found in the url) into the program, it will read chat messages from that stream and send key presses to your active window. Which chat inputs are bound to which key presses are determined by the input map you select.

All valid inputs will be displayed in the window to the side and can be saved if you give the log file a name before the program quits (otherwise they're not saved).

Chat can only press the keys you allow them to, with each key press happening sequentially (so no hotkeys or anything)
The connection to chat will be cut once the ytcp.exe window is closed.

## Usage
- Run ytcp.exe
- Choose an input map
- Paste the stream's 11-digit code (found in the url; https://www.youtube.com/watch?v=**abcdEFGH123**,  https://studio.youtube.com/video/**abcdEFGH123**/livestreaming, etc)
- (Optional) Give a name to the text file you want to save a record of the inputs in
- Click "Run"
- Click the button again to quit and close the program. This doesn't affect the stream or game in any way, besides stopping the keyboard inputs

## Limitations
- The stream you're trying to read inputs from must be currently live
- The keyphrase has to be the entire chat, otherwise it is ignored (i.e. "go up" won't do anything but "up" will)
- The key presses are sent to the active window, so make sure you're tabbed in to the program you want chat to control
- Only keyboard inputs can made (i.e. no mouse or controller inputs)
- For now, the only default mappings are for mGBA and snes9x, but you can easily add a JSON dictionary file to the Control Layouts folder for whatever program you choose. See the existing layouts for examples, it's really easy to make. The format is {"chat input": "key output"}. Chat inputs are case INsensitive.

## Possible Improvements
- make more json maps 
- allow for managing controls through gui
- only work in desired app/exe (get active window)

## Acknowledgements
I want to thank to [pytchat](https://github.com/taizan-hokuto/pytchat/wiki/PytchatCore), [pydirectinput](https://github.com/learncodebygaming/pydirectinput), and all the other libraries I used, as well as
[StreamersVsChat](https://youtu.be/uE_3RRBz3CQ) for their video that helped me get started with this project!

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
