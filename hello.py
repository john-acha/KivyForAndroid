# File name: hello.py
import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.button import Label


class HelloApp(App):
	def build(self):
		return Label(text='Hello kivy!')

if __name__ == '__main__':
	HelloApp().run()
