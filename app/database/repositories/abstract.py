"""
Абстрактный репозиторий от которого наследуются остальные репозитории.
"""

import abc
from typing import Generic, List, Optional, TypeVar

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Base

AbstractModel = TypeVar("AbstractModel")


class Repository(Generic[AbstractModel]):
    type_model: type[Base]
    session: AsyncSession

    def __init__(self, type_model: type[Base], session: AsyncSession):
        self.type_model = type_model
        self.session = session

    async def get(self, ident: int | str) -> AbstractModel | None:
        return await self.session.get(entity=self.type_model, ident=ident)

    async def get_by_where(self, where_clause: list) -> AbstractModel | None:
        statement = sa.select(self.type_model).where(sa.and_(*where_clause))
        return (await self.session.execute(statement)).unique().scalar_one_or_none()

    async def get_many(
        self, where_clause: list = None, limit: int = None, order_by=None
    ) -> Optional[List[AbstractModel]]:
        statement = sa.select(self.type_model).limit(limit).order_by(order_by)
        if where_clause:
            statement = statement.where(sa.and_(*where_clause))
        return (await self.session.scalars(statement)).unique().all()

    async def delete(
        self, ident: int = None, where_clauses: list[sa.ClauseElement] = None
    ) -> None:
        if where_clauses is None and ident is not None:
            where_clauses = [self.type_model.id == ident]
        statement = sa.delete(self.type_model).where(sa.and_(*where_clauses))
        await self.session.execute(statement)

    async def update(self, ident: int, **values) -> AbstractModel | None:
        statement = (
            sa.update(self.type_model)
            .values(**values)
            .where(self.type_model.id == ident)
        )
        await self.session.execute(statement)

    @abc.abstractmethod
    async def new(self, *args, **kwargs) -> None: ...
