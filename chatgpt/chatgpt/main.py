import solara as sl

from chat import Chat
from style import main_css


@sl.component
def Page() -> None:
    sl.Style(main_css)
    with sl.VBox(classes=["main"]):
        sl.HTML(tag="h1", style="margin: auto;", unsafe_innerHTML="ChatGPT in Solara")

        Chat()


Page()
