from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime
import os

class AgeCalculatorApp(App):
    def build(self):
        # Main Layout: Saare elements ko vertical line me set karne ke liye
        layout = BoxLayout(orientation='vertical', spacing=15, padding=20)

        # 1. APP LOGO (Safe Loading)
        # Agar logo.png folder me hogi toh dikhegi, nahi toh app bina crash huye chalega
        if os.path.exists('logo.png'):
            logo = Image(source='logo.png', size_hint=(1, 0.25))
            layout.add_widget(logo)
        else:
            # Agar logo nahi mila toh console me bas ek reminder dikhega
            print("Reminder: 'logo.png' nahi mili, isliye logo skip ho gaya.")

        # 2. APP TITLE (Logo ke thik niche)
        title_label = Label(
            text="Age Calculator",
            font_size=32,
            bold=True,
            size_hint=(1, 0.1)
        )
        layout.add_widget(title_label)

        # Horizontal Layout: Day, Month, Year ko ek hi line (row) me lane ke liye
        input_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.15))

        # 3. CLEAN & COMPACT INPUT BOXES (Sirf numbers allow karne ke liye)
        self.day_input = TextInput(
            hint_text="Day",
            multiline=False,
            input_filter='int', # Isse user sirf numbers type kar payega
            halign='center'
        )
        self.month_input = TextInput(
            hint_text="Month",
            multiline=False,
            input_filter='int',
            halign='center'
        )
        self.year_input = TextInput(
            hint_text="Year",
            multiline=False,
            input_filter='int',
            halign='center'
        )

        # Inputs ko horizontal layout me add kar rahe hain
        input_layout.add_widget(self.day_input)
        input_layout.add_widget(self.month_input)
        input_layout.add_widget(self.year_input)
        
        # Fir us horizontal layout ko main vertical layout me dal rahe hain
        layout.add_widget(input_layout)

        # 4. GREEN CALCULATE BUTTON (Fixed Color Transition)
        calculate_button = Button(
            text="Calculate Age",
            font_size=20,
            background_normal='',       # Default grey texture hatane ke liye (Crucial line!)
            background_color=(0, 1, 0, 1), # Pure Bright Green
            size_hint=(1, 0.15)
        )
        # Button click karne par color change (Darker Green on press)
        calculate_button.background_down = ''
        calculate_button.background_color_down = (0, 0.7, 0, 1)
        
        # Button ko logic se bind karna
        calculate_button.bind(on_press=self.calculate_age)
        layout.add_widget(calculate_button)

        # 5. BIG & ATTRACTIVE RESULT LABEL
        self.result_label = Label(
            text="Your age will appear here",
            font_size=24,
            markup=True, # Custom styling bold/color tags ke liye
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.result_label)

        return layout

    # Age Calculate Karne Ka Logic
    def calculate_age(self, instance):
        try:
            # Inputs se text nikal kar integer me badalna
            day = int(self.day_input.text)
            month = int(self.month_input.text)
            year = int(self.year_input.text)

            # Date of Birth aur Aaj ki date compare karna
            dob = datetime(year, month, day)
            today = datetime.now()

            age_years = today.year - dob.year
            # Agar is saal abhi tak birthday nahi aaya hai toh 1 saal minus karein
            if (today.month, today.day) < (dob.month, dob.day):
                age_years -= 1

            # Output screen par display karein ([b] se text bold dikhega)
            self.result_label.text = f"🎂 [b]Your Age is {age_years} Years[/b]"
        
        except ValueError:
            # Agar inputs khali hain ya galat date daali hai
            self.result_label.text = "⚠️ [color=#ff0000]Please enter a valid date![/color]"

if __name__ == '__main__':
    AgeCalculatorApp().run()
