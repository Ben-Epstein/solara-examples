import io
import os
from typing import Callable, Tuple

import pandas as pd
from solara.components.file_drop import FileInfo

from bulk_labeling.state import PlotState, State, reset
from bulk_labeling.utils.df import filtered_df, has_df, load_df
from bulk_labeling.utils.ml import add_embeddings_to_df

DIR = f"{os.getcwd()}/bulk_labeling"
PATH = f"{DIR}/conv_intent.csv"


def add_new_label(new_label: str) -> None:
    if not new_label:
        return
    all_labels = State.available_labels.value.copy()
    all_labels.add(new_label)
    State.available_labels.set(all_labels)
    # So the "assign points" button is already pre-populated with your new label =]
    State.chosen_label.set(new_label)


def assign_labels(df: pd.DataFrame) -> None:
    labeled_ids = State.labeled_ids.value.copy()
    new_ids = df["id"].tolist()
    if State.chosen_label.value:
        print(f"Setting {State.chosen_label.value} for {len(new_ids)} points")
        labeled_ids[State.chosen_label.value].extend(new_ids)
    State.labeled_ids.set(labeled_ids)
    # State.assigned_new_label.set(True)
    # Reset the view so no points are selected
    if State.reset_on_assignment.value:
        reset()


def get_assign_label_button_text(df: pd.DataFrame) -> Tuple[str, bool]:
    """Gets the label for the "assign label" button, and whether it's enabled"""
    button_enabled = bool(State.chosen_label.value) and has_df(df)
    fdf = filtered_df(df)
    num = len(fdf) if len(fdf) != len(df) else "all"
    if button_enabled:
        btn_label = f"Assign {num} points to label {State.chosen_label.value}"
    elif not has_df(df):
        btn_label = "Add data"
    elif not State.available_labels.value:
        btn_label = "Create a label"
    else:
        btn_label = "Choose a label"
    return btn_label, button_enabled


def load_demo_df(set_df: Callable) -> None:
    new_df = load_df(PATH)
    set_df(new_df)


def load_file_df(file: FileInfo, set_df: Callable) -> None:
    if not file["data"]:
        return
    new_df = load_df(io.BytesIO(file["data"]))
    # Set it before embeddings so the user can see the df while embeddings load
    PlotState.loading.set(True)
    set_df(new_df)
    new_df = add_embeddings_to_df(new_df)
    # Set it again after embeddings so we can render the plotly graph
    set_df(new_df)
    PlotState.loading.set(False)
