from io import BytesIO
from typing import Union

import pandas as pd

from bulk_labeling.state import State

INTERNAL_COLS = ["x", "y", "hovertext", "id"]


def has_df(df: pd.DataFrame) -> bool:
    return (len(df) != 0) and (len(df.columns) != 0)


def filtered_df(df: pd.DataFrame) -> pd.DataFrame:
    dfc = df.copy()
    if not has_df(dfc):
        return dfc
    if State.filtered_ids.value:
        dfc = dfc[dfc["id"].isin(State.filtered_ids.value)]
    if State.filter_text.value:
        dfc = dfc[dfc["text"].str.contains(State.filter_text.value)]
    return dfc


def set_default_cols(df: pd.DataFrame) -> pd.DataFrame:
    df["text_length"] = df.text.str.len()
    df["id"] = list(range(len(df)))
    df["hovertext"] = df.text.str.wrap(30).str.replace("\n", "<br>")
    return df


def load_df(data: Union[str, BytesIO]) -> pd.DataFrame:
    new_df = pd.read_csv(data)
    new_df = set_default_cols(new_df)
    return new_df


def apply_df_edits(df: pd.DataFrame) -> pd.DataFrame:
    print("Should be downloading!")
    df2 = df.copy()
    labeled_ids = State.labeled_ids.value
    # Map every ID to it's assigned labels
    # TODO: We can be smarter with conflicts and pick the label that an ID is
    #  assigned to most frequently
    id_label = {id_: label for label, ids in labeled_ids.items() for id_ in ids}
    df2["label"] = df2["id"].apply(lambda id_: id_label.get(id_, "-1"))
    df2 = df2[df2["label"] != "-1"]
    cols = [c for c in df2.columns if c not in INTERNAL_COLS]
    return df2[cols]
