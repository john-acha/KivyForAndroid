# Customize the application

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginApp(GridLayout):

	def __init__(self, **kwargs):
		super(LoginApp, self).__init__(**kwargs)

		self.cols = 2
		
		self.add_widget(Label(text='Username'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		
		self.add_widget(Label(text='Password'))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)

class PowerApp(App):

	def build(self):
		return LoginApp()

if __name__ == '__main__':
	PowerApp().run()
