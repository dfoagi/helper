'''
Здесь к окну чата добавил кнопки для записи голосом, состояния поймешь когда запустишь.
не добавлял отправку запроса и stt, просто пытался понять можно ли запустить два цикла
одновременно. спойлер - пока не понял
'''
import PySimpleGUI as sg

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))

layout = [[sg.Text('Your output will go here', size=(40, 1))],
          [sg.Output(size=(110, 20), font=('Helvetica 10'))],
          [sg.Multiline(size=(70, 5), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('Start', button_color=('white', 'black'), key='-Start-'),
           sg.Button('Stop', button_color=('white', 'black'), key='-Stop-'),
           sg.Button('Reset', button_color=('white', 'firebrick3'), key='-Reset-'),
           sg.Button('Submit', button_color=('white', 'springgreen4'), key='-Submit-')]]

window = sg.Window("Time Tracker", layout,
                   default_element_size=(12, 1),
                   text_justification='r',
                   auto_size_text=False,
                   auto_size_buttons=False,
                   default_button_element_size=(8, 3),
                   finalize=True)

for key, state in {'-Start-': False, '-Stop-': True, '-Reset-': True, '-Submit-': True}.items():
    window[key].update(disabled=state)

recording = have_data = False
while True:

    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break

    if event == '-Start-':
        for key, state in {'-Start-': True, '-Stop-': False, '-Reset-': True, '-Submit-': True}.items():
            window[key].update(disabled=state)
        recording = True
        # while recording:
        #     new_event, nv = window.read()
        #     if new_event == '-Stop-':
        #         recording = False

    elif event == '-Stop-' and recording:
        [window[key].update(disabled=value) for key, value in {
            '-Start-': False, '-Stop-': True, '-Reset-': False, '-Submit-': False}.items()]
        recording = False
        have_data = True
    elif event == '-Reset-':
        [window[key].update(disabled=value) for key, value in {
            '-Start-': False, '-Stop-': True, '-Reset-': True, '-Submit-': True}.items()]
        recording = False
        have_data = False
    elif event == '-Submit-' and have_data:
        [window[key].update(disabled=value) for key, value in {
            '-Start-': False, '-Stop-': True, '-Reset-': True, '-Submit-': True}.items()]
        recording = False
        have_data = False

window.close()
