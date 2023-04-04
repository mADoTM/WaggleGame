from PyQt5.QtGui import QColor


class Settings:
    level_number = 1
    color = QColor(100, 100, 100)

    @staticmethod
    def reset_level_number():
        Settings.level_number = 1

    @staticmethod
    def reset_color():
        Settings.color = QColor(100, 100, 100)

    @staticmethod
    def reset_settings():
        Settings.reset_color()
        Settings.reset_level_number()
