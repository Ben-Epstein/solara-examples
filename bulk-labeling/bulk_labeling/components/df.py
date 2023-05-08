import pandas as pd
import solara as sl

from bulk_labeling.state import PlotState, State
from bulk_labeling.utils.df import INTERNAL_COLS, filtered_df
from bulk_labeling.utils.plotly import create_plotly_figure, find_row_ids


@sl.component
def EmbLoadingState() -> None:
    sl.Markdown("## Embeddings")
    sl.Markdown("Loading your embeddings. Enjoy this fun animation for now")
    sl.ProgressLinear(True, color="purple")


@sl.component
def NoEmbs() -> None:
    with sl.Columns([1, 1]):
        Table(filtered_df(State.df.value))
        EmbLoadingState()


@sl.component
def Embeddings(df: pd.DataFrame, color: str, point_size: int) -> None:
    sl.Markdown("## Embeddings")
    fig = create_plotly_figure(df, color, point_size)

    # Plotly returns data in a weird way, we just want the ids
    # TODO: Solara to handle :)
    set_point_ids = lambda data: State.filtered_ids.set(  # noqa: E731
        find_row_ids(fig, data)
    )
    sl.FigurePlotly(fig, on_selection=set_point_ids)


@sl.component
def Table(df: pd.DataFrame) -> None:
    sl.Markdown(f"## Data ({len(df):,} points)")
    sl.DataFrame(df[[i for i in df.columns if i not in INTERNAL_COLS]])


@sl.component
def DFView() -> None:
    fdf = filtered_df(State.df.value)

    with sl.Columns([1, 1]):
        Table(fdf)
        Embeddings(fdf, PlotState.color.value, PlotState.point_size.value)
