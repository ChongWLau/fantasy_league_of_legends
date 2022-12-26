from typing import List, Tuple

import structlog
from buildpg import V, Values, render

logger = structlog.getLogger()


def build_insert(table: V, values: Values) -> Tuple[str, List]:
    """
    Build a SQL INSERT string for a given a table and column values
    Args:
        table (V): buildpg V object
        values (Values): buildpg Values object
    Returns:
        Tuple[str, List]: A tuple containing SQL template str and
            list of values to merge
    """
    sql = "INSERT INTO :table (:values__names) VALUES :values RETURNING *"
    return render(sql, table=table, values=values)
