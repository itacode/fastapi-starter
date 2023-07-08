from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_deleted: Optional[bool] = None
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
