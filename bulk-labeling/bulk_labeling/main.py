import solara as sl

from bulk_labeling.components.df import DFView, NoEmbs
from bulk_labeling.components.menu import AssignedLabelView, Menu
from bulk_labeling.state import PlotState, State
from bulk_labeling.utils.df import has_df


@sl.component
def NoDF() -> None:
    with sl.Columns([1, 1]):
        sl.Markdown("## DataFrame (Load Data)")
        sl.Markdown("## Embeddings (Load Data)")


@sl.component
def Page() -> None:
    sl.Title("Bulk Labeling!")
    # TODO: Why cant i get this view to render?
    AssignedLabelView()
    with sl.Sidebar():
        Menu()
    if has_df(State.df.value) and PlotState.loading.value:
        NoEmbs()
    elif has_df(State.df.value):
        DFView()
    else:
        NoDF()


if __name__ == "__main__":
    Page()
