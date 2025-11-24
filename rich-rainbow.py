from random import randint

from rich import print
from rich.highlighter import Highlighter
from rich.panel import Panel

class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({randint(0, 30)})", index, index + 1)

rainbow = RainbowHighlighter()
print(Panel(rainbow("I must not fear. Fear is the mind-killer.")))
