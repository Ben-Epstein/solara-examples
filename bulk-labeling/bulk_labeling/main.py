import solara as sl

from bulk_labeling.components.df import df_view, no_embs
from bulk_labeling.components.menu import assigned_label_view, menu
from bulk_labeling.state import PlotState, State
from bulk_labeling.utils.df import has_df


@sl.component
def no_df() -> None:
    with sl.Columns([1, 1]):
        sl.Markdown("## DataFrame (Load Data)")
        sl.Markdown("## Embeddings (Load Data)")


@sl.component
def Page() -> None:
    sl.Title("Bulk Labeling!")
    # TODO: Why cant i get this view to render?
    assigned_label_view()
    with sl.Sidebar():
        menu()
    if has_df(State.df.value) and PlotState.loading.value:
        no_embs()
    elif has_df(State.df.value):
        df_view()
    else:
        no_df()


if __name__ == "__main__":
    Page()
