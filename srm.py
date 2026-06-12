from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.animation import Animation
from datetime import datetime
import os

# 1. SPLASH SCREEN CLASS (With Realistic Opening Animation for Sm.png)
class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        
        # Background Canvas - Deep Premium Dark Theme
        with self.canvas.before:
            Color(0.05, 0.05, 0.07, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        self.layout = BoxLayout(orientation='vertical', padding=50)
        
        # Logo Setup (Sm.png file use ho rahi hai ab)
        self.logo = Image(source='Sm.png', size_hint=(None, None), size=(180, 180), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        if os.path.exists('Sm.png'):
            self.logo.opacity = 0  # Shuru me hidden rahega animation ke liye
            self.layout.add_widget(self.logo)
            
        self.add_widget(self.layout)

    def on_enter(self):
        if os.path.exists('Sm.png'):
            # Realistic Smooth Fade-in Animation (1.2 Seconds)
            anim = Animation(opacity=1, duration=1.2, t='in_out_quad')
            anim.bind(on_complete=self.start_clock)
            anim.start(self.logo)
        else:
            # Agar folder me Sm.png nahi mili toh screen skip karke direct main screen open hogi
            print("Warning: 'Sm.png' nahi mili! Direct main screen par switch ho raha hai.")
            self.switch_to_main(0)

    def start_clock(self, *args):
        Clock.schedule_once(self.switch_to_main, 0.5)

    def switch_to_main(self, dt):
        self.manager.current = 'main'

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


# 2. MAIN APPLICATION SCREEN (With Fixed Layout and Beautiful Visibility)
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        # Background Canvas - Premium Gray/Blue Backdrop
        with self.canvas.before:
            Color(0.1, 0.12, 0.16, 1) 
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        main_layout = BoxLayout(orientation='vertical', spacing=25, padding=[30, 40, 30, 40])
        
        # App Title
        title_label = Label(
            text="Age Calculator",
            font_size=28,
            bold=True,
            size_hint_y=None,
            height=40,
            color=(1, 1, 1, 1)
        )
        main_layout.add_widget(title_label)
        
        # Input Box Row Layout
        input_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=55)
        
        # Stylish Inputs
        self.day_in = TextInput(hint_text="Day", multiline=False, input_filter='int', halign='center', font_size=18, background_normal='', background_color=(0.2, 0.23, 0.28, 1), foreground_color=(1, 1, 1, 1), hint_text_color=(0.6, 0.6, 0.7, 1), padding=[0, 14, 0, 0])
        self.month_in = TextInput(hint_text="Month", multiline=False, input_filter='int', halign='center', font_size=18, background_normal='', background_color=(0.2, 0.23, 0.28, 1), foreground_color=(1, 1, 1, 1), hint_text_color=(0.6, 0.6, 0.7, 1), padding=[0, 14, 0, 0])
        self.year_in = TextInput(hint_text="Year", multiline=False, input_filter='int', halign='center', font_size=18, background_normal='', background_color=(0.2, 0.23, 0.28, 1), foreground_color=(1, 1, 1, 1), hint_text_color=(0.6, 0.6, 0.7, 1), padding=[0, 14, 0, 0])
        
        input_layout.add_widget(self.day_in)
        input_layout.add_widget(self.month_in)
        input_layout.add_widget(self.year_in)
        main_layout.add_widget(input_layout)
        
        # Premium Mint Green Button
        calculate_button = Button(
            text="Calculate Age",
            font_size=20,
            bold=True,
            size_hint_y=None,
            height=55,
            background_normal='',
            background_color=(0, 0.75, 0.45, 1),
            color=(1, 1, 1, 1)
        )
        calculate_button.bind(on_press=self.calculate_age)
        main_layout.add_widget(calculate_button)
        
        # Result Display Area
        self.result_lbl = Label(
            text="Enter details above",
            font_size=22,
            color=(0.8, 0.8, 0.85, 1),
            markup=True
        )
        main_layout.add_widget(self.result_lbl)
        
        self.add_widget(main_layout)

    def calculate_age(self, instance):
        try:
            day = int(self.day_in.text)
            month = int(self.month_in.text)
            year = int(self.year_in.text)

            dob = datetime(year, month, day)
            today = datetime.now()

            age_years = today.year - dob.year
            if (today.month, today.day) < (dob.month, dob.day):
                age_years -= 1

            self.result_lbl.text = f"🎉 [color=#00ff99][b]Age: {age_years} Years[/b][/color]"
        
        except ValueError:
            self.result_lbl.text = "[color=#ff4444]Please enter a valid date![/color]"

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


# 3. MAIN APP EXECUTION
class SrmApp(App):
    def build(self):
        # Handles transparent and realistic fade transition between screens
        sm = ScreenManager(transition=FadeTransition(duration=0.6))
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    SrmApp().run()
