import psycopg2
import config


class COLUMNS:
    chat_id = "chat_id"
    name = "user_name"
    login = "login"

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
                 f"VALUES ({chat_id}, '{login}', '{name}')")
        cursor.execute(query=query)

def get_all_users() -> list:
    with database_connect() as conn:
        cursor = conn.cursor()
        query = f"SELECT {COLUMNS.chat_id} FROM {config.POSTGRES_TABLES.users}"
        cursor.execute(query=query)
        data = cursor.fetchall()

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
        users = [logins]
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