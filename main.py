from models.faculty import add_faculty, update_faculty, delete_faculty
from models.department import add_department, update_department, delete_department
from models.teacher import add_teacher, update_teacher, delete_teacher
from models.manual import add_manual, update_manual, delete_manual
from models.proverka import send_message, update_manual_status
from models.reviewer import add_reviewer, update_reviewer
from models.rio import add_rio, update_rio, delete_rio
from models.rio import add_rio, update_rio, delete_rio

def main():
    id_faculty = add_faculty('ФФиПИ', 'Таныгин', 10)
    print(f'Добавлен факультет с id = {id_faculty}')

    id_department = add_department('ИБ', 2, id_faculty)
    print(f'Добавлена кафедра с id = {id_department}')

    id_teacher = add_teacher('Станислав Киреев', 2, 'Худший в мире', id_department)
    print(f'Добавлен преподаватель с id = {id_teacher}')

    id_manual = add_manual('Методичка по языку', '2025-03-06', 10, "На проверке", id_teacher, id_department, id_faculty)
    print(f'Добавлена методичка с id = {id_manual}')

    id_reviewer = add_reviewer('Глазов Михаил Юрьевич', id_manual)
    print(f'Добавлен проверяющий с id = {id_reviewer}')

    id_rio = add_rio("Глазов Михаил Юрьевич", 'Проверяющий', 2)
    print(f'Добавлен РИО с id = {id_rio}')

    id_message = send_message(id_teacher, id_reviewer, id_manual, 'Проверьте методичку', 'Отправлено')
    print(f"Сообщение отправлено с ID: {id_message}")

    update_manual_status(id_manual, "Одобрено")
    print(f"Статус методички с ID {id_manual} обновлен на 'Одобрено'")

if __name__ == '__main__':
    main()