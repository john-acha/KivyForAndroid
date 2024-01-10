# File name: pagelayout.py
import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class MyPageLayoutApp(PageLayout):
	pass

class PageLayoutApp(App):
	def build(self):
		return MyPageLayoutApp()

if __name__ == '__main__':
	PageLayoutApp().run()