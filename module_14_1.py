import sqlite3
connection = sqlite3.connect('not_telegram.db')
cursor=connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_age ON Users (age)")



balance = 1000
age = 0
for i in range(10): # Заполните её 10 записями:
    age += 10
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i+1}",f"example{i+1}@gmail.com", f"{age}", f"{balance}"))



for i in range(10): # Обновите balance у каждой 2ой записи начиная с 1ой на 500:
    if (i+1) % 2 != 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, f"{i+1}"))


step = 1
while step <= 10: # Удалите каждую 3ую запись в таблице начиная с 1ой:
    cursor.execute("DELETE FROM Users WHERE id = ?", (f"{step}",))
    step += 3

# Выборка по возрасту !=60 в формате Имя, Почта, Возраст, Баланс
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))


users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")


connection.commit()
connection. close()