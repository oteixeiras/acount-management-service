from sqlalchemy.orm import DeclarativeBase

from acount_management_service.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
