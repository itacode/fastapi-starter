from pydantic import BaseModel
from sqlalchemy import select

import app.entities.orm.orm_model as orm
from app.database import db_session
from app.entities.user import User


class UsersService:
    class GetUsersRes(BaseModel):
        users: list[User]

    def get_users(self) -> GetUsersRes:
        with db_session.begin() as session:
            stmt = select(orm.User).where(orm.User.is_deleted == 0)
            orm_users = session.scalars(stmt)

            users: list[User] = []
            for orm_user in orm_users:
                users.append(User.model_validate(orm_user))

        return self.GetUsersRes(users=users)
