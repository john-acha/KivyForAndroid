# Create an application
import kivy
kivy.require('2.2.1') # replace with your current kivy version

from kivy.app import App
from kivy.uix.label import Label

class PowerApp(App):
	def build(self):
		return Label(text='Hello Kivy')

if __name__ == '__main__':
	PowerApp().run()