

import kivy

from getQR import get_qr_code_binary

from kivy.app import App

from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
from kivy.uix.floatlayout import FloatLayout


class MyLayout(FloatLayout):
    def reload_qr(self, qr_code):
        print("getting the picture")
        binary_qr = get_qr_code_binary()
        with open("image.png", "wb") as f :
            f.write(binary_qr)
        qr_code.reload()





class TestApp(App):
    pass
        #MyLayout.reload_qr()






if __name__ == '__main__':
    TestApp().run()
