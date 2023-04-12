from typing import List

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from umap import UMAP

UMAP_MODEL = UMAP(n_neighbors=15, random_state=42, verbose=True)
ENCODER = SentenceTransformer("paraphrase-MiniLM-L3-v2")


def encode_inputs(samples: List[str]) -> np.ndarray:
    return ENCODER.encode(samples)
    # When doing rapid development, it's faster to return a numpy array
    # return np.random.rand(len(samples), 20)


def get_xy(embs: np.ndarray) -> np.ndarray:
    return UMAP_MODEL.fit_transform(embs)


def get_text_embeddings(samples: List[str]) -> np.ndarray:
    return get_xy(encode_inputs(samples))


def add_embeddings_to_df(df: pd.DataFrame) -> pd.DataFrame:
    embs = get_text_embeddings(df["text"].tolist())
    df["x"] = embs[:, 0]
    df["y"] = embs[:, 1]
    return df
