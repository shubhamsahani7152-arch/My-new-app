from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class MeriJankariApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.input_box = TextInput(hint_text='Kuch yahan likho...', size_hint=(1, 0.2))
        layout.add_widget(self.input_box)
        
        btn = Button(text='Jankari Khojo', size_hint=(1, 0.2), background_color=(0.1, 0.6, 0.8, 1))
        btn.bind(on_press=self.show_data)
        layout.add_widget(btn)
        
        self.result_label = Label(text='Jawab yahan dikhega', size_hint=(1, 0.6))
        layout.add_widget(self.result_label)
        
        return layout

    def show_data(self, instance):
        text = self.input_box.text.lower()
        if 'india' in text:
            self.result_label.text = 'India hamara desh hai, jo apni sanskriti ke liye jana jata hai.'
        elif 'python' in text:
            self.result_label.text = 'Python ek powerful aur aasan programming language hai.'
        else:
            self.result_label.text = 'Aapne likha: ' + self.input_box.text

if __name__ == '__main__':
    MeriJankariApp().run()
