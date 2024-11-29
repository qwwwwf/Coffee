import sqlite3


default_coffee_menu = [
    ('Капучино', 'Средняя', 'Молотый', 'Сбалансированный вкус с мягкой пенкой', 3.50, 250),
    ('Экспрессо', 'Темная', 'В зернах', 'Крепкий и насыщенный вкус', 2.00, 30),
    ('Латте макиато', 'Средняя', 'Молотый', 'Сложная смесь кофе и молока с кремовой текстурой', 4.00, 350)
]


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('coffee.sqlite')
        self.cursor = self.connection.cursor()

    def create_table(self) -> None:
        self.cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS menu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255) NOT NULL,
                    roastLevel VARCHAR(255) NOT NULL,
                    grindType VARCHAR(255) NOT NULL,
                    tasteDesc TEXT NOT NULL,
                    price REAL NOT NULL,
                    volume REAL NOT NULL
                )
            """
        )

        if not self.cursor.execute('SELECT * FROM menu').fetchall():
            for coffee_detail in default_coffee_menu:
                self.add_coffee(coffee_detail)

    def add_coffee(self, coffee_details: tuple) -> None:
        self.cursor.execute(
            """
                INSERT INTO menu (name, roastLevel, grindType, tasteDesc, price, volume) VALUES (?, ?, ?, ?, ?, ?)
            """,
            coffee_details
        )
        self.connection.commit()

    def get_all_coffee(self) -> list:
        return self.cursor.execute('SELECT * FROM menu').fetchall()
