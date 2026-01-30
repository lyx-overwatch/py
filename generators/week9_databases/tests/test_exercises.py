from generators.week9_databases.exercises import get_engine, create_tables, get_session, add_user, get_user


def test_db_crud():
    engine = get_engine()
    create_tables(engine)
    sess = get_session(engine)
    u = add_user(sess, "alice")
    assert u.id is not None
    assert get_user(sess, u.id).name == "alice"
