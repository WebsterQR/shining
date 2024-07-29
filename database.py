# pylint: disable=line-too-long

import psycopg2
import config


class COLUMNS:
    chat_id = "chat_id"
    name = "user_name"
    login = "login"
    notifications = "notifications"
    is_test = "is_test"


def database_connect():
    try:
        print('1')
        conn = psycopg2.connect(database=config.POSTGRESQL.database,
                                user=config.POSTGRESQL.user,
                                password=config.POSTGRESQL.password,
                                host=config.POSTGRESQL.host)
        print('CONNECTION SUCCESSFUL')
    except psycopg2.Error as e:
        print(e.diag.message_primary)
        conn = False

    return conn


def connection_info():
    database_connect()


def check_user_already_exist(chat_id: int) -> bool:
    with database_connect() as conn:
        cursor = conn.cursor()
        query = f" SELECT * FROM {config.POSTGRES_TABLES.users} WHERE {COLUMNS.chat_id}={chat_id}"
        cursor.execute(query=query)
        data = cursor.fetchall()
        print(data)
        if len(data) == 0:
            return False
        return True


def add_user(chat_id: int, name: str, login: str) -> None:
    with database_connect() as conn:
        cursor = conn.cursor()
        query = (f"INSERT INTO {config.POSTGRES_TABLES.users} "
                 f"VALUES ({chat_id}, '{login}', '{name}', {True})")
        cursor.execute(query=query)


def get_all_users() -> list:
    append_query = f" AND {COLUMNS.is_test}={True}" if config.TEST_MODE else ""
    with database_connect() as conn:
        cursor = conn.cursor()
        query = (f"SELECT {COLUMNS.chat_id} FROM {config.POSTGRES_TABLES.users} WHERE "
                 f"{COLUMNS.notifications}={True}") + append_query
        print(query)
        cursor.execute(query=query)
        data = cursor.fetchall()
        print(data)

    return [el[0] for el in data]


def delete_users(users: str | list) -> None:
    if isinstance(users, str):
        users = [users]
    with database_connect() as conn:
        cursor = conn.cursor()
        for user in users:
            query = f"DELETE FROM {config.POSTGRES_TABLES.users} WHERE {COLUMNS.login}='{user}'"
            cursor.execute(query=query)


def get_name_by_login(logins: str | list) -> None:
    if isinstance(logins, str):
        logins = [logins]
    where_query = ''
    for login in logins:
        where_query += f"{COLUMNS.login} = '{login}' OR "
    where_query = where_query[:-3]
    print(where_query)
    with database_connect() as conn:
        cursor = conn.cursor()
        query = f"SELECT {COLUMNS.name} FROM {config.POSTGRES_TABLES.users} WHERE {where_query}"
        cursor.execute(query=query)
        data = cursor.fetchall()
    return data


def switch_notifications_flag(chat_id: int, new_value: bool) -> None:
    with database_connect() as conn:
        cursor = conn.cursor()
        query = (f"UPDATE {config.POSTGRES_TABLES.users} SET {COLUMNS.notifications}={new_value} WHERE "
                 f"{COLUMNS.chat_id}={chat_id}")
        cursor.execute(query=query)


def check_user_notifications_value(chat_id: int) -> bool:
    with database_connect() as conn:
        cursor = conn.cursor()
        query = f"SELECT {COLUMNS.notifications} FROM {config.POSTGRES_TABLES.users} WHERE {COLUMNS.chat_id}={chat_id}"
        cursor.execute(query=query)
        data = cursor.fetchall()
    if data:
        # TODO: обработать ситуацию когда не нашлись данные
        return data[0][0]
