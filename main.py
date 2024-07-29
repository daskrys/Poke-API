import requests

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window

Window.size = (400, 500)

class MyApp(App):

    def build(self):
        self.title = "Poke Location"    
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        app_image = Image(source="pokeball.png")

        self.input = TextInput(text="", multiline=False, size_hint=(None, None), height=50, width=200, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.submit_button = Button(text="Submit", size_hint=(None, None), height=50, width=200, pos_hint={'center_x': 0.5}, on_press=self.update_label)
        self.result_label = Label(text="Enter a Pokemon", height=50)

        self.status_code = 0

        layout.add_widget(app_image)
        layout.add_widget(self.input)
        layout.add_widget(self.submit_button)
        layout.add_widget(self.result_label)

        return layout
    
    def get_pokemon(self, pokemon):

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
        response = requests.get(url)
        self.status_code = response.status_code

        if response.status_code == 200:
            data = response.json()
            
            return data
        else:
            print(f"An error occurred, returned status code {response.status_code}")

            return None


    def update_label(self, instance):
        pokemon_data = self.get_pokemon(self.input.text)   

        if pokemon_data:
            pokemon_location = requests.get(pokemon_data['location_area_encounters']).json()
            
            self.result_label.text = f"Name: {pokemon_data['name'].title()}\n"
            self.result_label.text += f"Height: {pokemon_data['height'] * 0.1}m\nWeight: {pokemon_data['weight'] * 0.1}kg\nTypes:"

    #response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
    #print(response.json())

if __name__ == '__main__':
    MyApp().run()