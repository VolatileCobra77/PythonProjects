def mainLoop():
    import pickle as pkl
    import PySimpleGUI as sg
    hiScore = pkl.load(open("Data/hiScore.Txt", 'rb'))
    window = sg.Window("Current Hi Score",[[sg.Text(f"Current Hi Score is: {hiScore}")],[sg.Button("OK", key="-OK-")]])

    while True:
        event, values = window.read()
        if event == "-OK-":
            break
    window.close()