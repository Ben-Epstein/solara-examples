import solara as sl

from gpt.state import State
from gpt.style import BUTTON_CSS, HTML_TABLE, TABLE_CSS
from gpt.utils import get_table_rows, query_gpt, save_answer


@sl.component
def qa() -> None:
    sl.Markdown('<h1 style="text-align: center;">Ask GPT</h1>')
    sl.InputText(
        "Ask your question",
        value="",
        on_value=State.question.set,
        continuous_update=True,
    )
    # Cant hit the button without adding an openai key
    need_tooltip = not State.openai_key.value
    if need_tooltip:
        with sl.Tooltip("Add OpenAI API Key to ask a question"):
            sl.Button("Get Answer", on_click=query_gpt, classes=["mybutton"])
    else:
        sl.Button("Get Answer", on_click=query_gpt, classes=["mybutton"])
    with sl.Card():
        sl.Markdown(State.answer.value)
    sl.Button(
        "Save Answer",
        on_click=save_answer,
        disabled=State.ans_btn_disabled.value,
        classes=["mybutton"],
    )
    sl.Style(BUTTON_CSS)


@sl.component
def history() -> None:
    sl.Markdown('<h1 style="text-align: center;">Saved Q&A</h1><br>')
    sl.Markdown("---")
    html = HTML_TABLE.format(table_rows=get_table_rows())
    sl.HTML(tag="div", unsafe_innerHTML=html, classes=["center"])
    sl.Markdown("---")
    sl.Style(TABLE_CSS)


@sl.component
def sidebar() -> None:
    sl.InputText("OpenAI API Key", password=True, on_value=State.openai_key.set)


@sl.component
def Page() -> None:
    sl.Title("Ask GPT")
    with sl.Column():
        with sl.Card():
            qa()
        with sl.Card():
            history()
    with sl.Sidebar():
        sidebar()


if __name__ == "__main__":
    Page()
