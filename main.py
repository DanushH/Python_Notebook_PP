import PySimpleGUI as sg
from pathlib import Path

sg.theme("DarkBlack")

menu_layout = [
    ["File", ["Open", "Save", "---", "Exit"]],
    ["Tools", ["Word Count"]]
]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("", key="-DOC_NAME-")],
    [sg.Multiline(key="-DOCUMENT-", no_scrollbar=True, size=(50,30))]
]

window = sg.Window("Notebook", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Open":
        file_path = sg.popup_get_file("Open", no_window=True)
        if file_path:
            file = Path(file_path)
            window["-DOCUMENT-"].update(file.read_text())
            window["-DOC_NAME-"].update(file_path.split('/')[-1])

    if event == "Save":
        file_path = sg.popup_get_file("Save as", no_window=True, save_as=True) + ".txt"
        file = Path(file_path)
        file.write_text(values["-DOCUMENT-"])
        window["-DOC_NAME-"].update(file_path.split('/')[-1])

    if event == "Word Count":
        full_text = values["-DOCUMENT-"]
        cleaned_text = full_text.replace('\n', ' ').split(' ')
        char_count = len(''.join(cleaned_text))
        word_count = 0 if char_count == 0 else len(cleaned_text)
        sg.popup(f"Words: {word_count} \nCharacters: {char_count}")

    if event == "Exit":
        window.close()


window.close()

