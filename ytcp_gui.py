import PySimpleGUI as sg
import yt_chat_plays_gui as ytcp
import json, threading, pytchat, pydirectinput

#to do:
# make more json maps 
# make read me
# allow for managing controls through gui
# only work in desired app/exe (get active window)

all_inputs = []
id_tooltip = "Please input your 11-digit stream id, found in the link to the stream\n\nFor example, the 'dQw4w9WgXcQ' part of:\n    (copied from url) https://www.youtube.com/watch?v=dQw4w9WgXcQ\n    (copied from share button) https://youtu.be/dQw4w9WgXcQ"
json_tooltip = "Select an option that corresponds to a .JSON file with mappings for your controls. \nEach key will be what chat types (case insensitive) and the corresponding value will be the keyboard press.\nFor example, if you choose mgba, if chat types 'up', the game reads the 'w' key"
in_tooltip = "If you want to save a text file of all the inputs made, type a name for the file. \nOtherwise, leave it blank and no file will be created"

settings = sg.UserSettings('config.json', convert_bools_and_none=True, path=".")

def validate_start(values: list):
    if not values["map"]:
        sg.popup_annoying("Please choose a layout for the inputs you want to let chat make", line_width=80)
        return False
    elif not values["id"]:
        sg.popup_annoying("Please type your stream id.", line_width=80)
        return False
    elif len(values["id"]) != 11:
        l = len(values["id"])
        sg.popup_annoying(f"Your stream id needs to be 11 digits (its current size is {l})", line_width=80)
        return False
    #elif not values["emu"]:
        # sg.popup_annoying("Please choose an .exe file for the game or emulator you are running", line_width=80)
        #return False

    return True

def main_gui ():

    sg.theme('LightGreen6')

    layout = [[
                sg.Col([#[sg.Text("Path to emulator's exe file: ", size=(16,1)), sg.In(key="emu", size=(20, 1), enable_events=True), sg.FileBrowse(file_types=(('EXE Files', "*.exe"),))],
                [sg.Text("* Input mappings: ", size=(16,1), tooltip=json_tooltip), sg.Combo(values=list(settings["layouts"].keys()), key="map", size=(20, 1), default_value=settings['default_template'], enable_events=True)],
                [sg.Text("* 11-digit stream id: ", size=(16,1), tooltip=id_tooltip), sg.In(key="id", size=(20, 1), enable_events=True), sg.Submit(visible=False, bind_return_key=True)],
                [sg.Text("Name of input log file: ", size=(16,1), tooltip=in_tooltip), sg.In("", key="save", size=(20, 1), enable_events=True), sg.Submit(visible=False, bind_return_key=True), sg.T(".txt")],
                [sg.Button("Run", border_width=0, expand_x=True)]]),
                sg.Col([[sg.Multiline(size=(10,6), autoscroll=True, auto_refresh=True, reroute_stdout=True, no_scrollbar=True, disabled=True)]])
                
            ]]

    window = sg.Window(title="yt Chat Plays", layout=layout,  alpha_channel=0.9)

    running = False
    while True:
        event, values = window.read()
        
        if event in ("exit", sg.WIN_CLOSED):
            break

        elif event == "Run":
            if running: ytcp.stop(values["save"])

            elif not validate_start(values): continue
            try:
                with open(settings["layouts"][values['map']]) as f:
                    data = f.read()
                    js = json.loads(data)
                thread = threading.Thread(target=ytcp.start, args=(js, pytchat.create(values["id"])), daemon=True)
                #main loop
                window["Run"].update("Running... Clicking again will quit program")
                thread.start()
                running = True
            except Exception as e:
                sg.popup_annoying(f"Something went wrong. Please review the values you inputted and try again.\nError: {e}", line_width=80)

        elif event == "map":
            settings['default_template'] = values['map']

    window.close()

if __name__ == "__main__":
    main_gui()
