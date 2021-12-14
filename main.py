from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
import calculate

symbols = ["+", "-", '*', '/', '.', '(', '%']

    

class DigitButton(Button):
    def __init__(self, **kwargs):
        super(DigitButton, self).__init__(**kwargs)
        self.symb = False



class CalcuLayout(Widget):
    def input_update(self, instance):
        if instance.symb == False or instance.text == "()":
            print(instance.symb)
            self.ids.input_text.text += instance.text
        else:
            if self.ids.input_text.text != "":
                if self.ids.input_text.text[-1] not in symbols :
                    print(instance.symb)
                    self.ids.input_text.text += instance.text

    def clear(self):
        self.ids.input_text.text = ""

    def add_parenthesis(self, instance):
        if instance.open == True:
            self.ids.input_text.text += "("
            instance.open = False
        else:
            self.ids.input_text.text += ")"
            instance.open = True
    
    def submit(self):
        solution = calculate.solve(self.ids.input_text.text)
        print(solution)
        self.ids.input_text.text = str(solution[0])




class CalculatorApp(App):
    def build(self):
        return CalcuLayout()

    

    

if __name__ == '__main__':
    CalculatorApp().run()