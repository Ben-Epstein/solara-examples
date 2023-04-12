from typing import cast

import pandas as pd
import solara as sl

from bulk_labeling.components.df import df_view, no_embs
from bulk_labeling.components.menu import assigned_label_view, menu
from bulk_labeling.state import PlotState
from bulk_labeling.utils.df import has_df


@sl.component
def no_df() -> None:
    with sl.Columns([1, 1]):
        sl.Markdown("## DataFrame (Load Data)")
        sl.Markdown("## Embeddings (Load Data)")


@sl.component
def Page() -> None:
    # TODO: Remove when solara updates
    # PlotState.loading.use()

    # This `eq` makes it so every time we set the dataframe, solara thinks it's new
    df, set_df = sl.use_state(
        cast(pd.DataFrame, pd.DataFrame({})), eq=lambda *args: False
    )
    sl.Title("Bulk Labeling!")
    # TODO: Why cant i get this view to render?
    assigned_label_view()
    with sl.Sidebar():
        menu(df, set_df)
    if has_df(df) and PlotState.loading.value:
        no_embs(df)
    elif has_df(df):
        df_view(df)
    else:
        no_df()


if __name__ == "__main__":
    Page()
