from typing import Dict, List

import pandas as pd
import plotly.express as px
from plotly.graph_objs._figure import Figure


def find_row_ids(fig: Figure, click_data: Dict) -> List[int]:
    """A very annoying function to get row IDs because Plotly is unhelpful

    Solara is going to do this for us in the future!
    """
    # goes from trace index and point index to row index in a dataframe
    # requires passing df.index as to custom_data
    trace_index = click_data["points"]["trace_indexes"]
    point_index = click_data["points"]["point_indexes"]
    point_ids = []
    for t, p in zip(trace_index, point_index):
        point_trace = fig.data[t]
        point_ids.append(point_trace.customdata[p][0])
    return point_ids


def create_plotly_figure(df: pd.DataFrame, color: str, point_size: int) -> Figure:
    # We pass in df.id to custom_data so we can get back the correct points on a
    # lasso selection. Plotly makes this difficult
    # TODO: Solara will wrap and handle all of this logic for us in the future
    fig = px.scatter(
        df,
        x="x",
        y="y",
        color=color or None,
        custom_data=[df["id"]],
        hover_data=["hovertext"],
    )
    fig.update_layout(showlegend=False)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.update_traces(marker_size=point_size)
    return fig
