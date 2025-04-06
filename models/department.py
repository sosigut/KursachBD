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

# Функция для добавления кафедры
def add_department(department_name, manual_count, id_faculty):
    conn = connect_to_db()
    if conn is None:
        return None

    try:
        if not department_name or not manual_count or not id_faculty: # Проверка на пустоту
            raise ValueError("Ошибка: Название кафедры, количество методичек и ID факультета являются обязательными для заполнения")

        if not is_valid_string(department_name): # Проверка на буквы
            raise ValueError("Ошибка: Название кафедры должны содержать только буквы")

        if not isinstance(manual_count, int) or not isinstance(id_faculty, int): # Проверка на цифры
            raise ValueError("Ошибка: Количество методичеку или ID факультета должны являться целыми числами")

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO department (department_name, manual_count, id_faculty)
            VALUES (%s, %s, %s) RETURNING id_department;
        """, (department_name, manual_count, id_faculty))
        id_department = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return id_department
    except IntegrityError as e:
        print(f"Ошибка целостности данных: {e}")
        conn.rollback()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при добавлении кафедры: {e}")
    finally:
        conn.close()


# Функция для редактирования кафедры
def update_department(id_department, department_name, manual_count, id_faculty):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE department
            SET department_name = %s, manual_count = %s, id_faculty = %s
            WHERE id_department = %s;
        """, (department_name, manual_count, id_faculty, id_department))
        conn.commit()
        cursor.close()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при редактировании кафедры: {e}")
    finally:
        conn.close()


# Функция для удаления кафедры
def delete_department(id_department):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM department WHERE id_department = %s;
        """, (id_department,))
        conn.commit()
        cursor.close()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при удалении кафедры: {e}")
    finally:
        conn.close()