from tkinter import Button, Frame, Label, StringVar, Tk


STATIC_VALUES = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
OPERATORS = ['+', '-', '*', '/', '%']
COMMANDS = ['CLR', 'BACK', '+/-', '=']
FONT = ('Terminal', 24, 'bold')

BUTTON_WIDTH = 0.25
BUTTON_HEIGHT = 0.2

POS_X_1 = 0.125
POS_X_2 = 0.375
POS_X_3 = 0.625
POS_X_4 = 0.875

POS_Y_1 = 0.1
POS_Y_2 = 0.3
POS_Y_3 = 0.5
POS_Y_4 = 0.7
POS_Y_5 = 0.9


class CalcButton:
    def __init__(self, text, pos_x, pos_y):
        self.button = Button(master=button_frame,
                             activebackground='black',
                             activeforeground='white',
                             bg='white',
                             bd='3',
                             command=lambda: press_button(self.button['text']),
                             font=FONT,
                             relief='solid',
                             text=text)
                             
        self.button.place(relx=pos_x,
                          rely=pos_y,
                          relwidth=BUTTON_WIDTH,
                          relheight=BUTTON_HEIGHT,
                          anchor='c')


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
                display_values.clear()
                display_values.append('Error')
    except IndexError:
        display_values.clear()
        display_values.append('???')
    except SyntaxError:
        display_values.clear()
        display_values.append('Bad syntax')
    except ZeroDivisionError:
        display_values.clear()
        display_values.append('Can\'t div by zero')
    
    display.set(str().join(display_values))


if __name__ == '__main__':
    root = Tk()
    root.geometry('480x640')
    root.title('Calculator')

    display = StringVar()
    display_values = list()

    root_frame = Frame(root, bg='white')
    button_frame = Frame(root_frame, bg='white', bd=3, relief='solid')
    display_frame = Frame(root_frame, bg='white', bd=3, relief='solid')
    display_label = Label(display_frame, font=FONT, bd=10, textvariable=display, anchor='e')

    root_frame.place(relwidth=1, relheight=1)
    button_frame.place(relx=0.5, rely=0.6, relwidth=0.95, relheight=0.75, anchor='c')
    display_frame.place(relx=0.5, rely=0.125, relwidth=0.95, relheight=0.15, anchor='c')
    display_label.place(relwidth=1, relheight=1)

    root.bind('0', lambda _:press_button('0'))
    root.bind('1', lambda _:press_button('1'))
    root.bind('2', lambda _:press_button('2'))
    root.bind('3', lambda _:press_button('3'))
    root.bind('4', lambda _:press_button('4'))
    root.bind('5', lambda _:press_button('5'))
    root.bind('6', lambda _:press_button('6'))
    root.bind('7', lambda _:press_button('7'))
    root.bind('8', lambda _:press_button('8'))
    root.bind('9', lambda _:press_button('9'))

    root.bind('.', lambda _:press_button('.'))
    root.bind('+', lambda _:press_button('+'))
    root.bind('-', lambda _:press_button('-'))
    root.bind('*', lambda _:press_button('*'))
    root.bind('/', lambda _:press_button('/'))
    root.bind('%', lambda _:press_button('%'))

    root.bind('<Return>', lambda _:press_button('='))
    root.bind('<Next>', lambda _:press_button('+/-'))
    root.bind('<End>', lambda _:press_button('CLR'))
    root.bind('<Delete>', lambda _:press_button('BACK'))

    CalcButton('0', POS_X_2, POS_Y_5)
    CalcButton('1', POS_X_1, POS_Y_4)
    CalcButton('2', POS_X_2, POS_Y_4)
    CalcButton('3', POS_X_3, POS_Y_4)
    CalcButton('4', POS_X_1, POS_Y_3)
    CalcButton('5', POS_X_2, POS_Y_3)
    CalcButton('6', POS_X_3, POS_Y_3)
    CalcButton('7', POS_X_1, POS_Y_2)
    CalcButton('8', POS_X_2, POS_Y_2)
    CalcButton('9', POS_X_3, POS_Y_2)

    CalcButton('.', POS_X_3, POS_Y_5)
    CalcButton('=', POS_X_4, POS_Y_5)
    CalcButton('+', POS_X_4, POS_Y_4)
    CalcButton('-', POS_X_4, POS_Y_3)
    CalcButton('*', POS_X_4, POS_Y_2)
    CalcButton('/', POS_X_4, POS_Y_1)
    CalcButton('%', POS_X_3, POS_Y_1)
    CalcButton('+/-', POS_X_1, POS_Y_5)
    CalcButton('CLR', POS_X_2, POS_Y_1)
    CalcButton('BACK', POS_X_1, POS_Y_1)

    root.mainloop()
