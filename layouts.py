# File name: layouts.py
import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGridLayoutApp(GridLayout):
	pass

class LayoutsApp(App):
	def build(self):
		return MyGridLayoutApp()

if __name__ == '__main__':
	LayoutsApp().run()