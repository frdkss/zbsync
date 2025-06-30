import os
import sys
import subprocess
from PySide6.QtWidgets import QFileDialog, QMessageBox
from logic.scanner import scan
from logic.writer import export_report
from gui.view import MainWindow


class Controller:
    def __init__(self):
        self.view = MainWindow()
        self._connect_signals()
        self.view.show()

    def _connect_signals(self):
        self.view.folderButton.clicked.connect(self._on_browse)
        self.view.goButton.clicked.connect(self._on_go)

    def _on_browse(self):
        folder = QFileDialog.getExistingDirectory(
            self.view, "Выберите папку", os.getcwd()
        )
        if folder:
            self.view.folderLineEdit.setText(folder)

    def _on_go(self):
        folder = self.view.folderLineEdit.text().strip()
        if not folder:
            QMessageBox.warning(self.view, "Внимание", "Укажите папку с файлами.")
            return

        try:
            metas = scan(folder)
        except Exception as e:
            QMessageBox.critical(self.view, "Ошибка сканирования", str(e))
            return

        if not metas:
            QMessageBox.information(self.view, "Результат", "Нет файлов для обработки.")
            return

        try:
            output_path = export_report(metas)
        except Exception as e:
            QMessageBox.critical(self.view, "Ошибка экспорта", str(e))
            return

        try:
            if sys.platform.startswith("win"):
                os.startfile(output_path)
            elif sys.platform == "darwin":
                subprocess.call(["open", output_path])
            else:
                subprocess.call(["xdg-open", output_path])
        except Exception as e:
            QMessageBox.warning(self.view, "Не удалось открыть файл", str(e))
