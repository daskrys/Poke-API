import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

# Set the size of the window
Window.size = (300, 350)

class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        bg_image = Image(source='pokeball.png')

        self.result = Label(text="Enter a Pokemon", size_hint_y=None, height=50)
        self.input = TextInput(text='', multiline=False, size_hint_y=None, height=50)
        pokemon_data = get_pokemon(self.input)
        pokemon_location = requests.get(pokemon_data['location_area_encounters']).json()

        submit_button = Button(text='Submit', on_press=self.update_label, size_hint_y=None, height=50)
        
        layout.add_widget(bg_image)
        layout.add_widget(self.input)
        layout.add_widget(submit_button)
        layout.add_widget(self.result)
        
        return layout
    
    def get_pokemon(pokemon):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            return data
        else: 
            print(f"Error: Received status code {response.status_code}")
            
            return None


    def update_label(self, instance):
        self.result.text = "You said : " + self.input.text

if __name__ == '__main__':
    MyApp().run()

