import solara as sl
import solara.lab as slab

from bulk_labeling.components.df import DFView, NoEmbs
from bulk_labeling.components.menu import Menu
from bulk_labeling.label_stats import LabelStats
from bulk_labeling.state import PlotState, State
from bulk_labeling.utils.df import has_df


@sl.component
def NoDF() -> None:
    with sl.Column(align="center"):
        sl.Markdown("# No Data Loaded")
        sl.Markdown("*Please load some data using the sidebar to get started*")


@sl.component
def LabelWorkspace() -> None:
    sl.Title("Bulk Labeling!")
    # TODO: Why cant i get this view to render?
    # AssignedLabelView()
    with sl.Sidebar():
        Menu()
    if has_df(State.df.value) and PlotState.loading.value:
        NoEmbs()
    elif has_df(State.df.value):
        DFView()
    else:
        NoDF()


@sl.component
def Page() -> None:
    with slab.Tabs(align="center"):
        with slab.Tab("Label Workbench"):
            LabelWorkspace()
        with slab.Tab("Label Stats", disabled=len(State.df.value) == 0):
            LabelStats()


if __name__ == "__main__":
    Page()
