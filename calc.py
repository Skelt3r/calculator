import tkinter as tk

# Initialize Tkinter
root = tk.Tk()
root.geometry('480x640')
root.title('Calculator')

# Define fonts and button values
STATIC_VALUES  = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
OPERATORS      = ['+', '-', '*', '/', '%']
COMMANDS       = ['CLR', 'BACK', '+/-', '=']
FONT           = ('Terminal', 24, 'bold')

# Define button geometry and axis positions
BUTTON_WIDTH   = 0.25
BUTTON_HEIGHT  = 0.2

POS_X_1 = 0.125
POS_X_2 = 0.375
POS_X_3 = 0.625
POS_X_4 = 0.875

POS_Y_1 = 0.1
POS_Y_2 = 0.3
POS_Y_3 = 0.5
POS_Y_4 = 0.7
POS_Y_5 = 0.9

# Declare variables used for on-screen display
display_values = []
display        = tk.StringVar()

# Define outlining GUI elements
root_frame    = tk.Frame(root, bg='white')
button_frame  = tk.Frame(root_frame, bg='white', bd=3, relief='solid')
display_frame = tk.Frame(root_frame, bg='white', bd=3, relief='solid')
display_label = tk.Label(display_frame, font=FONT, bd=10, textvariable=display, anchor='e')

# Place GUI elements
root_frame.place(relwidth=1, relheight=1)
button_frame.place(relx=0.5, rely=0.6, relwidth=0.95, relheight=0.75, anchor='c')
display_frame.place(relx=0.5, rely=0.125, relwidth=0.95, relheight=0.15, anchor='c')
display_label.place(relwidth=1, relheight=1)


# Functionality for all calculator buttons
def press_button(text):
    try:
        if text in STATIC_VALUES:
            if text == '.' and '.' in display_values: pass
            else: display_values.append(text)
        elif text in OPERATORS:
            display_values.append(text)
            new_str = str().join(display_values)
            display_values.clear()
            display_values.append(new_str)
        elif text in COMMANDS:
            if text == 'CLR':
                display_values.clear()
            elif text == 'BACK':
                display_values.pop(-1)
            elif text == '+/-':
                new_str = str(-int(str().join(display_values)))
                display_values.clear()
                display_values.append(new_str)
            elif text == '=':
                result = str(eval(str().join(display_values)))
                display_values.clear()
                display_values.append(result)
            else:
                display.set('Error')
    except:
        pass
    
    display.set(str().join(display_values))


# Class for generating calculator buttons
class CalcButton():
    def __init__(self, text, pos_x, pos_y):
        self.button = tk.Button(master=button_frame,
                                activebackground='black',
                                activeforeground='white',
                                bg='white',
                                bd='3',
                                command=lambda:press_button(self.button['text']),
                                font=FONT,
                                relief='solid',
                                text=text)
        
        self.button.place(relx=pos_x,
                          rely=pos_y,
                          relwidth=BUTTON_WIDTH,
                          relheight=BUTTON_HEIGHT,
                          anchor='c')


# Define calculator buttons
b_zero      = CalcButton('0', POS_X_2, POS_Y_5)
b_one       = CalcButton('1', POS_X_1, POS_Y_4)
b_two       = CalcButton('2', POS_X_2, POS_Y_4)
b_three     = CalcButton('3', POS_X_3, POS_Y_4)
b_four      = CalcButton('4', POS_X_1, POS_Y_3)
b_five      = CalcButton('5', POS_X_2, POS_Y_3)
b_six       = CalcButton('6', POS_X_3, POS_Y_3)
b_seven     = CalcButton('7', POS_X_1, POS_Y_2)
b_eight     = CalcButton('8', POS_X_2, POS_Y_2)
b_nine      = CalcButton('9', POS_X_3, POS_Y_2)

b_decimal   = CalcButton('.',    POS_X_3, POS_Y_5)
b_equal     = CalcButton('=',    POS_X_4, POS_Y_5)
b_plus      = CalcButton('+',    POS_X_4, POS_Y_4)
b_minus     = CalcButton('-',    POS_X_4, POS_Y_3)
b_multiply  = CalcButton('*',    POS_X_4, POS_Y_2)
b_divide    = CalcButton('/',    POS_X_4, POS_Y_1)
b_modulo    = CalcButton('%',    POS_X_3, POS_Y_1)
b_swap      = CalcButton('+/-',  POS_X_1, POS_Y_5)
b_clear     = CalcButton('CLR',  POS_X_2, POS_Y_1)
b_backspace = CalcButton('BACK', POS_X_1, POS_Y_1)

# Define keybinds
root.bind('0', lambda _0:press_button('0'))
root.bind('1', lambda _1:press_button('1'))
root.bind('2', lambda _2:press_button('2'))
root.bind('3', lambda _3:press_button('3'))
root.bind('4', lambda _4:press_button('4'))
root.bind('5', lambda _5:press_button('5'))
root.bind('6', lambda _6:press_button('6'))
root.bind('7', lambda _7:press_button('7'))
root.bind('8', lambda _8:press_button('8'))
root.bind('9', lambda _9:press_button('9'))

root.bind('.', lambda _per:press_button('.'))
root.bind('+', lambda _pls:press_button('+'))
root.bind('-', lambda _min:press_button('-'))
root.bind('*', lambda _mul:press_button('*'))
root.bind('/', lambda _div:press_button('/'))
root.bind('%', lambda _mod:press_button('%'))

root.bind('<Return>', lambda _ent:press_button('='))
root.bind('<Next>',   lambda _pdn:press_button('+/-'))
root.bind('<End>',    lambda _esc:press_button('CLR'))
root.bind('<Delete>', lambda _bak:press_button('BACK'))

# Initialize program loop
root.mainloop()
