# YouTube Chat Plays

This program fascilitates Twitch Plays-style livestreams on YouTube.

I don't know how much/if this project will be updated, but it does the minimum of what it sets out to do.

## Description
When you select an input map and pass an active stream's 11-digit code (found in the url) into the program, it will read chat messages from that stream and send key presses to your active window. Which chat inputs are bound to which key presses are determined by the input map you select.

All valid inputs will be displayed in the window to the side and can be saved if you give the log file a name before the program quits (otherwise they're not saved).

Chat can only press the keys you allow them to, with each key press happening sequentially (so no hotkeys or anything)
The connection to chat will be cut once the ytcp.exe window is closed.

## Usage
- Run ytcp.exe
- Choose an input map
- Paste the stream's 11-digit code (found in the url; https://www.youtube.com/watch?v=**sfC6ey0MYGY**,  https://studio.youtube.com/video/**sfC6ey0MYGY**/livestreaming, etc)
- (Optional) Give a name to the text file you want to save a record of the inputs in
- Click "Run"
- Click the button again to quit and close the program. This doesn't affect the stream or game in any way, besides stopping the keyboard inputs

## Limitations
- The stream you're trying to read inputs from must be currently live
- The keyphrase has to be the entire chat, otherwise it is ignored (i.e. "go up" won't do anything but "up" will)
- The key presses are sent to the active window, so make sure you're tabbed in to the program you want chat to control
- Only keyboard inputs can made (i.e. no mouse or controller inputs)
- For now, the only default mappings are for mGBA and snes9x, but you can easily add a JSON dictionary file to the Control Layouts folder for whatever program you choose. See the existing layouts for examples, it's really easy to make. The format is {"chat input": "key output"}. Chat inputs are case INsensitive.

## To-do/Nice to haves
- make more json maps 
- allow for managing controls through gui
- only work in desired app/exe (get active window)

## Acknowledgements
I want to thank to [pytchat](https://github.com/taizan-hokuto/pytchat/wiki/PytchatCore), [pydirectinput](https://github.com/learncodebygaming/pydirectinput), and all the other libraries I used, as well as
[StreamersVsChat](https://youtu.be/uE_3RRBz3CQ) for their video that helped me get started with this project!

## Contributing

If you make an input map that you think would be helpful, feel free to make a request to add it to the templates folder.

Pull requests welcome on the off chance someone wants to add/improve anything.

Please reach out if you know a simple way to send JoyKey/Controller outputs with Python! It would be a big QoL change. 

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
