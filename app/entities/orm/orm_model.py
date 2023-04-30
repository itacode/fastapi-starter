# coding: utf-8
from datetime import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    username: Mapped[str]
    email: Mapped[str]
    is_deleted: Mapped[bool] = mapped_column(server_default=text("'0'"))
    create_time: Mapped[datetime] = mapped_column(DATETIME(fsp=6), server_default=text("CURRENT_TIMESTAMP(6)"))
    update_time: Mapped[datetime] = mapped_column(
        DATETIME(fsp=6), server_default=text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)")
    )

    posts: Mapped[list["Post"]] = relationship(back_populates="user")


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    is_deleted: Mapped[bool] = mapped_column(server_default=text("'0'"))
    create_time: Mapped[datetime] = mapped_column(DATETIME(fsp=6), server_default=text("CURRENT_TIMESTAMP(6)"))
    update_time: Mapped[datetime] = mapped_column(
        DATETIME(fsp=6), server_default=text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)")
    )

    user: Mapped["User"] = relationship(back_populates="posts")
