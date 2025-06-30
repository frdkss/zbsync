from PySide6.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("zbsync")
        # Больший размер окна
        self.resize(600, 200)

        # Шрифт чуть больше
        font = QFont()
        font.setPointSize(12)

        central = QWidget(self)
        self.setCentralWidget(central)

        # Поле ввода пути
        self.folderLineEdit = QLineEdit()
        self.folderLineEdit.setPlaceholderText("Путь к папке с файлами...")
        self.folderLineEdit.setFont(font)
        self.folderLineEdit.setMinimumHeight(30)

        # Кнопка Browse
        self.folderButton = QPushButton("…")
        self.folderButton.setFont(font)
        self.folderButton.setMinimumHeight(30)

        hl = QHBoxLayout()
        hl.setSpacing(15)  # больше расстояние между элементами
        hl.addWidget(self.folderLineEdit)
        hl.addWidget(self.folderButton)

        # Кнопка Go
        self.goButton = QPushButton("->")
        self.goButton.setFont(font)
        self.goButton.setMinimumHeight(40)

        vl = QVBoxLayout(central)
        vl.setContentsMargins(20, 20, 20, 20)  # большие поля вокруг
        vl.setSpacing(20)  # больше расстояние между строками
        vl.addLayout(hl)
        vl.addWidget(self.goButton)
