from __future__ import annotations

from datetime import datetime
from typing import Any

import pandas as pd
import polars as pl
import pytest

import narwhals as nw
from tests.utils import compare_dicts

df_pandas = pd.DataFrame(
    {
        "a": [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)],
        "b": [4, 4, 6],
        "z": [7.0, 8, 9],
    }
)
df_polars = pl.DataFrame(
    {
        "a": [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)],
        "b": [4, 4, 6],
        "z": [7.0, 8, 9],
    }
)
df_lazy = pl.LazyFrame(
    {
        "a": [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)],
        "b": [4, 4, 6],
        "z": [7.0, 8, 9],
    }
)


@pytest.mark.parametrize("df_raw", [df_pandas, df_lazy])
def test_any_all(df_raw: Any) -> None:
    df = nw.LazyFrame(df_raw)
    result = nw.to_native(df.select(nw.col("a").dt.year()))
    expected = {"a": [2020, 2020, 2020]}
    compare_dicts(result, expected)
