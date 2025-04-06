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

# Функция отправки сообщения
def send_message(id_sender, id_receiver, id_manual, message_text, status):
    conn = connect_to_db()
    if conn is None:
        return None

    try:
        if not id_sender or not id_receiver or not id_manual or not message_text or not status: # Проверка на пустоту
            raise ValueError("Ошибка: ID отправителя, ID получателя, ID методички, текст сообщения и статус яввляются обязательными для заполнения")

        if not isinstance(id_sender, int) or not isinstance(id_receiver, int) or not isinstance(id_manual, int): # Проверка на цифры
            raise ValueError("Ошибка: ID отправителя, ID получателя или ID методички должны являться целыми числами")

        if not is_valid_string(message_text) or not is_valid_string(status): # Проверка на буквы
            raise ValueError("Ошибка: Текст сообщения или статус должны содержать только буквы")

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO messages (id_sender, id_receiver, id_manual, message_text, status)
            VALUES (%s, %s, %s, %s, %s) RETURNING id_message;
        """, (id_sender, id_receiver, id_manual, message_text, status))
        id_message = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return id_message
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
    finally:
        conn.close()

# Функция для обноваления статуса методички
def update_manual_status(id_manual, new_status):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE manual
            SET status = %s
            WHERE id_manual = %s;
        """, (new_status, id_manual))
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Ошибка при обновлении статуса методички: {e}")
    finally:
        conn.close()
