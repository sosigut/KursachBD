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
def add_department(department_name, department_code, manual_count, id_faculty):
    conn = connect_to_db()
    if conn is None:
        return None

    try:
        if not department_name or not manual_count or not id_faculty or not department_code: # Проверка на пустоту
            raise ValueError("Ошибка: Название кафедры, количество методичек, ID факультета, Код Кафедры являются обязательными для заполнения")

        if not is_valid_string(department_name): # Проверка на буквы
            raise ValueError("Ошибка: Название кафедры должны содержать только буквы")

        if not isinstance(manual_count, int) or not isinstance(id_faculty, int) or not isinstance(department_code, int): # Проверка на цифры
            raise ValueError("Ошибка: Количество методичеку, ID факультета или Код Кафедры должны являться целыми числами")

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO department (department_name, department_code, manual_count, id_faculty)
            VALUES (%s, %s, %s, %s) RETURNING id_department;
        """, (department_name, department_code, manual_count, id_faculty))
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
def update_department_field(id_department, field_name, new_value):
    conn = connect_to_db()
    if conn is None:
        return

    allowed_fields = ["department_name", "manual_count", "id_faculty"]

    if field_name not in allowed_fields:
        print("Ошибка: Недопустимое поле для обновления")
        return

    try:
        cursor = conn.cursor()
        query = f"UPDATE department SET {field_name} = %s WHERE id_department = %s;"
        cursor.execute(query, (new_value, id_department))
        conn.commit()
        cursor.close()
        print("Кафедра успешно обновлена")
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