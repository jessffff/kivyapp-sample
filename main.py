from kivymd.app import MDApp
from kivy.lang import Builder

class SampleApp(MDApp):

    def build(self):
        self.appKv='''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1, 1, 1, 1  # Blanc

        MDLabel:
            text: 'Hello, World.'
            halign: 'center'
'''

        AppScreen=Builder.load_string(self.appKv)
        return AppScreen
    
SampleApp().run()

