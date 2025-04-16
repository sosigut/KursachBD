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

# Функция для добавления факультета
def add_faculty(faculty_name, faculty_code, dean_fio, manual_count):
    conn = connect_to_db()
    if conn is None:
        return None

    try:
        if not faculty_name or not dean_fio or not manual_count: # Проверка на пустоту
            raise ValueError("Ошибка: Название факультета, ФИО декана и количество методичек являются обязательными для заполнения")

        if not is_valid_string(faculty_name) or not is_valid_string(dean_fio): # Проверка на буквы
            raise ValueError("Ошибка: ФИО или название факультета должны содержать только буквы")

        if not isinstance(manual_count, int) or not isinstance(faculty_code, int): # Проверка на цифры
            raise ValueError('Ошибка: Количество методичек или Код Факультета должно являться целым цислом')

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO faculty (faculty_name, faculty_code, dean_fio, manual_count)
            VALUES (%s, %s, %s, %s) RETURNING id_faculty;
        """, (faculty_name, faculty_code, dean_fio, manual_count))
        id_faculty = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return id_faculty
    except IntegrityError as e:
        print(f"Ошибка целостности данных: {e}")
        conn.rollback()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при добавлении факультета: {e}")
    finally:
        conn.close()

# Функция для редактирования факультета
def update_faculty_field(id_faculty, field_name, new_value):
    conn = connect_to_db()
    if conn is None:
        return

    allowed_fields = ["faculty_name", "dean_fio", "manual_count"]

    if field_name not in allowed_fields:
        print("Ошибка: Недопустимое поле для обновления")
        return

    try:
        cursor = conn.cursor()
        query = f"UPDATE faculty SET {field_name} = %s WHERE id_faculty = %s;"
        cursor.execute(query, (new_value, id_faculty))
        conn.commit()
        cursor.close()
        print("Факультет успешно обновлён")
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при редактировании факультета: {e}")
    finally:
        conn.close()


# Функция для удаления факультета
def delete_faculty(id_faculty):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM faculty WHERE id_faculty = %s
        """, (id_faculty,))
        conn.commit()
        cursor.close()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при удалении факультета: {e}")
    finally:
        conn.close()