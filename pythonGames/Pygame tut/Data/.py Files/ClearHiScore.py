def mainLoop():
    import pickle as pkl
    import PySimpleGUI as sg

    layout = [
        [sg.Text('Confirm Deletion of save file')],
        [sg.Button("Confirm", key = '-CONFIRM-'),sg.Button('Deny', key='-DENY-')]]

    window = sg.Window("Confirm Deletion of Save File",layout)

    while True:
       event, values = window.read()
       if event == quit:
          break
       if event == '-CONFIRM-':
          pkl.dump(0, open('Data/hiScore.txt', 'wb'))
          window.close()
          return (0,0,0)
       else:
          break
    window.close()