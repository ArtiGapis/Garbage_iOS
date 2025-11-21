from toga.app import App
from toga import Label
from toga import MainWindow

class MyApp(App):
    def startup(self):
        self.window = MainWindow(title="BeeWare Python App")
        self.label = Label("Hello from Python on iOS!")
        self.window.content = self.label
        self.window.show()

def main():
    return MyApp()
