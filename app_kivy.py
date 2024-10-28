from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("label_color.kv")

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', text='Назад'):
        super().__init__(text=text)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Вітаємо на головному екрані!", color="blue", font_size=45, outline_color="red", 
                      outline_width=5)
        layout.add_widget(label)
        layout.add_widget(ScrButton(screen=self, direction='left', goal='screen1', text='Перейти до екрану 1'))
        layout.add_widget(ScrButton(screen=self, direction='up', goal='screen2', text='Перейти до екрану 2'))
        self.add_widget(layout)

class Screen1(Screen):
    def __init__(self, name='screen1'):
        super().__init__(name=name)

        layout = BoxLayout(orientation='vertical')
        label = Label(text="Екран 1")
        layout.add_widget(label)

        layout.add_widget(ScrButton(screen=self, direction='right', goal='main', text='Назад на головний'))
        layout.add_widget(ScrButton(screen=self, direction='up', goal='screen2', text='До екрану 2'))

        self.add_widget(layout)

class Screen2(Screen):
    def __init__(self, name='screen2'):
        super().__init__(name=name)

        layout = BoxLayout(orientation='vertical')
        label = Label(text="Екран 2")
        layout.add_widget(label)

        layout.add_widget(ScrButton(screen=self, direction='down', goal='main', text='Назад на головний'))
        layout.add_widget(ScrButton(screen=self, direction='left', goal='screen1', text='До екрану 1'))

        self.add_widget(layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        return sm

app = MyApp()
app.run()
