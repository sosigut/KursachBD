import tkinter as tk
from tkinter import messagebox
from models.teacher import add_teacher, delete_teacher, update_teacher_field
from models.reviewer import add_reviewer, update_reviewer_field, delete_reviewer
from models.rio import add_rio, update_rio_field, delete_rio
from models.department import add_department, update_department_field, delete_department  # Допустим, функция для добавления кафедры
from models.faculty import add_faculty, update_faculty_field, delete_faculty  # Функция для добавления факультета
from models.manual import add_manual, check_manual, update_manual_field, delete_manual  # Функция для добавления методички

# Основной интерфейс
def open_main_interface():
    root = tk.Tk()
    root.title("Приложение для работы с методичками")

    # Кнопки выбора действия
    btn_add_faculty = tk.Button(root, text="Добавить факультет", command=open_add_faculty)
    btn_add_faculty.grid(row=0, column=0, padx=10, pady=10)

    btn_edit_faculty = tk.Button(root, text="Редактировать факультет", command=open_edit_faculty)
    btn_edit_faculty.grid(row=1, column=0, padx=10, pady=10)

    btn_delete_faculty = tk.Button(root, text="Удалить факультет", command=open_delete_faculty)
    btn_delete_faculty.grid(row=2, column=0, padx=10, pady=10)

    btn_add_department = tk.Button(root, text="Добавить кафедру", command=open_add_department)
    btn_add_department.grid(row=0, column=1, padx=10, pady=10)

    btn_edit_department = tk.Button(root, text="Редактировать кафедру", command=open_edit_department)
    btn_edit_department.grid(row=1, column=1, padx=10, pady=10)

    btn_delete_department = tk.Button(root, text="Удалить кафедру", command=open_delete_department)
    btn_delete_department.grid(row=2, column=1, padx=10, pady=10)

    btn_add_manual = tk.Button(root, text="Добавить методичку", command=open_add_manual)
    btn_add_manual.grid(row=0, column=2, padx=10, pady=10)

    btn_edit_manual = tk.Button(root, text="Редактировать методичку", command=open_edit_manual)
    btn_edit_manual.grid(row=2, column=2, padx=10, pady=10)

    btn_delete_manual = tk.Button(root, text="Удалить методичку", command=open_delete_manual)
    btn_delete_manual.grid(row=1, column=2, padx=10, pady=10)

    btn_add_teacher = tk.Button(root, text="Добавить преподавателя", command=open_add_teacher)
    btn_add_teacher.grid(row=0, column=3, padx=10, pady=10)

    btn_edit_teacher = tk.Button(root, text="Редактировать преподавателя", command=open_edit_teacher)
    btn_edit_teacher.grid(row=1, column=3, padx=10, pady=10)

    btn_delete_teacher = tk.Button(root, text="Удалить преподавателя", command=open_delete_teacher)
    btn_delete_teacher.grid(row=2, column=3, padx=10, pady=10)

    btn_add_reviewer = tk.Button(root, text="Добавить проверяющего", command=open_add_reviewer)
    btn_add_reviewer.grid(row=0, column=4, padx=10, pady=10)

    btn_edit_reviewer = tk.Button(root, text="Редактировать проверяющего", command=open_edit_reviewer)
    btn_edit_reviewer.grid(row=1, column=4, padx=10, pady=10)

    btn_delete_reviewer = tk.Button(root, text="Удалить проверяющего", command=open_delete_reviewer)
    btn_delete_reviewer.grid(row=2, column=4, padx=10, pady=10)

    btn_add_rio = tk.Button(root, text="Добавить РИО", command=open_add_rio)
    btn_add_rio.grid(row=0, column=5, padx=10, pady=10)

    btn_edit_rio = tk.Button(root, text="Редактировать РИО", command=open_edit_rio)
    btn_edit_rio.grid(row=1, column=5, padx=10, pady=10)

    btn_delete_rio = tk.Button(root, text="Удалить РИО", command=open_delete_rio)
    btn_delete_rio.grid(row=2, column=5, padx=10, pady=10)

    btn_check_manual = tk.Button(root, text="Проверить методичку", command=open_check_manual)
    btn_check_manual.grid(row=0, column=6, padx=10, pady=10)

    root.mainloop()

# Окно для добавления факультета
def open_add_faculty():
    form = tk.Toplevel()
    form.title("Добавить факультет")

    tk.Label(form, text="Название факультета").pack()
    entry_name = tk.Entry(form)
    entry_name.pack()

    tk.Label(form, text="Код Факультета").pack()
    entry_faculty_code = tk.Entry(form)
    entry_faculty_code.pack()

    tk.Label(form, text="ФИО декана").pack()
    entry_dean = tk.Entry(form)
    entry_dean.pack()

    tk.Label(form, text="Количество методичек").pack()
    entry_manuals = tk.Entry(form)
    entry_manuals.pack()

    def submit_faculty():
        name = entry_name.get()
        dean = entry_dean.get()
        try:
            manuals = int(entry_manuals.get())
            faculty_code = int(entry_faculty_code.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Количество методичек или Код Факультета должно быть числом")
            return

        try:
            faculty_id = add_faculty(name, faculty_code, dean, manuals)
            messagebox.showinfo("Успех", f"Факультет добавлен с ID: {faculty_id}")
            form.destroy()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось добавить факультет: {e}")

    tk.Button(form, text="Добавить", command=submit_faculty).pack(pady=10)

def open_edit_faculty():
    window = tk.Toplevel()
    window.title("Редактирование факультета")

    # Метки и поля ввода
    tk.Label(window, text="ID факультета:").grid(row=0, column=0, padx=5, pady=5)
    entry_faculty_id = tk.Entry(window)
    entry_faculty_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Поле для редактирования:").grid(row=1, column=0, padx=5, pady=5)
    entry_field = tk.Entry(window)
    entry_field.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Новое значение:").grid(row=2, column=0, padx=5, pady=5)
    entry_new_value = tk.Entry(window)
    entry_new_value.grid(row=2, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            faculty_id = int(entry_faculty_id.get())
            field = entry_field.get()
            new_value = entry_new_value.get()
            update_faculty_field(faculty_id, field, new_value)  # Замените на вашу функцию обновления
            messagebox.showinfo("Успех", "Факультет успешно обновлен.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID факультета должен быть числом.")

    # Кнопка обновления
    tk.Button(window, text="Обновить", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

def open_delete_faculty():
    window = tk.Toplevel()
    window.title("Удаление факультета")

    # Метки и поля ввода
    tk.Label(window, text="ID факультета для удаления:").grid(row=0, column=0, padx=5, pady=5)
    entry_faculty_id = tk.Entry(window)
    entry_faculty_id.grid(row=0, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            faculty_id = int(entry_faculty_id.get())
            delete_faculty(faculty_id)  # Замените на вашу функцию удаления
            messagebox.showinfo("Успех", "Факультет успешно удален.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID факультета должен быть числом.")

    # Кнопка удаления
    tk.Button(window, text="Удалить", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

# Окно для редактирования кафедры
def open_edit_department():
    window = tk.Toplevel()
    window.title("Редактировать кафедру")

    # Метки и поля ввода
    tk.Label(window, text="ID кафедры:").grid(row=0, column=0, padx=5, pady=5)
    entry_department_id = tk.Entry(window)
    entry_department_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Поле для редактирования:").grid(row=1, column=0, padx=5, pady=5)
    entry_field = tk.Entry(window)
    entry_field.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Новое значение:").grid(row=2, column=0, padx=5, pady=5)
    entry_new_value = tk.Entry(window)
    entry_new_value.grid(row=2, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            department_id = int(entry_department_id.get())
            field = entry_field.get()
            new_value = entry_new_value.get()
            update_department_field(department_id, field, new_value)  # Функция обновления кафедры
            messagebox.showinfo("Успех", "Кафедра успешно обновлена.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID кафедры должен быть числом.")

    # Кнопка обновления
    tk.Button(window, text="Обновить", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

def open_add_department():
    window = tk.Toplevel()
    window.title("Добавить кафедру")

    # Метки и поля ввода
    tk.Label(window, text="Название кафедры:").grid(row=0, column=0, padx=5, pady=5)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Код Кафедры:").grid(row=1, column=0, padx=5, pady=5)
    entry_department_code = tk.Entry(window)
    entry_department_code.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Количество методичек:").grid(row=2, column=0, padx=5, pady=5)
    entry_manual_count = tk.Entry(window)
    entry_manual_count.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(window, text="ID факультета:").grid(row=3, column=0, padx=5, pady=5)
    entry_faculty_id = tk.Entry(window)
    entry_faculty_id.grid(row=3, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        name = entry_name.get()
        try:
            manual_count = int(entry_manual_count.get())
            faculty_id = int(entry_faculty_id.get())
            department_code = int(entry_department_code.get())

            result = add_department(name, department_code, manual_count, faculty_id)
            if result:
                messagebox.showinfo("Успех", f"Кафедра добавлена с id {result}")
                window.destroy()
            else:
                messagebox.showerror("Ошибка", "Не удалось добавить кафедру")
        except ValueError:
            messagebox.showerror("Ошибка", "Количество методичек и ID факультета должны быть целыми числами")

    # Кнопка отправки
    tk.Button(window, text="Добавить", command=submit).grid(row=5, column=0, columnspan=2, pady=10)

# Окно для редактирования кафедры
def open_edit_department():
    window = tk.Toplevel()
    window.title("Редактировать кафедру")

    # Метки и поля ввода
    tk.Label(window, text="ID кафедры:").grid(row=0, column=0, padx=5, pady=5)
    entry_department_id = tk.Entry(window)
    entry_department_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Поле для редактирования:").grid(row=1, column=0, padx=5, pady=5)
    entry_field = tk.Entry(window)
    entry_field.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Новое значение:").grid(row=2, column=0, padx=5, pady=5)
    entry_new_value = tk.Entry(window)
    entry_new_value.grid(row=2, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            department_id = int(entry_department_id.get())
            field = entry_field.get()
            new_value = entry_new_value.get()
            update_department_field(department_id, field, new_value)  # Функция обновления кафедры
            messagebox.showinfo("Успех", "Кафедра успешно обновлена.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID кафедры должен быть числом.")

    # Кнопка обновления
    tk.Button(window, text="Обновить", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

# Окно для удаления кафедры
def open_delete_department():
    window = tk.Toplevel()
    window.title("Удаление кафедры")

    # Метки и поля ввода
    tk.Label(window, text="ID кафедры для удаления:").grid(row=0, column=0, padx=5, pady=5)
    entry_department_id = tk.Entry(window)
    entry_department_id.grid(row=0, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            department_id = int(entry_department_id.get())
            delete_department(department_id)  # Функция удаления кафедры
            messagebox.showinfo("Успех", "Кафедра успешно удалена.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID кафедры должен быть числом.")

    # Кнопка удаления
    tk.Button(window, text="Удалить", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

def open_add_manual():
    window = tk.Toplevel()
    window.title("Добавить методичку")

    # Метки и поля ввода
    tk.Label(window, text="Название методички:").grid(row=0, column=0, padx=5, pady=5)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Дата выпуска (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
    entry_date = tk.Entry(window)
    entry_date.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Количество страниц:").grid(row=2, column=0, padx=5, pady=5)
    entry_pages = tk.Entry(window)
    entry_pages.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(window, text="Статус:").grid(row=3, column=0, padx=5, pady=5)
    entry_status = tk.Entry(window)
    entry_status.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(window, text="ID преподавателя:").grid(row=4, column=0, padx=5, pady=5)
    entry_teacher_id = tk.Entry(window)
    entry_teacher_id.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(window, text="ID кафедры:").grid(row=5, column=0, padx=5, pady=5)
    entry_department_id = tk.Entry(window)
    entry_department_id.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(window, text="ID факультета:").grid(row=6, column=0, padx=5, pady=5)
    entry_faculty_id = tk.Entry(window)
    entry_faculty_id.grid(row=6, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        name = entry_name.get()
        release_date = entry_date.get()
        status = entry_status.get()
        try:
            page_count = int(entry_pages.get())
            teacher_id = int(entry_teacher_id.get())
            department_id = int(entry_department_id.get())
            faculty_id = int(entry_faculty_id.get())

            result = add_manual(name, release_date, page_count, status, teacher_id, department_id, faculty_id)
            if result:
                messagebox.showinfo("Успех", f"Методичка добавлена с id {result}")
                window.destroy()
            else:
                messagebox.showerror("Ошибка", "Не удалось добавить методичку")
        except ValueError:
            messagebox.showerror("Ошибка", "Числовые поля должны быть заполнены корректно и дата должна быть в формате YYYY-MM-DD")

    # Кнопка добавления
    tk.Button(window, text="Добавить методичку", command=submit).grid(row=7, column=0, columnspan=2, pady=10)

# Окно для удаления методички
def open_delete_manual():
    window = tk.Toplevel()
    window.title("Удалить методичку")

    tk.Label(window, text="ID методички для удаления:").grid(row=0, column=0, padx=5, pady=5)
    entry_manual_id = tk.Entry(window)
    entry_manual_id.grid(row=0, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            manual_id = int(entry_manual_id.get())
            delete_manual(manual_id)  # Функция для удаления методички
            messagebox.showinfo("Успех", "Методичка успешно удалена.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID методички должен быть числом.")

    tk.Button(window, text="Удалить", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

# Окно для редактирования методички
def open_edit_manual():
    window = tk.Toplevel()
    window.title("Редактировать методичку")

    # Поля для ввода
    tk.Label(window, text="ID методички:").grid(row=0, column=0, padx=5, pady=5)
    entry_manual_id = tk.Entry(window)
    entry_manual_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Поле для редактирования:").grid(row=1, column=0, padx=5, pady=5)
    entry_field = tk.Entry(window)
    entry_field.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Новое значение:").grid(row=2, column=0, padx=5, pady=5)
    entry_new_value = tk.Entry(window)
    entry_new_value.grid(row=2, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            manual_id = int(entry_manual_id.get())
            field = entry_field.get()
            new_value = entry_new_value.get()
            update_manual_field(manual_id, field, new_value)  # Функция для обновления методички
            messagebox.showinfo("Успех", "Методичка успешно обновлена.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID методички должен быть числом.")

    tk.Button(window, text="Обновить", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

# Окно для добавления преподавателя
def open_add_teacher():
    window = tk.Toplevel()
    window.title("Добавление преподавателя")

    label_fio = tk.Label(window, text="ФИО преподавателя:")
    label_fio.grid(row=0, column=0, padx=10, pady=5)
    entry_fio = tk.Entry(window)
    entry_fio.grid(row=0, column=1, padx=10, pady=5)

    label_manual_count = tk.Label(window, text="Количество методичек:")
    label_manual_count.grid(row=1, column=0, padx=10, pady=5)
    entry_manual_count = tk.Entry(window)
    entry_manual_count.grid(row=1, column=1, padx=10, pady=5)

    label_academic_degree = tk.Label(window, text="Ученая степень:")
    label_academic_degree.grid(row=2, column=0, padx=10, pady=5)
    entry_academic_degree = tk.Entry(window)
    entry_academic_degree.grid(row=2, column=1, padx=10, pady=5)

    label_id_department = tk.Label(window, text="ID кафедры:")
    label_id_department.grid(row=3, column=0, padx=10, pady=5)
    entry_id_department = tk.Entry(window)
    entry_id_department.grid(row=3, column=1, padx=10, pady=5)

    def add_teacher_action():
        teacher_fio = entry_fio.get()
        manual_count = entry_manual_count.get()
        academic_degree = entry_academic_degree.get()
        id_department = entry_id_department.get()

        if not teacher_fio or not manual_count or not academic_degree or not id_department:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены.")
            return

        try:
            manual_count = int(manual_count)
            id_department = int(id_department)
        except ValueError:
            messagebox.showerror("Ошибка", "Количество методичек и ID кафедры должны быть числами.")
            return

        id_teacher = add_teacher(teacher_fio, manual_count, academic_degree, id_department)
        if id_teacher:
            messagebox.showinfo("Успех", f"Преподаватель добавлен с ID: {id_teacher}")
        else:
            messagebox.showerror("Ошибка", "Ошибка при добавлении преподавателя.")

    btn_add = tk.Button(window, text="Добавить", command=add_teacher_action)
    btn_add.grid(row=4, column=0, columnspan=2, pady=10)

# Окно для редактирования преподавателя
def open_edit_teacher():
    window = tk.Toplevel()
    window.title("Редактирование преподавателя")

    # Метки и поля ввода
    tk.Label(window, text="ID преподавателя:").grid(row=0, column=0, padx=5, pady=5)
    entry_teacher_id = tk.Entry(window)
    entry_teacher_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Поле для редактирования:").grid(row=1, column=0, padx=5, pady=5)
    entry_field = tk.Entry(window)
    entry_field.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Новое значение:").grid(row=2, column=0, padx=5, pady=5)
    entry_new_value = tk.Entry(window)
    entry_new_value.grid(row=2, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            teacher_id = int(entry_teacher_id.get())
            field = entry_field.get()
            new_value = entry_new_value.get()
            update_teacher_field(teacher_id, field, new_value)
            messagebox.showinfo("Успех", "Преподаватель успешно обновлен.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID преподавателя должен быть числом.")

    # Кнопка обновления
    tk.Button(window, text="Обновить", command=submit).grid(row=3, column=0, columnspan=2, pady=10)


def open_delete_teacher():
    window = tk.Toplevel()
    window.title("Удаление преподавателя")

    # Метки и поля ввода
    tk.Label(window, text="ID преподавателя для удаления:").grid(row=0, column=0, padx=5, pady=5)
    entry_teacher_id = tk.Entry(window)
    entry_teacher_id.grid(row=0, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            teacher_id = int(entry_teacher_id.get())
            delete_teacher(teacher_id)
            messagebox.showinfo("Успех", "Преподаватель успешно удален.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID преподавателя должен быть числом.")

    # Кнопка удаления
    tk.Button(window, text="Удалить", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

def open_add_reviewer():
    window = tk.Toplevel()
    window.title("Добавить проверяющего")

    # Метки и поля ввода
    tk.Label(window, text="ФИО проверяющего:").grid(row=0, column=0, padx=5, pady=5)
    entry_fio = tk.Entry(window)
    entry_fio.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="ID методички:").grid(row=1, column=0, padx=5, pady=5)
    entry_manual_id = tk.Entry(window)
    entry_manual_id.grid(row=1, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        fio = entry_fio.get()
        try:
            manual_id = int(entry_manual_id.get())
            result = add_reviewer(fio, manual_id)
            if result:
                messagebox.showinfo("Успех", f"Проверяющий добавлен с id {result}")
                window.destroy()
            else:
                messagebox.showerror("Ошибка", "Не удалось добавить проверяющего")
        except ValueError:
            messagebox.showerror("Ошибка", "ID методички должно быть целым числом")

    # Кнопка добавления
    tk.Button(window, text="Добавить проверяющего", command=submit).grid(row=2, column=0, columnspan=2, pady=10)

# Окно для редактирования проверяющего
def open_edit_reviewer():
    window = tk.Toplevel()
    window.title("Редактирование проверяющего")

    # Метки и поля ввода
    tk.Label(window, text="ID проверяющего:").grid(row=0, column=0, padx=5, pady=5)
    entry_reviewer_id = tk.Entry(window)
    entry_reviewer_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Поле для редактирования:").grid(row=1, column=0, padx=5, pady=5)
    entry_field = tk.Entry(window)
    entry_field.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Новое значение:").grid(row=2, column=0, padx=5, pady=5)
    entry_new_value = tk.Entry(window)
    entry_new_value.grid(row=2, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            reviewer_id = int(entry_reviewer_id.get())
            field = entry_field.get()
            new_value = entry_new_value.get()
            update_reviewer_field(reviewer_id, field, new_value)
            messagebox.showinfo("Успех", "Проверяющий успешно обновлен.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID проверяющего должен быть числом.")

    # Кнопка обновления
    tk.Button(window, text="Обновить", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

# Окно для удаления проверяющего
def open_delete_reviewer():
    window = tk.Toplevel()
    window.title("Удаление проверяющего")

    # Метки и поля ввода
    tk.Label(window, text="ID проверяющего для удаления:").grid(row=0, column=0, padx=5, pady=5)
    entry_reviewer_id = tk.Entry(window)
    entry_reviewer_id.grid(row=0, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            reviewer_id = int(entry_reviewer_id.get())
            delete_reviewer(reviewer_id)
            messagebox.showinfo("Успех", "Проверяющий успешно удален.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID проверяющего должен быть числом.")

    # Кнопка удаления
    tk.Button(window, text="Удалить", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

def open_add_rio():
    window = tk.Toplevel()
    window.title("Добавить РИО")

    # Метки и поля ввода
    tk.Label(window, text="ФИО работника РИО:").grid(row=0, column=0, padx=5, pady=5)
    entry_fio = tk.Entry(window)
    entry_fio.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Должность:").grid(row=1, column=0, padx=5, pady=5)
    entry_position = tk.Entry(window)
    entry_position.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Количество методичек:").grid(row=2, column=0, padx=5, pady=5)
    entry_manual_count = tk.Entry(window)
    entry_manual_count.grid(row=2, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        fio = entry_fio.get()
        position = entry_position.get()
        try:
            manual_count = int(entry_manual_count.get())
            result = add_rio(fio, position, manual_count)
            if result:
                messagebox.showinfo("Успех", f"РИО добавлен с id {result}")
                window.destroy()
            else:
                messagebox.showerror("Ошибка", "Не удалось добавить работника РИО")
        except ValueError:
            messagebox.showerror("Ошибка", "Количество методичек должно быть целым числом")

    # Кнопка добавления
    tk.Button(window, text="Добавить РИО", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

def open_delete_rio():
    window = tk.Toplevel()
    window.title("Удаление РИО")

    # Метки и поля ввода
    tk.Label(window, text="ID РИО для удаления:").grid(row=0, column=0, padx=5, pady=5)
    entry_rio_id = tk.Entry(window)
    entry_rio_id.grid(row=0, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            rio_id = int(entry_rio_id.get())
            delete_rio(rio_id)  # Предполагается, что у вас есть такая функция
            messagebox.showinfo("Успех", "РИО успешно удален.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID РИО должен быть числом.")

    # Кнопка удаления
    tk.Button(window, text="Удалить", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

def open_edit_rio():
    window = tk.Toplevel()
    window.title("Редактирование РИО")

    # Метки и поля ввода
    tk.Label(window, text="ID РИО:").grid(row=0, column=0, padx=5, pady=5)
    entry_rio_id = tk.Entry(window)
    entry_rio_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(window, text="Поле для редактирования:").grid(row=1, column=0, padx=5, pady=5)
    entry_field = tk.Entry(window)
    entry_field.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Новое значение:").grid(row=2, column=0, padx=5, pady=5)
    entry_new_value = tk.Entry(window)
    entry_new_value.grid(row=2, column=1, padx=5, pady=5)

    # Обработчик кнопки
    def submit():
        try:
            rio_id = int(entry_rio_id.get())
            field = entry_field.get()
            new_value = entry_new_value.get()
            update_rio_field(rio_id, field, new_value)  # Предполагается, что у вас есть такая функция
            messagebox.showinfo("Успех", "РИО успешно обновлен.")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "ID РИО должен быть числом.")

    # Кнопка обновления
    tk.Button(window, text="Обновить", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

# Окно для проверки методички
def open_check_manual():
    window = tk.Toplevel()
    window.title("Проверка методички")

    # Поле для ввода ID методички
    label_manual_id = tk.Label(window, text="ID методички для проверки:")
    label_manual_id.grid(row=0, column=0, padx=10, pady=5)
    entry_manual_id = tk.Entry(window)
    entry_manual_id.grid(row=0, column=1, padx=10, pady=5)

    # Поле для ввода комментария (если методичка не прошла проверку)
    label_comment = tk.Label(window, text="Комментарий (если не прошла проверку):")
    label_comment.grid(row=1, column=0, padx=10, pady=5)
    entry_comment = tk.Entry(window)
    entry_comment.grid(row=1, column=1, padx=10, pady=5)

    # Радиокнопки для статуса методички (прошла или не прошла проверку)
    var_status = tk.StringVar(value="Прошла проверку")
    radio_passed = tk.Radiobutton(window, text="Прошла проверку", variable=var_status, value="Прошла проверку")
    radio_passed.grid(row=2, column=0, padx=10, pady=5)
    radio_rework = tk.Radiobutton(window, text="На доработку", variable=var_status, value="На доработку")
    radio_rework.grid(row=2, column=1, padx=10, pady=5)

    # Функция для обработки кнопки проверки методички
    def check_manual_action():
        manual_id = entry_manual_id.get()
        if not manual_id:
            messagebox.showerror("Ошибка", "ID методички не может быть пустым.")
            return
        try:
            manual_id = int(manual_id)
        except ValueError:
            messagebox.showerror("Ошибка", "ID методички должен быть числом.")
            return

        comment = entry_comment.get()  # Получаем комментарий
        approved = var_status.get() == "Прошла проверку"  # Определяем, прошла ли методичка проверку

        # Вызываем функцию check_manual для обновления статуса
        try:
            result = check_manual(manual_id, approved, comment)
            if result:
                messagebox.showinfo("Успех", f"Методичка с ID {manual_id} успешно обновлена.")
            else:
                messagebox.showerror("Ошибка", "Ошибка при проверке методички.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

    # Кнопка для проверки методички
    btn_check = tk.Button(window, text="Проверить", command=check_manual_action)
    btn_check.grid(row=3, column=0, columnspan=2, pady=10)

    window.mainloop()

# Запуск основного интерфейса
open_main_interface()
