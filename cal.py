from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.grid = GridLayout(cols=4)
        self.prev_text = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        self.text = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        self.grid.add_widget(self.prev_text)
        self.grid.add_widget(self.text)
        buttons = [
            '1', '2', '3', '4',
            '5', '6', '7', '8',
            '9', '0', '+', '-',
            '*', '/', '.', '%',
            '='
        ]
        for button in buttons:
            self.grid.add_widget(Button(text=button, on_press=self.on_button_press))
        clear_button = Button(text='C')
        clear_button.bind(on_press=self.clear)
        self.grid.add_widget(clear_button)
        return self.grid

    def on_button_press(self, instance):
        current = self.text.text
        button_text = instance.text

        if button_text == '=':
            try:
                result = str(eval(current))
                self.prev_text.text = current
                self.text.text = result
            except Exception:
                self.text.text = 'Error'
        elif button_text == 'C':
            self.text.text = ''
        else:
            new_text = current + button_text
            self.text.text = new_text

    def clear(self, instance):
        self.text.text = ''
        self.prev_text.text = ''
        instance.text.text = ''
        instance.prev_text.text = ''

if __name__== '__main__':
 app = CalculatorApp()
 app.run()