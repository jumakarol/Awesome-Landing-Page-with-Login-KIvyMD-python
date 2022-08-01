from kivymd.app import MDApp
from kivy.lang  import Builder
from helpers import *
from kivy.core.window import Window





class LandingApp(MDApp):

	def build(self):
		self.theme_cls.primary_palette="Pink"
		return Builder.load_file('helper.kv')


	def navigation_menu(self):
		print("Menu Clicked")





LandingApp().run()
