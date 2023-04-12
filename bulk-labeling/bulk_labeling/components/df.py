import pandas as pd
import solara as sl
from reacton import ipyvuetify as V

from bulk_labeling.state import PlotState, State
from bulk_labeling.utils.df import INTERNAL_COLS, filtered_df
from bulk_labeling.utils.plotly import create_plotly_figure, find_row_ids


@sl.component
def _emb_loading_state() -> None:
    sl.Markdown("## Embeddings")
    sl.Markdown("Loading your embeddings. Enjoy this fun animation for now")
    V.ProgressLinear(indeterminate=True)


@sl.component
def no_embs(df: pd.DataFrame) -> None:
    with sl.Columns([1, 1]):
        table(filtered_df(df))
        _emb_loading_state()


@sl.component
def embeddings(df: pd.DataFrame, color: str, point_size: int) -> None:
    State.filtered_ids.use()

    sl.Markdown("## Embeddings")
    fig = create_plotly_figure(df, color, point_size)

    # Plotly returns data in a weird way, we just want the ids
    # TODO: Solara to handle :)
    set_point_ids = lambda data: State.filtered_ids.set(  # noqa: E731
        find_row_ids(fig, data)
    )
    sl.FigurePlotly(fig, on_selection=set_point_ids)


@sl.component
def table(df: pd.DataFrame) -> None:
    sl.Markdown(f"## Data ({len(df):,} points)")
    sl.DataFrame(df[[i for i in df.columns if i not in INTERNAL_COLS]])


@sl.component
def df_view(df: pd.DataFrame) -> None:
    # TODO: Remove when solara updates
    PlotState.point_size.use()
    PlotState.color.use()
    # We need these because of the `filtered_df` call.
    # next itertation we will move the df into global state (solara blocking)
    # and then filtered_df becomes always up to date
    State.filtered_ids.use()
    State.filter_text.use()

    fdf = filtered_df(df)

    with sl.Columns([1, 1]):
        table(fdf)
        embeddings(fdf, PlotState.color.value, PlotState.point_size.value)
