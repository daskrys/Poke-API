import requests
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text='Hello, Kivy!')
    
    #response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
    #print(response.json())

if __name__ == '__main__':
    MyApp().run()