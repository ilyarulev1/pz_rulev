# Приложение КОНТРОЛЬ ИСПОЛНЕНИЯ ПОРУЧЕНИЙ для некоторой организации. БД должна содержать таблицу Поручения со следующей структурой записи:
# Порядковый номер поручения, Название поручения, Дата выдачи поручения, Срок исполнения, Исполнитель.

import sqlite3 as sq

info = [
    (1, 'подготовить отчет', '10.05.2025', '17.05.2025', 'Иванов'),
    (2, 'встреча', '11.05.2025', '12.05.2025', 'Петрова'),
    (3, 'заказ канцтоваров', '10.05.2025', '14.05.2025', 'Смирнов'),
    (4, 'проверка исправности техники', '12.05.2025', '11.05.2025', 'Козловов'),
    (5, 'подготовка презентации', '14.05.2025', '20.05.2025', 'Сидорова'),
    (6, 'обновление базы данных', '11.05.2025', '15.05.2025', 'Федоров'),
    (7, 'подготовка договора', '10.05.2025', '13.05.2025', 'Васильева'),
    (8, 'провести аудит', '10.05.2025', '25.05.2025', 'Алексеев'),
    (9, 'организовать мероприятие', '10.05.2025', '30.05.2025', 'Морозова'),
    (10, 'провести совещание', '11.05.2025', '11.05.2025', 'Николаев')
]

with sq.connect('execution_control.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS instruction")
    cur.execute("""CREATE TABLE IF NOT EXISTS instruction(
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    lead_time TEXT NOT NULL,
    executor TEXT NOT NULL
    )""")
    cur.executemany("INSERT INTO instruction VALUES(?, ?, ?, ?, ?)", info)

print("поручение Иванова:")
cur.execute("SELECT * FROM instruction WHERE executor = 'Иванов'")
for row in cur.fetchall():
    print(row)

print("поручения со сроком до 15.05.2025:")
cur.execute("SELECT * FROM instruction WHERE lead_time = '15.05.2025'")
for row in cur.fetchall():
    print(row)

print("поручения 10.05.2025:")
cur.execute("SELECT * FROM instruction WHERE start_date = '10.05.2025'")
for row in cur.fetchall():
    print(row)

cur.execute("DELETE FROM instruction WHERE id = 3")
print("поручение с id=3 удалено")

cur.execute("DELETE FROM instruction WHERE name = 'встреча'")
print("поручение 'встреча' удалено")

cur.execute("DELETE FROM instruction WHERE executor = 'Николаев'")
print("поручение Николаева удалено")

cur.execute("UPDATE instruction SET lead_time = '18.05.2025' WHERE id = 1")
print("изменен срок исполнения")

cur.execute("UPDATE instruction SET executor = 'Петров' WHERE executor = 'Петрова'")
print("исполнителем стал Петров")

cur.execute("UPDATE instruction SET name = 'провести совещание' WHERE name = 'провести аудит'")
print("изменено название поручения на 'провести совещание'")

print('таблица после изменений: ')
for i in cur.execute('SELECT * FROM instruction'):
    print(i)