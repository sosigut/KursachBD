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

# Функция для добавления проверяющего
def add_reviewer(reviewer_fio, id_manual):
    conn = connect_to_db()
    if conn is None:
        return None

    try:
        if not reviewer_fio or not id_manual: # Проверка на пустоту
            raise ValueError("Ошибка: ФИО проверяющего и ID методички являются обязательными для заполнения")

        if not is_valid_string(reviewer_fio): # Проверка на буквы
            raise ValueError("Ошибка: ФИО проверяющего должно содержать только буквы")

        if not isinstance(id_manual, int): # Проверка на цифры
            raise ValueError("Ошибка: ID методички должно являться целым числом")

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reviewer (reviewer_fio, id_manual)
            VALUES (%s, %s) RETURNING id_reviewer;
        """, (reviewer_fio, id_manual))
        id_reviewer = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return id_reviewer
    except IntegrityError as e:
        print(f"Ошибка целостности данных: {e}")
        conn.rollback()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при добавлении проверяющего: {e}")
    finally:
        conn.close()


# Функция для редактирования проверяющего
def update_reviewer_field(id_reviewer, field_name, new_value):
    conn = connect_to_db()
    if conn is None:
        return

    allowed_fields = ["reviewer_fio", "id_manual"]

    if field_name not in allowed_fields:
        print("Ошибка: Недопустимое поле для обновления")
        return

    try:
        cursor = conn.cursor()
        query = f"UPDATE reviewer SET {field_name} = %s WHERE id_reviewer = %s;"
        cursor.execute(query, (new_value, id_reviewer))
        conn.commit()
        cursor.close()
        print("Проверяющий успешно обновлен")
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при редактировании проверяющего: {e}")
    finally:
        conn.close()


# Функция для удаления проверяющего
def delete_reviewer(id_reviewer):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM reviewer WHERE id_reviewer = %s;
        """, (id_reviewer,))
        conn.commit()
        cursor.close()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при удалении проверяющего: {e}")
    finally:
        conn.close()