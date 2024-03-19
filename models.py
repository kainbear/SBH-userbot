from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class UsersORM(Base):

    __tablename__ = "users"

    id: Mapped[intpk]
    created_at: Mapped[str]
    status: Mapped[str]
    status_updated_at: Mapped[str]



