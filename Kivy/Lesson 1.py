from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput

from kivy.config import Config
Config.set('graphics','resizable','0');
Config.set('graphics','width','640');
Config.set('graphics','height','480');

# заполняет все доступное пространство и в его контексте позв располагать виджеты, кот к нему крепятся
from kivy.uix.floatlayout import FloatLayout

# добавляет возможность изменять размер пальцами как на тачскрине
from kivy.uix.scatter import Scatter

class MyApp(App):
    def build(self):
        
        s = Scatter()
        fl = FloatLayout(size = (300, 300))
        s.add_widget(fl)
        fl.add_widget(Button(text = "Это моя первая кнопка", 
        font_size = 16, 
        on_press = self.btn_press,
        background_color = [.62, .88, .88, 1],
        background_normal = '',
        size_hint = (.5, .25)))
        
        return s
        
    def btn_press(self, instance):
        print('Кнопка нажата!')
        instance.text = 'Я нажата'
        
    
if __name__ == "__main__":
    MyApp().run()