# pyright: reportGeneralTypeIssues=false

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from litestar import (
    Controller,
    delete,
    get,  # pylint: disable=unused-import
    post,
    put,
)
from litestar.di import Provide
from litestar.params import Dependency
from litestar.status_codes import HTTP_200_OK

if TYPE_CHECKING:
    from uuid import UUID

    from litestar.contrib.repository.abc import FilterTypes

    from app.domain.projects.models import Service
from app.domain.projects.dependencies import provides_service
from app.domain.projects.models import Project as Model
from app.domain.projects.models import ReadDTO, WriteDTO

__all__ = ["ApiController"]


validation_skip: Any = Dependency(skip_validation=True)


class ApiController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO
    path = "/api/projects"
    dependencies = {"service": Provide(provides_service, sync_to_thread=True)}
    tags = ["Projects API"]
    DETAIL_ROUTE = "/{row_id:uuid}"

    @get()
    async def filter(self, service: "Service", filters: list["FilterTypes"] = validation_skip) -> Sequence[Model]:
        """Get a list of Models."""
        return await service.list(*filters)

    @post()
    async def create(self, data: Model, service: "Service") -> Model:
        """Create an `Model`."""
        return await service.create(data)

    @get(DETAIL_ROUTE)
    async def retrieve(self, service: "Service", row_id: "UUID") -> Model:
        """Get Model by ID."""
        return await service.get(row_id)

    @put(DETAIL_ROUTE)
    async def update(self, data: Model, service: "Service", row_id: "UUID") -> Model:
        """Update an Model."""
        return await service.update(row_id, data)

    @delete(DETAIL_ROUTE, status_code=HTTP_200_OK)
    async def delete(self, service: "Service", row_id: "UUID") -> Model:
        """Delete Author by ID."""
        return await service.delete(row_id)
