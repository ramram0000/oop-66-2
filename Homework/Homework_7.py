import sqlite3

DB_NAME = "store.db"


def init_db():
    """Создает базу данных и таблицу products, если они еще не созданы."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """
    )

    conn.commit()
    conn.close()

def create_product(name, price, quantity):
    """Добавляет новый товар в базу данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity),
    )

    conn.commit()
    conn.close()
    print(
        f" Товар '{name}' успешно добавлен! (Цена: {price}, Кол-во: {quantity})"
    )

def read_products():
    """Выводит все товары из базы данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    print("\n--- Список товаров в магазине ---")
    if not products:
        print("База данных пуста.")
        return

    for prod in products:
        print(
            f"ID: {prod[0]} | Название: {prod[1]} | Цена: {prod[2]} руб. | Количество: {prod[3]} шт."
        )
    print("---------------------------------\n")

def update_product(id, price):
    """Обновляет цену товара по его ID."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, id))

    conn.commit()
    conn.close()
    print(f" Цена товара с ID {id} успешно обновлена на {price}.")

def delete_product(id):
    """Удаляет товар по его ID."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id = ?", (id,))

    conn.commit()
    conn.close()
    print(f" Товар с ID {id} успешно удален.")

if __name__ == "__main__":
    init_db()

    print("--- 1. Тестируем CREATE ---")
    create_product("Ноутбук", 45000.50, 5)
    create_product("Мышка", 1200.00, 15)
    create_product("Клавиатура", 2500.00, 8)

    print("\n--- 2. Тестируем READ ---")
    read_products()

    print("--- 3. Тестируем UPDATE ---")
    update_product(2, 1499.90)

    print("\n--- Проверяем изменения (READ) ---")
    read_products()

    print("--- 4. Тестируем DELETE ---")
    delete_product(3)

    print("\n--- Итоговый список товаров (READ) ---")
    read_products()