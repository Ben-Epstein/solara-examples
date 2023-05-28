import solara as sl

from bulk_labeling.state import State


@sl.component
def LabelStats() -> None:
    df_len = len(State.df.value)
    pct_labeled = (100 * len(State.labeled_ids.value) / df_len) if df_len else 0
    with sl.Row(justify="center"):
        sl.Card(f"{df_len} samples")
        sl.Card(f"{pct_labeled}% labeled")
        sl.Card(f"{len(State.available_labels.value)} labels")
