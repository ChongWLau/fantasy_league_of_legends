from typing import List, Tuple
import structlog
import uuid

import asyncpg
from buildpg import V, Values, clauses, render

from fantasy_league_of_legends import models

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


def build_select(
    select: clauses.Select,
    table: V,
    where: clauses.Where,
):
    sql = ":select FROM :table :where"
    return render(sql, select=select, table=table, where=where)


async def create_team(conn: asyncpg.connection.Connection, data: dict):
    values = Values(
        **data, id=uuid.uuid4()
    )

    sql, values = build_insert(
        table=V("fantasy_team"),
        values=values,
    )

    team = await conn.fetch(sql, *values)

    return models.ReadTeam(**team[0])
