from typing import List

from solara.lab import Reactive


class Question:
    def __init__(self, q: str, a: str) -> None:
        self.q = q
        self.a = a


class State:
    question = Reactive[str]("")
    answer = Reactive[str]("<br><br><br>")
    history = Reactive[List[Question]]([])
    ans_btn_disabled = Reactive[bool](True)
    openai_key = Reactive[str]("")
