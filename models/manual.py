import psycopg2
from psycopg2 import OperationalError, IntegrityError, DatabaseError
from datetime import datetime
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

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')  # Проверка на формат YYYY-MM-DD
        return True
    except ValueError:
        return False

# Функция для добавления методички
def add_manual(manual_name, release_date, page_count, status, id_teacher, id_department, id_faculty):
    conn = connect_to_db()
    if conn is None:
        return None

    try:
        if not manual_name or not release_date or not page_count or not status or not id_teacher or not id_department or not id_faculty: # Проверка на пустоту
            raise ValueError("Ошибка: Название методички, дата выпуска методички, ФИО автора, количество страниц, статус ID преподавателя, ID кафедры и ID факультета являются обязательными для заполнения")

        if not is_valid_string(manual_name) or not is_valid_string(status): # Проверка на буквы
            raise ValueError("Ошибка: Названия методички или статус должны содержать только буквы")

        if not is_valid_date(release_date): # Проверка на цифры
            raise ValueError("Ошибка: Дата должна иметь вид YYYY-mm-dd")

        if not isinstance(page_count, int) or not isinstance(id_teacher, int) or not isinstance(id_department, int) or not isinstance(id_faculty, int):
            raise ValueError("Ошибка: Дата выпуска методички, количество страниц, ID преподавателя, ID кафедры или ID факультета должны являться целыми числами")

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO manual (manual_name, release_date, page_count, status, id_teacher, id_department, id_faculty)
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_manual;
        """, (manual_name, release_date, page_count, status, id_teacher, id_department, id_faculty))
        id_manual = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return id_manual
    except IntegrityError as e:
        print(f"Ошибка целостности данных: {e}")
        conn.rollback()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при добавлении методички: {e}")
    finally:
        conn.close()


# Функция для редактирования методички
def update_manual_field(id_manual, field_name, new_value):
    conn = connect_to_db()
    if conn is None:
        return

    allowed_fields = ["manual_name", "release_date", "page_count", "status", "id_teacher", "id_department", "id_faculty"]

    if field_name not in allowed_fields:
        print("Ошибка: Недопустимое поле для обновления")
        return

    try:
        cursor = conn.cursor()
        query = f"UPDATE manual SET {field_name} = %s WHERE id_manual = %s;"
        cursor.execute(query, (new_value, id_manual))
        conn.commit()
        cursor.close()
        print("Методичка успешно обновлена")
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при редактировании методички: {e}")
    finally:
        conn.close()

def check_manual(id_manual, approved, comment=None):
    conn = connect_to_db()
    if conn is None:
        print("Ошибка подключения к базе данных.")
        return False  # Возвращаем False в случае ошибки соединения

    try:
        cursor = conn.cursor()

        # Обновляем статус методички
        status = 'издано' if approved else 'на доработку'
        cursor.execute("""
            UPDATE manual
            SET status = %s
            WHERE id_manual = %s;
        """, (status, id_manual))

        # Если не одобрено — добавляем комментарий преподавателю
        if not approved and comment:
            cursor.execute("""
                UPDATE manual
                SET comment = %s
                WHERE id_manual = %s;
            """, (comment, id_manual))

        conn.commit()
        cursor.close()

        # Логируем успешное выполнение
        print(f"Методичка с ID {id_manual} {'издана' if approved else 'отправлена на доработку'}.")

        return True  # Возвращаем True, если все прошло успешно

    except DatabaseError as e:
        print(f"Ошибка при обновлении методички: {e}")
        conn.rollback()
        return False  # Возвращаем False при ошибке в базе данных
    except Exception as e:
        print(f"Неизвестная ошибка при проверке методички: {e}")
        conn.rollback()
        return False  # Возвращаем False при неизвестной ошибке
    finally:
        conn.close()

# Функция для удаления методички
def delete_manual(id_manual):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM manual WHERE id_manual = %s;
        """, (id_manual,))
        conn.commit()
        cursor.close()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при удалении методички: {e}")
    finally:
        conn.close()