def test_database_operation(database):
    database.insert_user("John")
    user = database.get_user("John")
    assert user is not None
    