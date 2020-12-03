import random
import PySimpleGUI as sg

random_number = random.randint(0,100)
count = 10

sg.theme('BluePurple') 
   
layout = [[sg.Text(size=(50,1),key='PORADA',text_color='red')],
          [sg.Text('Podaj liczbe w zakresie 0-100:'), 
           sg.Text(size=(25,1), key='COUNT',text_color='red')], 
          [sg.Input(key='-IN-')], 
          [sg.Button('Zgaduj',key='Zgaduj'), sg.Button('Zakończ')]] 
  
window = sg.Window('Number Guessing', layout) 

while True: 
    event, values = window.read() 
    print(event, values) 
      
    if event in  (None, 'Zakończ'): 
        break
      
    if event == 'Zgaduj':
        guessed_number = int(values['-IN-'])
        if(guessed_number == random_number):
            window['PORADA'].update("WYGRAŁEŚ!!!",text_color='green')
            window['COUNT'].update("")
            window['Zgaduj'].update(disabled=True)
        else:
            if(guessed_number < random_number):
                window['PORADA'].update('Podana liczba jest zbyt mała!')
            else:
                window['PORADA'].update('Podana liczba jest zbyt duża!')
            count = count - 1
            window['COUNT'].update(f'Pozostało {count} prób!')
        
window.close() 