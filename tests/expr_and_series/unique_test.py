from __future__ import annotations

import narwhals.stable.v1 as nw
from tests.utils import Constructor
from tests.utils import ConstructorEager
from tests.utils import compare_dicts

data = {"a": [1, 1, 2]}


def test_unique_expr(constructor: Constructor) -> None:
    df = nw.from_native(constructor(data))
    result = df.select(nw.col("a").unique()).sort("a")
    expected = {"a": [1, 2]}
    compare_dicts(result, expected)


def test_unique_series(constructor_eager: ConstructorEager) -> None:
    series = nw.from_native(constructor_eager(data), eager_only=True)["a"]
    result = series.unique()
    expected = {"a": [1, 2]}
    compare_dicts({"a": result}, expected)
