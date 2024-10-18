if __name__ == "__main__":
    import sys

    from PySide6 import QtWidgets

    QtWidgets.QApplication.setOrganizationName("QuackTech")
    QtWidgets.QApplication.setApplicationName("DnD5e Manager")

    from src.dnd5e_manager.app import EquipmentManager

    app = EquipmentManager(sys.argv)
    app.mw.show()

    sys.exit(app.exec())
