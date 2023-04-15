import reacton.ipyvuetify as v
import requests
import solara as sl

from card_viewer.utils import format_readme

MODELS = [
    "bert-base-cased",
    "bert-base-uncased",
    "google/bigbird-roberta-large",
    "stabilityai/stable-diffusion-2-1",
]
DATASETS = ["wikipedia", "wikitext", "glue"]
README_TEMPLATE = "https://huggingface.co/{asset}/raw/main/README.md"


@sl.component
def ShowCard(asset: str):
    if not asset:
        sl.Markdown("# Choose Model or Dataset to view card")
        return
    is_dataset = asset in DATASETS
    if is_dataset:
        asset = f"datasets/{asset}"
    url = README_TEMPLATE.format(asset=asset)
    readme = requests.get(url).text
    with sl.Card():
        format_readme(readme)


@sl.component
def Page():
    asset, set_asset = sl.use_state("")

    assets = MODELS + DATASETS
    with sl.Columns([1, 3]):
        sl.Select("model/dataset", assets, asset, on_value=set_asset)
        ShowCard(asset)
