import requests

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window

Window.size = (500, 750)

class MyApp(App):

    def build(self):
        self.title = "Poke Location"

        layout = BoxLayout(orientation="vertical")
        slayout = GridLayout(cols=2, padding=1, spacing=1)
        
        app_image = Image(source="pokeball.png")

        self.input = TextInput(text="", multiline=False, size_hint=(None, None), height=50, width=200, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.submit_button = Button(text="Submit", size_hint=(None, None), height=50, width=100, pos_hint={'center_x': 0.5}, on_press=self.update_label)
        self.result_label = Label(text="Enter a Pokemon", height=50, font_size="13sp")
        self.location_label = Label(text="", height=50, font_size="11sp")

        self.status_code = 0

        layout.add_widget(app_image)
        slayout.add_widget(self.result_label)
        slayout.add_widget(self.location_label)
        layout.add_widget(slayout)
        layout.add_widget(self.input)
        layout.add_widget(self.submit_button)
        #layout.add_widget(self.result_label)
        #layout.add_widget(self.location_label)

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
            pokemon_name = pokemon_data['name'].title()
            pokemon_height = round(pokemon_data['height'] * 0.1, 2)
            pokemon_weight = round(pokemon_data['weight'] * 0.1, 2)
            pokemon_types = pokemon_data['types']
            
            self.result_label.text = f"Name: {pokemon_name}\n"
            self.result_label.text += f"Height: {pokemon_height}m\nWeight: {pokemon_weight}kg\n\nTypes:"

            for i in pokemon_types:
                self.result_label.text += f"\n- {i['type']['name'].title()}"
            
            if pokemon_location:

                counter = 0

                self.location_label.text = "\nLocations: "

                for i in pokemon_location:

                    if counter < 25:
                        self.location_label.text += f"\n- {i['location_area']['name'].title()}"

                    counter += 1
                    
if __name__ == '__main__':
    MyApp().run()