import pytest

from app.api.endpoints.users.users_service import UsersService
from tests.data_helper import DataHelper

data_helper = DataHelper()
users_service = UsersService()


def insert_data():
    data_helper.insert_from_csv("user", "api/service/users_service/user.csv")


def delete_data():
    data_helper.delete_all_rows("user")


@pytest.fixture(scope="function")
def fix_test_data(request: pytest.FixtureRequest):
    delete_data()
    insert_data()
    request.addfinalizer(delete_data)


class TestUsersService:
    def test_get_users(self, fix_test_data):
        result = users_service.get_users()
        assert len(result.users) == 1
