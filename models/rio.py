import psycopg2
from psycopg2 import OperationalError, IntegrityError, DatabaseError
import re

def connect_to_db():
    try:
        return psycopg2.connect(
            dbname="kursach",
            user="postgres",
            password="do6rblubatman",
            host="localhost",
        )
    except psycopg2.OperationalError as e:
        print(f"Ошибка при подключении к БД: {e}")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка при подключении к БД: {e}")
        return None

def is_valid_string(s):
    return bool(re.match(r'^[A-Za-zА-Яа-яЁё\s]+$', s))  # Разрешает буквы и пробелы

# Функция для добавления РИО
def add_rio(reviewer_fio, positions, manual_count):
    conn = connect_to_db()
    if conn is None:
        return None

    try:
        if not reviewer_fio or not positions or not manual_count: # Проверка на пустоту
            raise ValueError("Ошибка: ФИО проверяющего, должность проверяющего и количество методичек являются обязательными для заполнения")

        if not is_valid_string(reviewer_fio) or not is_valid_string(positions): # Проверка на буквы
            raise ValueError("Ошибка: ФИО проверяюзего или должность проверяющего должны содержать только буквы")

        if not isinstance(manual_count, int): # Проверка на цифры
            raise ValueError("Ошибка: Количество методичек должно являться целым числом")

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO rio (reviewer_fio, positions, manual_count)
            VALUES (%s, %s, %s) RETURNING id_worker;
        """, (reviewer_fio, positions, manual_count))
        id_worker = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return id_worker
    except IntegrityError as e:
        print(f"Ошибка целостности данных: {e}")
        conn.rollback()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при добавлении РИО: {e}")
    finally:
        conn.close()


# Функция для редактирования РИО
def update_rio_field(id_worker, field_name, new_value):
    conn = connect_to_db()
    if conn is None:
        return

    allowed_fields = ["reviewer_fio", "positions", "manual_count"]

    if field_name not in allowed_fields:
        print("Ошибка: Недопустимое поле для обновления")
        return

    try:
        cursor = conn.cursor()
        query = f"UPDATE rio SET {field_name} = %s WHERE id_worker = %s;"
        cursor.execute(query, (new_value, id_worker))
        conn.commit()
        cursor.close()
        print("РИО успешно обновлен")
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при редактировании РИО: {e}")
    finally:
        conn.close()


# Функция для удаления РИО
def delete_rio(id_worker):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM rio WHERE id_worker = %s;
        """, (id_worker,))
        conn.commit()
        cursor.close()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при удалении РИО: {e}")
    finally:
        conn.close()