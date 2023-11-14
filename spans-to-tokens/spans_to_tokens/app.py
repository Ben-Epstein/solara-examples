import json
from json import JSONDecodeError

import solara as sl
from datasets import Dataset
import pandas as pd

from spacy_to_hf import spacy_to_hf

DEMO_OPTION = [
    {
        "text": "Planned to go to the Apple Storefront on Tuesday",
        "spans": [
            {"start": 0, "end": 7, "label": "Action"},
            {"start": 21, "end": 37, "label": "Loc"},
            {"start": 41, "end": 48, "label": "Date"},
        ],
    }
]

TOKENIZERS = [
    "bert-base-uncased",
    "bert-base-cased",
    "distilbert-base-uncased",
    "distilbert-base-cased",
    "roberta-base",
]

tokenizer = sl.reactive("bert-base-uncased")
spans = sl.reactive(json.dumps(DEMO_OPTION))
spans_checkpoint = sl.reactive("")


def try_json(span_str: str, show_warn: bool = True) -> dict:
    try:
        return json.loads(span_str)
    except JSONDecodeError as e:
        if show_warn:
            sl.Warning(f"Invalid JSON data, try again\n{str(e)}")
        return {}


@sl.component
def TokenViewer():
    with sl.Row(style={"align-items": "center"}, justify="space-between") as title_row:
        sl.Text("Token Data", style={"font-size": "1.5rem"})
    sl.v.Divider()
    if not spans_checkpoint.value:
        return
    spans_json = try_json(spans_checkpoint.value)
    if not spans_json:
        return
    try:
        token_data = spacy_to_hf(spans_json, tokenizer.value)
        data = pd.DataFrame(token_data).to_csv()
        title_row.add_children(
            [
                sl.FileDownload(
                    data,
                    filename="token_data.csv",
                    icon_name="mdi-download",
                    label="Download",
                )
            ]
        )
        for key in token_data.keys():
            with sl.Row(gap="5px", style={"flex-wrap": "wrap", "row-gap": "5px"}):
                # I'm not sure why this is double wrapped in a list?
                for token in token_data[key][0]:
                    sl.v.Chip(
                        children=[token], color="primary" if key == "tokens" else None
                    )
    except Exception as e:
        print(type(e))
        sl.Error(f"Failed to create tokens and tags: {str(e)}")


@sl.component
def SpanJson():
    print(f"\n\n{spans.value}\n\n")
    spans_json = try_json(spans.value, show_warn=False)
    show_spans = json.dumps(spans_json, indent=4) if spans_json else spans.value
    sl.Markdown(f"```json\n{show_spans}\n```", style={"padding": "0"})


@sl.component
def Options():
    sl.Text("Enter Your Data", style={"font-size": "1.5rem"})
    sl.v.Divider()
    sl.Select("Pick your tokenizer", TOKENIZERS, tokenizer)
    sl.MarkdownEditor(
        value=f"```json\n{spans.value}\n```",
        on_value=lambda spans_str: spans.set(
            spans_str.lstrip("```json\n").rstrip("\n```")
        ),
    )
    sl.Button("Convert to tokens", on_click=lambda: spans_checkpoint.set(spans.value))
    SpanJson()


@sl.component
def Page():
    with sl.Columns([1, 1]):
        Options()
        TokenViewer()
    sl.Style(
        """.solara-markdown{max-width: unset;}
            .solara-milkdown .milkdown-menu{display: none;}"""
    )
