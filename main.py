import sys

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *

from game import Game
from point import Point
from settings import Settings
from window.settings import Ui_SettingsWindow


class Window2(QWidget):
    game_rules = """
        Правила игры просты!
        Ты должен перекинуть за другую единицу: (1 1 0) -> (0 0 1)
        Ты можешь выбирать уровни и цвет ячеечек в настройках
        Право признать поражение предоставляется пользователю. Удачи :)
    """

    def __init__(self):
        super(QWidget, self).__init__()
        self.setGeometry(100, 100, 250, 200)
        self.setWindowTitle('Правила игры')
        self.label = QTextBrowser(self)
        self.label.setText(Window2.game_rules)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set = None
        self.w2 = None
        self.settings_action = None
        self.how_to_play_action = None
        self.reset_settings_action = None
        self.p1 = Point(-1, -1)
        self.p2 = Point(0, 0)
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('MainWindow')
        self.game = Game(Settings.level_number)
        self.initUI()

    def initUI(self):
        menu = self.menuBar()

        how_to_play_action_menu = menu.addMenu('&Файл')  # +++
        self.how_to_play_action = how_to_play_action_menu.addAction("Правила игры")
        self.reset_game_action = how_to_play_action_menu.addAction("Заново")
        how_to_play_action_menu.triggered.connect(self.show_how_to_play)
        how_to_play_action_menu.triggered.connect(self.reset_game)

        settings_action_menu = menu.addMenu('&Настройки')  # +++
        self.settings_action = settings_action_menu.addAction("Открыть настройки")
        self.reset_settings_action = settings_action_menu.addAction("Восстановить настройки")
        settings_action_menu.triggered.connect(self.show_settings)
        settings_action_menu.triggered.connect(self.reset_settings)

        self.init_grid()

    def init_grid(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 50, 600, 600))
        self.tableWidget.viewport().installEventFilter(self)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.on_right_click)
        self.tableWidget.cellClicked.connect(self.row_column_clicked)
        self.fill_game_grid()

    def fill_game_grid(self):
        self.tableWidget.setRowCount(len(self.game.level))
        self.tableWidget.setColumnCount(len(self.game.level[0]))
        height = len(self.game.level)
        width = len(self.game.level[0])
        for y in range(height):
            for x in range(width):
                content = 1 if self.game.level[y][x] == 1 else 0
                item = QTableWidgetItem(str(content))
                item.setBackground(Settings.color)
                self.tableWidget.setItem(y, x, item)

    def on_right_click(self, qp):
        index = self.tableWidget.indexAt(qp)
        row = index.row()
        col = index.column()
        self.p2 = Point(col, row)
        print(self.p2)
        if self.p1.x < 0 or self.p1.y < 0:
            return
        self.game.do_step(self.p1, self.p2)
        self.fill_game_grid()


    def row_column_clicked(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        self.p1 = Point(col, row)

    def show_how_to_play(self, action):
        if action == self.how_to_play_action:
            self.w2 = Window2()
            self.w2.show()

    def show_settings(self, action):
        if action == self.settings_action:
            self.set = Ui_SettingsWindow()
            self.set.show()

    def reset_settings(self, action):
        if action == self.reset_settings_action:
            Settings.reset_settings()
            self.game = Game(Settings.level_number)
            self.fill_game_grid()

    def reset_game(self, action):
        if action == self.reset_game_action:
            self.game = Game(Settings.level_number)
            self.fill_game_grid()


stylesheet = """
    QTableWidget {
        background-color: black; 
        border-radius: 10px
    }

    QTableWidget::item:selected {
        background-color: yellow;
        color: blue;
    }
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
