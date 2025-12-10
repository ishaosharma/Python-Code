import pytest
@pytest.fixture
def sample_data():
    return {"name":"Amit", "role": "Developer"}



class connect_to_database:
    def __init__(self):
        self.users = set()
    def create_table(self, table_name):
        pass
    def drop_table(self, table_name):
        pass
    def disconnect(self):
        pass
    def insert_user(self, username):
        self.users.add(username)
    def get_user(self, username):
        if username in self.users:
            return {"name": username}
        return None

@pytest.fixture
def database():
    db = connect_to_database()
    db.create_table("users")
    yield db    #This is where test runs
    db.drop_table("users")
    db.disconnect()

