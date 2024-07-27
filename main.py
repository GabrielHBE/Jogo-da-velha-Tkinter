import tkinter as tk
import random

class Player:

    def __init__(self,name, icon) -> None:
        self.name = name
        self.icon = icon

player1 = None
player2 = None

window = tk.Tk()

turn = tk.StringVar()

button_1_content = tk.StringVar()
button_2_content = tk.StringVar()
button_3_content = tk.StringVar()
button_4_content = tk.StringVar()
button_5_content = tk.StringVar()
button_6_content = tk.StringVar()
button_7_content = tk.StringVar()
button_8_content = tk.StringVar()
button_9_content = tk.StringVar()

def verify():

    global button_1_content, button_2_content, button_3_content, button_4_content, button_5_content, button_6_content, button_7_content, button_8_content, button_9_content

    
    if button_1_content.get()=='X' and button_2_content.get() == 'X' and button_3_content.get() =='X':
        return f'{player1.name} won'
    
    elif button_4_content.get()=='X' and button_5_content.get() == 'X' and button_6_content.get() =='X':
        return f'{player1.name} won'
    
    elif button_7_content.get()=='X' and button_8_content.get() == 'X' and button_9_content.get() =='X':
        return f'{player1.name} won'
    
    elif button_7_content.get()=='X' and button_4_content.get() == 'X' and button_1_content.get() =='X':
        return f'{player1.name} won'
    
    elif button_2_content.get()=='X' and button_5_content.get() == 'X' and button_8_content.get() =='X':
        return f'{player1.name} won'
    
    elif button_3_content.get()=='X' and button_6_content.get() == 'X' and button_9_content.get() =='X':
        return f'{player1.name} won'
    
    elif button_1_content.get()=='X' and button_5_content.get() == 'X' and button_9_content.get() =='X':
        return f'{player1.name} won'
    
    elif button_7_content.get()=='X' and button_5_content.get() == 'X' and button_3_content.get() =='X':
        return f'{player1.name} won'
    
    elif button_1_content.get()=='O' and button_2_content.get() == 'O' and button_3_content.get() =='O':
        return f'{player2.name} won'
    
    elif button_4_content.get()=='O' and button_5_content.get() == 'O' and button_6_content.get() =='O':
        return f'{player2.name} won'
    
    elif button_7_content.get()=='O' and button_8_content.get() == 'O' and button_9_content.get() =='O':
        return f'{player2.name} won'
    
    elif button_7_content.get()=='O' and button_4_content.get() == 'O' and button_1_content.get() =='O':
        return f'{player2.name} won'
    
    elif button_2_content.get()=='O' and button_5_content.get() == 'O' and button_8_content.get() =='O':
        return f'{player2.name} won'
    
    elif button_3_content.get()=='O' and button_6_content.get() == 'O' and button_9_content.get() =='O':
        return f'{player2.name} won'
    
    elif button_1_content.get()=='O' and button_5_content.get() == 'O' and button_9_content.get() =='O':
        return f'{player2.name} won'
    
    elif button_7_content.get()=='O' and button_5_content.get() == 'O' and button_3_content.get() =='O':
        return f'{player2.name} won'

def Play(button):
    global cont, x_o, turn,player1,player2
    global button_1_content, button_2_content, button_3_content, button_4_content, button_5_content, button_6_content, button_7_content, button_8_content, button_9_content

    if player1.name in turn.get():
        if button == 'b1':
            button_1_content.set(player1.icon)
        elif button == 'b2':
            button_2_content.set(player1.icon)
        elif button == 'b3':
            button_3_content.set(player1.icon)
        elif button == 'b4':
            button_4_content.set(player1.icon)
        elif button == 'b5':
            button_5_content.set(player1.icon)
        elif button == 'b6':
            button_6_content.set(player1.icon)
        elif button == 'b7':
            button_7_content.set(player1.icon)
        elif button == 'b8':
            button_8_content.set(player1.icon)
        elif button == 'b9':
            button_9_content.set(player1.icon)

        turn.set(player2.name)
    elif player2.name in turn.get():
        if button == 'b1':
            button_1_content.set(player2.icon)
        elif button == 'b2':
            button_2_content.set(player2.icon)
        elif button == 'b3':
            button_3_content.set(player2.icon)
        elif button == 'b4':
            button_4_content.set(player2.icon)
        elif button == 'b5':
            button_5_content.set(player2.icon)
        elif button == 'b6':
            button_6_content.set(player2.icon)
        elif button == 'b7':
            button_7_content.set(player2.icon)
        elif button == 'b8':
            button_8_content.set(player2.icon)
        elif button == 'b9':
            button_9_content.set(player2.icon)

        turn.set(player1.name)


    winner = verify()
    if winner != None:
        turn.set(winner)
        print(winner)

def Start():
    global turn,player1,player2

    player1 = Player(enter_player1.get(),'X')
    player2 = Player(enter_player2.get(),'O')

    enter_player1.grid_forget()
    enter_player1_text.grid_forget()
    enter_player2.grid_forget()
    enter_player2_text.grid_forget()
    start_game_button.grid_forget()

    rand = random.randint(1, 2)

    if rand == 1:
        turn.set(f'{player1.name}, ({player1.icon})')
    else:
        turn.set(f'{player2.name}, ({player2.icon})')

    turn_text = tk.Label(window, textvariable=turn, font=('Arial', 15))
    turn_text.grid(row=0, column=0, columnspan=3)

    button1 = tk.Button(window, textvariable=button_1_content, command=lambda: Play('b1'), padx=10, pady=10)
    button1.grid(row=2, column=0, sticky='nsew')

    button2 = tk.Button(window, textvariable=button_2_content, command=lambda: Play('b2'), padx=10, pady=10)
    button2.grid(row=2, column=1, sticky='nsew')

    button3 = tk.Button(window, textvariable=button_3_content, command=lambda: Play('b3'), padx=10, pady=10)
    button3.grid(row=2, column=2, sticky='nsew')

    button4 = tk.Button(window, textvariable=button_4_content, command=lambda: Play('b4'), padx=10, pady=10)
    button4.grid(row=3, column=0, sticky='nsew')

    button5 = tk.Button(window, textvariable=button_5_content, command=lambda: Play('b5'), padx=10, pady=10)
    button5.grid(row=3, column=1, sticky='nsew')

    button6 = tk.Button(window, textvariable=button_6_content, command=lambda: Play('b6'), padx=10, pady=10)
    button6.grid(row=3, column=2, sticky='nsew')

    button7 = tk.Button(window, textvariable=button_7_content, command=lambda: Play('b7'), padx=10, pady=10)
    button7.grid(row=4, column=0, sticky='nsew')

    button8 = tk.Button(window, textvariable=button_8_content, command=lambda: Play('b8'), padx=10, pady=10)
    button8.grid(row=4, column=1, sticky='nsew')

    button9 = tk.Button(window, textvariable=button_9_content, command=lambda: Play('b9'), padx=10, pady=10)
    button9.grid(row=4, column=2, sticky='nsew')



# Configurando pesos das colunas e linhas para evitar esticamento
for i in range(3):
    window.columnconfigure(i, weight=1)
for i in range(5):
    window.rowconfigure(i, weight=1)

enter_player1_text = tk.Label(window, text='First player name (X):')
enter_player1_text.grid(row=0, column=0, sticky='w')
enter_player1 = tk.Entry(window, font=('Arial', 15))
enter_player1.grid(row=0, column=1, sticky='ew')

enter_player2_text = tk.Label(window, text='Second player name (O):')
enter_player2_text.grid(row=1, column=0, sticky='w')
enter_player2 = tk.Entry(window, font=('Arial', 15))
enter_player2.grid(row=1, column=1, sticky='ew')

start_game_button = tk.Button(window, text='Start game', command=Start)
start_game_button.grid(row=2, column=0, columnspan=2)

window.mainloop()