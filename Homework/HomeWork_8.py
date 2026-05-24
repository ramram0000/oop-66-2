import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);
""")

cursor.execute("DELETE FROM reviews")
cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM movies")

users_data = [('Алексей',), ('Мария',), ('Иван',), ('Светлана',), ('Дмитрий',)]
cursor.executemany("INSERT INTO users (name) VALUES (?);", users_data)

movies_data = [
    ('Начало', 'Научная фантастика'),
    ('Интерстеллар', 'Научная фантастика'),
    ('Темный рыцарь', 'Боевик'),
    ('Зеленая миля', 'Драма'),
    ('Аватар 3', 'Фантастика')
]
cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?);", movies_data)

reviews_data = [
    (1, 1, 9), (1, 2, 10), (2, 1, 8), (2, 3, 10), (3, 2, 9),
    (3, 4, 10), (4, 3, 7), (4, 4, 8), (5, 1, 10), (5, 2, 8), (5, 4, 9)
]
cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?);", reviews_data)
conn.commit()

print("--- 1. Имя пользователя + фильм + оценка ---")
cursor.execute("""
SELECT u.name, m.title, r.rating
FROM reviews r
JOIN users u ON r.user_id = u.id
JOIN movies m ON r.movie_id = m.id;
""")
for row in cursor.fetchall():
    print(f"Пользователь: {row[0]} | Фильм: {row[1]} | Оценка: {row[2]}")

print("\n--- 2. ВСЕ фильмы (даже без отзывов) ---")
cursor.execute("""
SELECT m.title, r.rating
FROM movies m
LEFT JOIN reviews r ON m.id = r.movie_id;
""")
for row in cursor.fetchall():
    print(f"Фильм: {row[0]} | Оценка: {row[1]}")

print("\n--- 3. Агрегации ---")
cursor.execute("SELECT AVG(rating), MAX(rating), MIN(rating) FROM reviews;")
metrics = cursor.fetchone()
print(f"Средняя оценка: {metrics[0]:.2f}")
print(f"Максимальная оценка: {metrics[1]}")
print(f"Минимальная оценка: {metrics[2]}")

conn.close()