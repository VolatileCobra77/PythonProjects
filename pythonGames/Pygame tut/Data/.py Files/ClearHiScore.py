import pickle as pkl
import PySimpleGUI as sg

layout = [
    [sg.Text('Confirm Deletion of save file')],
    [sg.Button("Confirm", key = '-CONFIRM-'),sg.Button('Deny', key='-DENY-')]]

window = sg.Window("Confirm Deletion of Save File",layout)

while True:
    event, values = window.read()
    if event == '-CONFIRM-':
        pkl.dump(0, open('Data/hiScore.txt', 'wb'))
        break
    else:
        break



"""
def inputManager():
    clear = input('Are You Sure?(y/n)\n').upper()

    if clear == 'Y' or clear.upper == 'YES':
        pkl.dump(0, open('Data/hiScore.txt', 'wb'))
        print('cleared!')
        return 1
    elif clear == 'N' or clear.upper == 'NO':
        return 0
    else:
        print(clear)
        print("Invalid Choice please try Again")
        return inputManager()

exitcode = inputManager()
print(f"Succeded With Exit Code {exitcode}")
"""