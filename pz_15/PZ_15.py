#Приложение КОНТРОЛЬ ИСПОЛНЕНИЯ ПОРУЧЕНИЙ для некоторой
#организации. БД должна содержать таблицу Поручения со следующей структурой записи:
#Порядковый номер поручения, Название поручения, Дата выдачи поручения, Срок
#исполнения, Исполнитель.


import sqlite3
from datetime import datetime
from typing import List, Dict, Optional


class TaskManager:
    def __init__(self, db_name: str = 'tasks.db'):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        #Инициализация базы данных и создание таблицы, если её нет
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    issue_date TEXT NOT NULL,
                    deadline TEXT NOT NULL,
                    assignee TEXT NOT NULL,
                    status TEXT DEFAULT 'active'
                )
            ''')
            conn.commit()

    def add_task(self, title: str, deadline: str, assignee: str) -> int:
        #Добавление нового поручения
        issue_date = datetime.now().strftime('%Y-%m-%d')
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tasks (title, issue_date, deadline, assignee)
                VALUES (?, ?, ?, ?)
            ''', (title, issue_date, deadline, assignee))
            conn.commit()
            return cursor.lastrowid

    def complete_task(self, task_id: int) -> bool:
        #Пометить поручение как выполненное
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE tasks SET status = 'completed' WHERE id = ?
            ''', (task_id,))
            conn.commit()
            return cursor.rowcount > 0

    def get_all_tasks(self, filter_status: Optional[str] = None) -> List[Dict]:
        #Получить список всех поручений с возможностью фильтрации по статусу
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            if filter_status:
                cursor.execute('''
                    SELECT * FROM tasks WHERE status = ? ORDER BY deadline
                ''', (filter_status,))
            else:
                cursor.execute('''
                    SELECT * FROM tasks ORDER BY deadline
                ''')

            return [dict(row) for row in cursor.fetchall()]

    def get_task(self, task_id: int) -> Optional[Dict]:
        #Получить информацию о конкретном поручении
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def delete_task(self, task_id: int) -> bool:
        #Удалить поручение
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            conn.commit()
            return cursor.rowcount > 0

    def get_overdue_tasks(self) -> List[Dict]:
        #Получить список просроченных поручений
        today = datetime.now().strftime('%Y-%m-%d')
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM tasks 
                WHERE deadline < ? AND status = 'active'
                ORDER BY deadline
            ''', (today,))
            return [dict(row) for row in cursor.fetchall()]


def display_menu():
    #Отображение меню приложения
    print("\nКонтроль исполнения поручений")
    print("1. Добавить новое поручение")
    print("2. Просмотреть все активные поручения")
    print("3. Просмотреть выполненные поручения")
    print("4. Просмотреть просроченные поручения")
    print("5. Отметить поручение как выполненное")
    print("6. Удалить поручение")
    print("7. Выход")


def display_tasks(tasks: List[Dict]):
    #Отображение списка поручений
    if not tasks:
        print("Нет поручений для отображения.")
        return

    print("\nСписок поручений:")
    print("-" * 80)
    print(
        f"{'ID':<5} | {'Название':<30} | {'Дата выдачи':<12} | {'Срок исполнения':<15} | {'Исполнитель':<20} | {'Статус':<10}")
    print("-" * 80)

    for task in tasks:
        print(f"{task['id']:<5} | {task['title'][:28]:<30} | {task['issue_date']:<12} | "
              f"{task['deadline']:<15} | {task['assignee'][:18]:<20} | {task['status']:<10}")
    print("-" * 80)


def main():
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            # Добавление нового поручения
            title = input("Введите название поручения: ")
            deadline = input("Введите срок исполнения (ГГГГ-ММ-ДД): ")
            assignee = input("Введите имя исполнителя: ")

            try:
                task_id = task_manager.add_task(title, deadline, assignee)
                print(f"Поручение успешно добавлено с ID {task_id}")
            except Exception as e:
                print(f"Ошибка при добавлении поручения: {e}")

        elif choice == '2':
            # Просмотр активных поручений
            tasks = task_manager.get_all_tasks(filter_status='active')
            display_tasks(tasks)

        elif choice == '3':
            # Просмотр выполненных поручений
            tasks = task_manager.get_all_tasks(filter_status='completed')
            display_tasks(tasks)

        elif choice == '4':
            # Просмотр просроченных поручений
            tasks = task_manager.get_overdue_tasks()
            display_tasks(tasks)

        elif choice == '5':
            # Отметка поручения как выполненного
            task_id = input("Введите ID поручения для отметки как выполненного: ")
            try:
                if task_manager.complete_task(int(task_id)):
                    print("Поручение успешно отмечено как выполненное")
                else:
                    print("Поручение с таким ID не найдено")
            except ValueError:
                print("Неверный формат ID")

        elif choice == '6':
            # Удаление поручения
            task_id = input("Введите ID поручения для удаления: ")
            try:
                if task_manager.delete_task(int(task_id)):
                    print("Поручение успешно удалено")
                else:
                    print("Поручение с таким ID не найдено")
            except ValueError:
                print("Неверный формат ID")

        elif choice == '7':
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 7.")


if __name__ == "__main__":
    main()
