from typing import List

from solara import reactive, Reactive


class Question:
    def __init__(self, q: str, a: str) -> None:
        self.q = q
        self.a = a


class State:
    question = reactive("")
    answer = reactive("<br><br><br>")
    history: Reactive[List[Question]] = reactive([])
    ans_btn_disabled = reactive(True)
    openai_key = reactive("")
