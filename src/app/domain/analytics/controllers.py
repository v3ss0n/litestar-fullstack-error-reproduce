"""User Account Controllers."""
from __future__ import annotations

from typing import TYPE_CHECKING

from litestar import Controller, get
from litestar.di import Provide

from app.domain import urls
from app.domain.accounts.guards import requires_active_user
from app.domain.analytics.dependencies import provides_analytic_queries
from app.lib import log
from app.utils import paginated

from .schemas import NewUsersByWeek

if TYPE_CHECKING:
    from litestar.pagination import OffsetPagination

    from app.lib.db.base import SQLAlchemyAiosqlQueryManager


__all__ = ["StatsController"]


logger = log.get_logger()


class StatsController(Controller):
    """Various system queries."""

    tags = ["Statistics"]
    guards = [requires_active_user]
    dependencies = {
        "analytic_queries": Provide(provides_analytic_queries),
    }

    @get(
        operation_id="StatsWeeklyNewUsers",
        name="stats:weekly-new-users",
        path=urls.STATS_WEEKLY_NEW_USERS,
        summary="Weekly New Users",
        description="List New Users by Week.",
        cache=1000,
    )
    async def weekly_new_users(
        self, analytic_queries: SQLAlchemyAiosqlQueryManager
    ) -> OffsetPagination[NewUsersByWeek]:
        """New Users by week."""
        results = await analytic_queries.select("users_by_week")
        return paginated(NewUsersByWeek, results)