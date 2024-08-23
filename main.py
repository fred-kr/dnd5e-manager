import sys

from src.dnd_app.app import EquipmentManager

if __name__ == "__main__":
    # QtWidgets.QApplication.setStyle("Fusion")
    # EquipmentManager.setStyle("Fusion")
    # app = EquipmentManager(sys.argv)
    app = EquipmentManager(sys.argv)
    app.mw.show()
    sys.exit(app.exec())
