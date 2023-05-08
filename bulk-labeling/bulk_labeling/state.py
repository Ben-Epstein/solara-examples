from collections import defaultdict
from typing import Dict, List, Set

import pandas as pd
from solara import Reactive, reactive

DEFAULT_POINT_SIZE = 2


class State:
    available_labels: Reactive[Set[str]] = reactive(set())
    labeled_ids: Reactive[Dict[str, List[int]]] = reactive(defaultdict(list))
    filtered_ids: Reactive[List[int]] = reactive([])
    chosen_label = reactive("")
    assigned_new_label = reactive(False)
    filter_text = reactive("")
    reset_on_assignment = reactive(True)
    df = reactive(pd.DataFrame({}))


class PlotState:
    point_size = reactive(DEFAULT_POINT_SIZE)
    color = reactive("")
    # While we calculate embeddings and UMAP, we can manage the loading state
    loading = reactive(False)


def reset() -> None:
    """Removes any filters applied to the data"""
    State.filtered_ids.set([])
    State.filter_text.set("")
    State.chosen_label.set("")
    PlotState.point_size.set(DEFAULT_POINT_SIZE)
    PlotState.color.set("")
