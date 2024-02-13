'''
тест чатового окна, чтобы можно было вводить вопрос и получать ответ
тут есть особенность, что запрос не печатается, пока не придет ответ,
но я на это дело подзабил, когда делал
'''

import PySimpleGUI as sg
import requests

url = "http://ip-31-222-229-137-89923.vps.hosted-by-mvps.net:9090/"

sg.theme('GreenTan')

layout = [[sg.Text('Your output will go here', size=(40, 1))],
          [sg.Output(size=(110, 20), font=('Helvetica 10'))],
          [sg.Multiline(size=(70, 5), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
           sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window('Chat window', layout, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):
        break
    if event == 'SEND':
        query = values['-QUERY-'].rstrip()

        print('User: {}'.format(query), flush=True)
        r = requests.post(url, json={"question": query})
        print('Helper: ', r.json()['answer'])

window.close()

