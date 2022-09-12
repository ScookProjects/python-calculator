# Sam Cook (c) 2022

from tkinter import *


class Calculator:

    

    def __init__(self):

        # colors
        self.black = '#001524'
        self.blue = '#15616D'
        self.orange = '#FF7D00'
        self.white = '#FFECD1'

        self.text = ''
        
        self.window=Tk()
        self.window.minsize(450, 600)
        self.window.config(bg='#001524')

        Grid.rowconfigure(self.window, 0, weight=2)
        Grid.columnconfigure(self.window, 0, weight=2)
        Grid.rowconfigure(self.window, 1, weight=2)
        Grid.columnconfigure(self.window, 1, weight=2)
        Grid.rowconfigure(self.window, 2, weight=2)
        Grid.columnconfigure(self.window, 2, weight=2)
        Grid.rowconfigure(self.window, 3, weight=2)
        Grid.columnconfigure(self.window, 3, weight=2)
        Grid.rowconfigure(self.window, 4, weight=2)
        Grid.rowconfigure(self.window, 5, weight=2)

        
        # font size
        size = 48

        # Text line
        self.equation_line = Label(self.window, height=2, bg=self.white, fg=self.black, font=("Helvetica",int(size)))
        
        # Button styles
        number_button_color = self.white
        number_button_hover_color = self.white
        number_button_text_color = self.blue
        number_button_hover_text_color = self.orange

        button_color = self.blue
        button_hover_color = self.blue
        button_text_color = self.white
        button_hover_text_color = self.orange

        equals_button_color = self.orange
        equals_button_hover_color = self.orange
        equals_button_text_color = self.white
        equals_button_hover_text_color = self.black


        # Create Buttons
        button_0 = Button(self.window, 
            text='0', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('0'))
        button_1 = Button(self.window, 
            text='1', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('1'))
        button_2 = Button(self.window, 
            text='2', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('2'))
        button_3 = Button(self.window, 
            text='3', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('3'))
        button_4 = Button(self.window, 
            text='4', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('4'))
        button_5 = Button(self.window, 
            text='5', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('5'))
        button_6 = Button(self.window, 
            text='6', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('6'))
        button_7 = Button(self.window, 
            text='7', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('7'))
        button_8 = Button(self.window, 
            text='8', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('8'))
        button_9 = Button(self.window, 
            text='9', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('9'))
        button_add = Button(self.window, 
            text='+', 
            bg=button_color, 
            fg=button_text_color, 
            activeforeground=button_hover_text_color, 
            activebackground=button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('+'))
        button_clear = Button(self.window, 
            text='C', 
            bg=button_color, 
            fg=button_text_color, 
            activeforeground=button_hover_text_color, 
            activebackground=button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('C'))
        button_close_parentheses = Button(self.window, 
            text=')', 
            bg=button_color, 
            fg=button_text_color, 
            activeforeground=button_hover_text_color, 
            activebackground=button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press(')'))
        button_delete = Button(self.window, 
            text=u'\u2190', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('D'))
        button_divide = Button(self.window, 
            text='/', 
            bg=button_color, 
            fg=button_text_color, 
            activeforeground=button_hover_text_color, 
            activebackground=button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('/'))
        button_equals = Button(self.window, 
            text='=', 
            bg=equals_button_color, 
            fg=equals_button_text_color, 
            activeforeground=equals_button_hover_text_color, 
            activebackground=equals_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('='))
        button_multiply = Button(self.window, 
            text='x', 
            bg=button_color, 
            fg=button_text_color, 
            activeforeground=button_hover_text_color, 
            activebackground=button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('*'))
        button_open_parentheses = Button(self.window, 
            text='(', 
            bg=button_color, 
            fg=button_text_color, 
            activeforeground=button_hover_text_color, 
            activebackground=button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('('))
        button_point = Button(self.window, 
            text='.', 
            bg=number_button_color, 
            fg=number_button_text_color, 
            activeforeground=number_button_hover_text_color, 
            activebackground=number_button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('.'))
        button_subtract = Button(self.window, 
            text='-', 
            bg=button_color, 
            fg=button_text_color, 
            activeforeground=button_hover_text_color, 
            activebackground=button_hover_color, 
            font=("Helvetica",int(size)), 
            command=lambda: self.handle_button_press('-'))


        
        # Arrange elements in grid
        # row 0
        self.equation_line.grid(row=0, column=0, columnspan=4, sticky='NSEW')

        # row 1
        button_clear.grid(row=1, column=0, sticky='NSEW')
        button_open_parentheses.grid(row=1, column=1, sticky='NSEW')
        button_close_parentheses.grid(row=1, column=2, sticky='NSEW')
        button_divide.grid(row=1, column=3, sticky='NSEW')

        # row 2
        button_1.grid(row=2, column=0, sticky='NSEW')
        button_2.grid(row=2, column=1, sticky='NSEW')
        button_3.grid(row=2, column=2, sticky='NSEW')
        button_multiply.grid(row=2, column=3, sticky='NSEW')

        # row 3
        button_4.grid(row=3, column=0, sticky='NSEW')
        button_5.grid(row=3, column=1, sticky='NSEW')
        button_6.grid(row=3, column=2, sticky='NSEW')
        button_subtract.grid(row=3, column=3, sticky='NSEW')

        # row 4
        button_7.grid(row=4, column=0, sticky='NSEW')
        button_8.grid(row=4, column=1, sticky='NSEW')
        button_9.grid(row=4, column=2, sticky='NSEW')
        button_add.grid(row=4, column=3, sticky='NSEW')

        # row 5
        button_delete.grid(row=5, column=0, sticky='NSEW')
        button_0.grid(row=5, column=1, sticky='NSEW')
        button_point.grid(row=5, column=2, sticky='NSEW')
        button_equals.grid(row=5, column=3, sticky='NSEW')

        self.window.title('Scook\'s Python Calculator')
        self.window.geometry('600x800')
        self.window.mainloop()


    def handle_button_press(self, text):
        self.equation_line.config(fg=self.black)

        # user pressed equals
        if text == '=':
            self.calculate_answer()

        # user pressed clear
        elif text == 'C':
            self.text = ''

        # user pressed delete
        elif text == 'D':
            self.text = self.text[:-1]
        
        # user pressed open paratheses
        elif text == '(':

            # handle potential issues due to bad syntax in the equation
            if len(self.text) > 0:
                try:
                    if int(self.text[-1]):
                        self.text = self.text + '*'

                except:
                    
                    if self.text[-1] == '.':

                        while (self.text[-1] == '.'):

                            self.text = self.text[:-1]

                            if len(self.text) == 0:
                                break

                        if len(self.text) > 0:
                            self.text += '*'

                self.text = self.text

            
            self.text += text 

        # add user input to equation line
        else:
            self.text += text
            
        self.equation_line.config(text=self.text)
    

    def calculate_answer(self):

        try:
            # limit to 6 decimal points
            result = round(eval(self.text), 6)

            # if the result doesn't need a decimal point then remove it
            if result == int(result):
                result = int(result)

            # output result
            self.text = str(result)

        except:
            # something is wrong with the equation so change the text to self.orange to alert the user
            self.equation_line.config(fg=self.orange)



def start_calculaltor():
    calc = Calculator()

    
start_calculaltor()
