import openai

from .state import Question, State


def make_request(q: str) -> str:
    openai.api_key = State.openai_key.value
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": q},
        ],
    )
    return res.choices[0].message.content


def query_gpt() -> None:
    if not State.openai_key.value:
        return
    ans = make_request(State.question.value)
    State.answer.set(ans)
    # Enable the save button
    State.ans_btn_disabled.set(False)


def save_answer() -> None:
    q = Question(q=State.question.value, a=State.answer.value)
    hist = State.history.value.copy()
    hist.append(q)
    State.history.set(hist)


def get_table_rows() -> str:
    table_rows = ""
    for question in State.history.value:
        table_rows += f"<tr>\n\t<td>{question.q}</td>\n\t<td>{question.a}</td>\n</tr>"
    return table_rows
