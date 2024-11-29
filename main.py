import sys
import sqlite3

from db_requests import DataBase
from PyQt6 import QtWidgets, uic


db = DataBase()


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        uic.loadUi('main.ui', self)

        self.setFixedSize(800, 600)

        db.create_table()
        self.load_coffee_data()

    def load_coffee_data(self) -> None:
        coffee_data = db.get_all_coffee()

        table = self.findChild(QtWidgets.QTableWidget, 'coffeeTable')
        table.setRowCount(len(coffee_data))
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(
            ['ID', 'Name', 'Roast Level', 'Grind Type', 'Taste Desc', 'Price', 'Volume'])

        for row, coffee in enumerate(coffee_data):
            for col, item in enumerate(coffee):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(item)))

        table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
