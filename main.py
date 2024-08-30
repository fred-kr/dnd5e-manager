if __name__ == "__main__":
    import sys

    from src.dnd5e_manager.app import EquipmentManager

    app = EquipmentManager(sys.argv)
    app.mw.show()

    sys.exit(app.exec())
