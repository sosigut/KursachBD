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

# Функция для добавления преподавателя
def add_teacher(teacher_fio, manual_count, academic_degree, id_department):
    conn = connect_to_db()
    if conn is None:
        return None

    try:
        if not teacher_fio or not manual_count or not academic_degree or not id_department: # Проверка на пустоту
            raise ValueError("Ошибка: ФИО преподавателя, количество методичек, ученая степень и ID кафедры являются обязательными для заполнения")

        if not is_valid_string(teacher_fio) or not is_valid_string(academic_degree): # Проверка на буквы
            raise ValueError("Ошибка: ФИО преподавателя или ученая степень должны содержать только буквы")

        if not isinstance(manual_count, int) or not isinstance(id_department, int): # Проверка на цифры
            raise ValueError("Ошибка: Количество методичек или ID кафедры должны являться целыми цислами")

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO teacher (teacher_fio, manual_count, academic_degree, id_department)
            VALUES (%s, %s, %s, %s) RETURNING id_teacher;
        """, (teacher_fio, manual_count, academic_degree, id_department))
        id_teacher = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return id_teacher
    except IntegrityError as e:
        print(f"Ошибка целостности данных: {e}")
        conn.rollback()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при добавлении преподавателя: {e}")
    finally:
        conn.close()


# Функция для редактирования преподавателя
def update_teacher(id_teacher, teacher_fio, manual_count, academic_degree, id_department):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE teacher
            SET teacher_fio = %s, manual_count = %s, academic_degree = %s, id_department = %s
            WHERE id_teacher = %s;
        """, (teacher_fio, manual_count, academic_degree, id_department, id_teacher))
        conn.commit()
        cursor.close()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при редактировании преподавателя: {e}")
    finally:
        conn.close()


# Функция для удаления преподавателя
def delete_teacher(id_teacher):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM teacher WHERE id_teacher = %s;
        """, (id_teacher,))
        conn.commit()
        cursor.close()
    except DatabaseError as e:
        print(f"Ошибка выполнения запроса: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Неизвестная ошибка при удалении преподавателя: {e}")
    finally:
        conn.close()