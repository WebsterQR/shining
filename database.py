import psycopg2
import config


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
        query = f" SELECT * FROM {config.POSTGRES_TABLES.users} WHERE chat_id={chat_id}"
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
        query = f"SELECT chat_id FROM {config.POSTGRES_TABLES.users}"
        cursor.execute(query=query)
        data = cursor.fetchall()

    return [el[0] for el in data]