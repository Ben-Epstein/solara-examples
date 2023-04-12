import itertools
from collections import defaultdict
from time import sleep
from typing import List

import solara as sl

from bulk_labeling.state import PlotState, State, reset
from bulk_labeling.utils.common import BUTTON_KWARGS
from bulk_labeling.utils.df import INTERNAL_COLS, apply_df_edits
from bulk_labeling.utils.menu import (
    add_new_label,
    assign_labels,
    get_assign_label_button_text,
    load_demo_df,
    load_file_df,
)

NO_COLOR_COLS = INTERNAL_COLS + ["text"]


@sl.component
def assigned_label_view() -> None:
    State.assigned_new_label.use()
    State.filtered_ids.use()

    if State.assigned_new_label.value:
        sl.Info(f"{len(State.filtered_ids.value)} labeled!")
        sleep(2)
        State.assigned_new_label.set(False)


@sl.component
def assign_label_button() -> None:
    btn_label, button_enabled = get_assign_label_button_text(State.df.value)
    sl.Button(
        btn_label,
        on_click=assign_labels,
        disabled=not button_enabled,
        **BUTTON_KWARGS,
    )


@sl.component
def register_new_label_button() -> None:
    # TODO: Remove when solara updates
    State.available_labels.use()
    State.chosen_label.use()

    # TODO: Make a State.available_labels.append
    sl.InputText("Register new label", on_value=add_new_label)
    if State.available_labels.value:
        sl.Select("Available labels", list(State.available_labels.value)).connect(
            State.chosen_label
        )


@sl.component
def export_edits_button() -> None:
    # TODO: Remove when solara updates
    State.labeled_ids.use()

    def clear_labels() -> None:
        State.labeled_ids.set(defaultdict(list))

    if State.labeled_ids.value:
        # Flatten all of the edits into a single set, so we know how many were edited
        num_edited = len(set(itertools.chain(*State.labeled_ids.value.values())))
        exp_df = apply_df_edits(State.df.value)
        data = exp_df.to_csv(index=False)
        with sl.Row():
            sl.FileDownload(
                data,
                label=f"Export {num_edited} labeled points",
                filename="export.csv",
            )
            sl.Button("Clear labels?", on_click=clear_labels)


@sl.component
def label_manager() -> None:
    register_new_label_button()
    assign_label_button()
    export_edits_button()


@sl.component
def file_manager() -> None:
    PlotState.color.use()
    PlotState.loading.use()

    sl.FileDrop(
        label="Drop CSV here (`text` col required)!",
        on_file=load_file_df,
        lazy=False,
    )
    # We use sl.Column to force these two buttons to be stacked instead of side-by-side
    with sl.Column():
        sl.Button(
            label="Load demo dataset",
            on_click=load_demo_df,
            **BUTTON_KWARGS,
        )
        sl.Button(label="Reset view", on_click=reset, **BUTTON_KWARGS)


@sl.component
def view_controller(avl_cols: List[str]) -> None:
    # TODO: Remove when solara updates
    PlotState.color.use()
    PlotState.point_size.use()
    State.filter_text.use()

    sl.InputText(
        "Filter by search", State.filter_text.value, on_value=State.filter_text.set
    )
    sl.Markdown("**Set point size**")
    sl.SliderInt("", PlotState.point_size.value, on_value=PlotState.point_size.set)
    # TODO: A drop down should have "remove selection" option
    #  (esp if default state is None)
    sl.Select(
        "Color by",
        [None] + avl_cols,
        PlotState.color.value,
        on_value=PlotState.color.set,
    )


@sl.component
def menu() -> None:
    State.reset_on_assignment.use()

    # avl_cols is dependent on df, so any time it changes,
    # this will automatically update
    avl_cols = [i for i in State.df.value.columns if i not in NO_COLOR_COLS]

    file_manager()
    label_manager()
    view_controller(avl_cols)
    sl.Markdown("**Reset filters on label assignment?**")
    if State.reset_on_assignment.value:
        label = "Reset"
    else:
        label = "Keep state"
    sl.Checkbox(label=label).connect(State.reset_on_assignment)
