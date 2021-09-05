# Tela de Login 
# Versão com Interface
# USER: futex | SENHA: 123

# @badfutex | github.com/badfutex

from PySimpleGUI import PySimpleGUI as sg

# Meu Tema

FutexTheme = {'BACKGROUND': '#201c24',
                'TEXT': '#c9fffb',
                'INPUT': '#36313b',
                'TEXT_INPUT': '#ffffff',
                'SCROLL': '#36313b',
                'BUTTON': ('white', '#36313b'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

sg.theme_add_new('FutexTheme', FutexTheme)

# Layout
sg.theme('FutexTheme')
layout = [
    [sg.Text(' USER:  '),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('SENHA: '),sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Button('LOGIN '), sg.Button('FECHAR ')]
]
# Janela
janela = sg.Window('LOGIN', layout)
# Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        print('Programa Fechado')
        break
    if eventos == 'LOGIN ':
        if valores['usuario'] == 'futex' and valores['senha'] == '123':
            print('Login efetuado com Sucesso!')
        else:
            print('Usuario ou Senha incorretos')
    if eventos == 'FECHAR ':
        print('Programa Fechado')
        break
