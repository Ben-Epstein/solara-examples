from dataclasses import asdict, dataclass
from typing import Iterator, List

import openai
import solara as sl
from solara.alias import rv

from style import chat_css, chatbox_css


@dataclass
class Message:
    role: str
    content: str


def get_chatgpt_response(messages: List[Message]) -> Iterator[Message]:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[asdict(m) for m in messages],
        temperature=0.1,
        stream=True,
    )

    total = ""
    for chunk in response:
        part = chunk["choices"][0]["delta"].get("content", "")
        total += part
        yield Message(role="assistant", content=total)


def ChatBox(message: Message) -> None:
    # Don't show the system message here. It's in the sidebar
    if message.role == "system":
        return
    sl.Style(chatbox_css)
    align = (
        "start"
        if message.role == "assistant"
        else "center"
        if message.role == "system"
        else "end"
    )
    with sl.Column(align=align):
        with sl.Card(classes=["message", f"{message.role}-message"]):
            sl.Markdown(message.content)
        with sl.HBox(align_items="center"):
            sl.Image(f"logos/{message.role}-logo.png", classes=["avatar"])
            sl.Text(message.role.capitalize())


@sl.component
def Chat() -> None:
    sl.Style(chat_css)
    system_message = "Assist the user with whatever they need"

    messages = sl.use_reactive([Message(role="system", content=system_message)])
    input, set_input = sl.use_state("")

    # Allowing the user to modify the system message
    def update_system_message(new_msg: str) -> None:
        new_system_message = Message(role="system", content=new_msg)
        messages.set([new_system_message] + messages.value[1:])

    with sl.Sidebar():
        sl.InputText("System Message", system_message, on_value=update_system_message)

    def ask_chatgpt() -> None:
        _messages = messages.value + [Message(role="user", content=input)]
        set_input("")
        messages.set(_messages)
        for new_message in get_chatgpt_response(_messages):
            messages.set(_messages + [new_message])

    with sl.VBox():
        for message in messages.value:
            ChatBox(message)

    with sl.Row(justify="center"):
        with sl.HBox(align_items="center", classes=["chat-input"]):
            rv.Textarea(
                v_model=input,
                on_v_model=set_input,
                solo=True,
                hide_details=True,
                outlined=True,
                rows=1,
                auto_grow=True,
            )
            sl.IconButton("send", on_click=ask_chatgpt)
