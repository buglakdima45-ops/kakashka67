from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import math

# Налаштування широкого вікна
Window.size = (750, 550)
Window.clear_color = (0.05, 0.05, 0.05, 1)


class CalculatorApp(App):
    def build(self):
        self.title = "Pro Wide Murchik Calculator"

        # Головний вертикальний контейнер
        root = BoxLayout(orientation='vertical', spacing=10, padding=15)

        # 1. ЕКРАН (Дисплей)
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right",
            font_size=45, background_color=(0, 0, 0, 1),
            foreground_color=(1, 1, 1, 1), size_hint_y=0.2,
            padding=(15, 25, 15, 10), cursor_color=(0, 0, 0, 0),
            background_normal=''
        )
        root.add_widget(self.solution)

        # 2. СІТКА КНОПОК (6 стовпчиків)
        buttons_layout = GridLayout(cols=6, spacing=8, size_hint_y=0.7)

        # Розкладка: π під 3, ) під +, % поруч
        buttons = [
            ["7", "8", "9", "/", "sin", "cos"],
            ["4", "5", "6", "*", "tan", "cot"],
            ["1", "2", "3", "-", "log", "ln"],
            ["0", ".", "π", "+", "^", "√"],
            ["C", "<-", "(", ")", "%", "x²"],
            ["e", "", "", "", "", ""]
        ]

        for row in buttons:
            for label in row:
                if label == "": continue

                # Кольори: Зелений для математики, Червоний для видалення, Чорний для цифр
                if label in ["/", "*", "-", "+", "^", "√", "x²", "(", ")", "sin", "cos", "tan", "cot", "log", "ln", "e",
                             "%"]:
                    bg_color = (0, 0.6, 0.2, 1)
                elif label == "C" or label == "<-":
                    bg_color = (0.7, 0.1, 0.1, 1)
                else:
                    bg_color = (0.15, 0.15, 0.15, 1)

                btn = Button(
                    text=label, font_size=22, color=(1, 1, 1, 1),
                    background_normal='', background_color=bg_color
                )
                btn.bind(on_press=self.on_button_press)
                buttons_layout.add_widget(btn)

        root.add_widget(buttons_layout)

        # 3. КНОПКА РЕЗУЛЬТАТУ
        equals_button = Button(
            text="=", font_size=40, color=(1, 1, 1, 1),
            size_hint_y=0.15, background_normal='',
            background_color=(0, 0.5, 0.15, 1)
        )
        equals_button.bind(on_press=self.on_solution)
        root.add_widget(equals_button)

        Window.bind(on_key_down=self._on_keyboard_down)
        return root

    def _add_to_screen(self, val):
        current = self.solution.text
        # Якщо на екрані "МУРЧІК", очищаємо його перед введенням нового
        if current == "МУРЧІК":
            self.solution.text = ""
            current = ""

        if val == "C":
            self.solution.text = ""
        elif val == "<-":
            self.solution.text = current[:-1]
        elif val == "x²":
            self.solution.text += "**2"
        elif val == "^":
            self.solution.text += "**"
        elif val in ["sin", "cos", "tan", "cot", "√", "log", "ln"]:
            char = "√(" if val == "√" else f"{val}("
            self.solution.text += char
        else:
            self.solution.text += val

    def on_button_press(self, instance):
        self._add_to_screen(instance.text)

    def on_solution(self, instance=None):
        expr = self.solution.text
        if expr:
            try:
                # Авто-закриття дужок
                open_b = expr.count("(")
                close_b = expr.count(")")
                if open_b > close_b:
                    expr += ")" * (open_b - close_b)

                # Заміна для обчислень
                expr = expr.replace("√", "sqrt").replace("π", "math.pi")
                expr = expr.replace("e", "math.e").replace("log", "math.log10")
                expr = expr.replace("ln", "math.log").replace("%", "/100")

                calc_env = {
                    "math": math,
                    "sqrt": math.sqrt,
                    "sin": lambda x: math.sin(math.radians(x)),
                    "cos": lambda x: math.cos(math.radians(x)),
                    "tan": lambda x: math.tan(math.radians(x)),
                    "cot": lambda x: 1 / math.tan(math.radians(x)) if math.tan(math.radians(x)) != 0 else float('inf'),
                    "__builtins__": None
                }

                res = eval(expr, calc_env)
                self.solution.text = f"{res:g}"
            except Exception:
                # ЗАМІНА ERROR НА МУРЧІК
                self.solution.text = "МУРЧІК"

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 42:  # Backspace
            self._add_to_screen("<-")
        elif keycode == 40:  # Enter
            self.on_solution()
        elif text and (text.isdigit() or text in "+-*/().%e"):
            self._add_to_screen(text)
        return True


if __name__ == '__main__':
    CalculatorApp().run()
